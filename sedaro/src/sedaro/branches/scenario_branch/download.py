import dask.dataframe as dd

class StreamManager:
    def __init__(self):
        self.dataframe = dd.DataFrame()

    def ingest(self, stream_id, stream_data):
        core_data = stream_data[1][stream_id.split('/')[1]]
        self.dataframe = dd.concat([self.dataframe, dd.from_dict(core_data, npartitions=1)], axis=0)

class DownloadManager:
    def __init__(self):
        self.streams = {}

    def ingest(self, page):
        for stream_id, stream_data in page.items():
            if stream_id not in self.streams:
                self.streams[stream_id] = StreamManager()
            self.streams[stream_id].ingest(stream_id, stream_data)

    def archive(self, path):
        for stream_id, stream_manager in self.streams.items():
            stream_manager.dataframe.to_parquet(f"{path}/{stream_id}.parquet", overwrite=True, ignore_divisions=True)