# import warnings

# from tqdm import TqdmWarning, tqdm

# imprecision of float math sometimes forces Tqdm to clamp a number to a range
# this suppresses the warning that prints each time that happens
# warnings.filterwarnings('ignore', category=TqdmWarning)

class NonTqdmProgressBar:
    def __init__(self, *args, **kwargs):
        print("Downloading...")
        self.n = 0
        pass

    def update(self, *args, **kwargs):
        pass

    def refresh(self):
        pass

    def close(self):
        print("...download complete!")


class ProgressBar:
    def __init__(self, start, stop, num_streams, desc):
        # self.bar = tqdm(range(num_streams), desc=desc,  bar_format='{l_bar}{bar}[{elapsed}<{remaining}]')
        self.bar = NonTqdmProgressBar()
        self.num_streams = num_streams
        self.start = start
        self.stop = stop
        self.prev = {}

    def update(self, stream_id, new):
        # used for the download progress bar. Updates the progress bar based on the time range
        # fetched for a stream by the latest page.
        if stream_id not in self.prev:
            self.prev[stream_id] = 0
        if new > self.stop:
            new = self.stop
        incr = ((new - self.start) / (self.stop - self.start)) - self.prev[stream_id]
        # sometimes the elapsed time goes over the sim stop time
        # this would cause the progress bar to go over 100%, so we clamp it
        self.bar.update(min(incr, self.num_streams - self.bar.n))
        self.bar.refresh()
        self.prev[stream_id] = incr

    def complete(self):
        # set the progress bar to EXACTLY 100% and close it
        self.bar.update(self.num_streams - self.bar.n)  # see https://github.com/tqdm/tqdm/issues/1264
        self.bar.refresh()
        self.bar.close()


class StreamManager:
    def __init__(self, download_bar):
        self.dataframe = None
        self.keys = set()
        self.download_bar = download_bar

    def ingest_core_data(self, stream_id, core_data):
        import dask.dataframe as dd
        if self.dataframe is None:
            self.dataframe = dd.from_dict(core_data, npartitions=1)
        else:
            self.dataframe = dd.concat([self.dataframe, dd.from_dict(core_data, npartitions=1)], axis=0)
        self.keys.update(core_data.keys())
        self.download_bar.update(stream_id, core_data['time'][-1])

    def ingest(self, stream_id, stream_data):
        core_data = stream_data[1][stream_id.split('/')[0]]
        self.ingest_core_data(stream_id, core_data)

    def select_columns_to_remove(self):
        columns_to_remove = set()
        for column in self.keys:
            for other_column in self.keys:
                if column != other_column and column in other_column:
                    # the below check ensures that it's a parent column, not just a column with a shared prefix
                    # for instance, we want to remove 'position' if 'position.x' is present, but not if only 'positionx' is present
                    if other_column[len(column)] == '.':
                        columns_to_remove.add(column)
        return list(columns_to_remove)

    def filter_columns(self):
        """Remove columns whose name is a parent of another column's name."""
        columns_to_remove = self.select_columns_to_remove()
        if not columns_to_remove:
            return
        self.dataframe = self.dataframe.drop(columns_to_remove, axis=1)

    def finalize(self):
        return self.dataframe.set_index('time')


def prep_stream_id(stream_id):
    engines = {
        '0': 'GNC',
        '1': 'CDH',
        '2': 'Power',
        '3': 'Thermal'
    }
    split_base = stream_id.split('/')
    prepped_stream_id = f"{split_base[0]}.{engines[split_base[1]]}"
    return prepped_stream_id


class DownloadWorker:
    def __init__(self, download_bar):
        self.download_bar = download_bar
        self.streams = {}

    def ingest(self, page):
        for stream_id, stream_data in page.items():
            if stream_id not in self.streams:
                self.streams[stream_id] = StreamManager(self.download_bar)
            self.streams[stream_id].ingest(stream_id, stream_data)

    def finalize(self):
        for _, stream_manager in self.streams.items():
            # REF 1: https://docs.dask.org/en/stable/dataframe-best-practices.html#repartition-to-reduce-overhead
            stream_manager.dataframe = stream_manager.dataframe.repartition(partition_size="100MB")  # REF 1
            stream_manager.dataframe = stream_manager.dataframe.reset_index(drop=True)
            stream_manager.filter_columns()
            stream_manager.dataframe = stream_manager.dataframe.persist()
        for k in self.streams:
            self.streams[k] = self.streams[k].finalize()

    def add_metadata(self, metadata):
        self.metadata = metadata

    def update_metadata(self, new_metadata):
        for k in new_metadata['counts']:
            if k not in self.metadata['counts']:
                self.metadata['counts'][k] = 0
            self.metadata['counts'][k] += new_metadata['counts'][k]

    def finalize_metadata(self, others: "list[DownloadWorker]"):
        for other in others:
            self.update_metadata(other.metadata)
        return self.metadata
