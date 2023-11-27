import dask.dataframe as dd
import os
from uuid import uuid6
import zipfile

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
            # temp working directory
            os.mkdir(tmpdir := uuid6())
            stream_manager.dataframe.to_parquet(f"{tmpdir}/{stream_id}.parquet", overwrite=True, ignore_divisions=True)
            # zip and move to specified path
            path_end = path.split('/')[-1]
            with zipfile.ZipFile(f"{tmpdir}/{path_end}.zip", 'w') as zip:
                for file in os.listdir(tmpdir):
                    if file.endswith('.parquet'):
                        zip.write(f"{tmpdir}/{file}")