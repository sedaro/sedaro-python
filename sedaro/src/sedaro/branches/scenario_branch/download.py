import dask.dataframe as dd
import os
from pathlib import Path
import shutil
from tqdm import tqdm
from tqdm import TqdmWarning
import uuid6
import warnings

# imprecise float math sometimes forces Tqdm to clamp a number to a range
# this suppresses the warning that prints each time that happens
warnings.filterwarnings('ignore', category=TqdmWarning)

class ProgressBar:
    def __init__(self, start, stop, num_streams):
        self.bar = tqdm(range(num_streams), desc='Downloading...', bar_format='{l_bar}{bar}[{elapsed}<{remaining}]')
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

    def complete(self):
        self.bar.update(self.num_streams - self.bar.n) # see https://github.com/tqdm/tqdm/issues/1264
        self.bar.refresh()
        self.bar.close()

class StreamManager:
    def __init__(self):
        self.dataframe = None
        # self.progress_bar = ProgressBar(position, start, stop)

    def ingest(self, stream_id, stream_data):
        core_data = stream_data[1][stream_id.split('/')[0]]
        if self.dataframe is None:
            self.dataframe = dd.from_dict(core_data, npartitions=1)
        else:
            self.dataframe = dd.concat([self.dataframe, dd.from_dict(core_data, npartitions=1)], axis=0)

class DownloadManager:
    def __init__(self, meta):
        self.streams = {}
        self.position = 0
        self.progress_bar = ProgressBar(meta['start'], meta['stop'], meta['numStreams'])

    def newStreamManager(self):
        sm = StreamManager()
        return sm

    def ingest(self, page):
        for stream_id, stream_data in page.items():
            if stream_id not in self.streams:
                self.streams[stream_id] = self.newStreamManager()
            self.streams[stream_id].ingest(stream_id, stream_data)
            self.progress_bar.update(stream_id, stream_data[1][stream_id.split('/')[0]]['time'][-1])

    def archive(self, path):
        # create temp working directory
        os.mkdir(tmpdir := f".{uuid6.uuid7()}")
        self.progress_bar.complete()
        # build parquet files in tmpdir
        progress_bar = tqdm(range(len(self.streams)), desc='Archiving...')
        for stream_id, stream_manager in self.streams.items():
            stream_manager.dataframe = stream_manager.dataframe.repartition(npartitions=1)
            stream_manager.dataframe.to_parquet(f"{tmpdir}/{stream_id.replace('/', '!')}", overwrite=True, ignore_divisions=True)
            progress_bar.update(1) # increment progress bar
            progress_bar.refresh()
        progress_bar.close()
        # use shutil to make zip in working directory with provisional name
        shutil.make_archive(tmpzip := f"{uuid6.uuid7()}", 'zip', tmpdir)
        curr_zip_base = ''
        # if the path is to another directory, make that directory if nonexistent, and move the zip there
        if len(path_split := path.split('/')) > 1:
            path_dirs = '/'.join(path_split[:-1])
            Path(path_dirs).mkdir(parents=True, exist_ok=True)
            shutil.move(f"{tmpzip}.zip", f"{(curr_zip_base := path_dirs)}/{tmpzip}.zip")
            zip_desired_name = path_split[-1]
        else:
            zip_desired_name = path
        # rename zip to specified name
        if len(curr_zip_base) > 0:
            zip_new_path = f"{curr_zip_base}/{zip_desired_name}"
            curr_zip_name = f"{curr_zip_base}/{tmpzip}"
        else:
            zip_new_path = zip_desired_name
            curr_zip_name = tmpzip
        os.rename(f"{curr_zip_name}.zip", zip_new_path)
        # remove tmpdir
        os.system(f"rm -r {tmpdir}") # TODO: make this safer