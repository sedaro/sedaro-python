import dask.dataframe as dd
from tqdm import tqdm
from tqdm import TqdmWarning
import warnings

# imprecision of float math sometimes forces Tqdm to clamp a number to a range
# this suppresses the warning that prints each time that happens
warnings.filterwarnings('ignore', category=TqdmWarning)

class ProgressBar:
    def __init__(self, start, stop, num_streams, desc):
        self.bar = tqdm(range(num_streams), desc=desc,  bar_format='{l_bar}{bar}[{elapsed}<{remaining}]')
        self.num_streams = num_streams
        self.start = start
        self.stop = stop
        self.prev = {}

    def update(self, stream_id, new):
        if stream_id not in self.prev:
            self.prev[stream_id] = 0
        if new > self.stop:
            new = self.stop
        incr = ((new - self.start) / (self.stop - self.start)) - self.prev[stream_id]
        self.bar.update(min(incr, self.num_streams - self.bar.n))
        self.bar.refresh()
        self.prev[stream_id] = incr

    def incr1(self):
        self.bar.update(1)
        self.bar.refresh()

    def complete(self):
        self.bar.update(self.num_streams - self.bar.n) # see https://github.com/tqdm/tqdm/issues/1264
        self.bar.refresh()
        self.bar.close()

class StreamManager:
    def __init__(self, download_bar):
        self.dataframe = None
        self.keys = set()
        self.download_bar = download_bar

    def ingest(self, stream_id, stream_data):
        core_data = stream_data[1][stream_id.split('/')[0]]
        if self.dataframe is None:
            self.dataframe = dd.from_dict(core_data, npartitions=1)
        else:
            self.dataframe = dd.concat([self.dataframe, dd.from_dict(core_data, npartitions=1)], axis=0)
        self.keys.update(core_data.keys())
        self.download_bar.update(stream_id, core_data['time'][-1])

    def filter_columns(self):
        """Remove columns whose name is a strict prefix of another column's name."""
        columns_to_remove = set()
        for column in self.keys:
            for other_column in self.keys:
                if column != other_column and column != 'time' and column in other_column:
                    columns_to_remove.add(column)
        self.dataframe = self.dataframe.drop(columns_to_remove, axis=1)

class DownloadWorker:
    def __init__(self, tmpdir, filename, download_bar, archive_bar):
        self.tmpdir = tmpdir
        self.filename = filename
        self.download_bar = download_bar
        self.archive_bar = archive_bar
        self.streams = {}
        self.stream_keys = {}

    def ingest(self, page):
        for stream_id, stream_data in page.items():
            if stream_id not in self.streams:
                self.streams[stream_id] = StreamManager(self.download_bar)
            self.streams[stream_id].ingest(stream_id, stream_data)

    def archive(self):
        for stream_id, stream_manager in self.streams.items():
            stream_manager.dataframe = stream_manager.dataframe.repartition(npartitions=1)
            stream_manager.filter_columns()
            stream_manager.dataframe.to_parquet(f"{self.tmpdir}/{stream_id.replace('/', '!')}", overwrite=True, ignore_divisions=True)
            self.archive_bar.incr1()