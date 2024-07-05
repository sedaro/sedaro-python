import json
import msgpack
import requests
from typing import List, Tuple, TYPE_CHECKING

from ...utils import parse_urllib_response

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient

class FastFetcherResponse:
    def __init__(self, response: requests.Response):
        self.type = response.headers['Content-Type']

        if self.type == 'application/json':
            self.data = response.text
        elif self.type == 'application/msgpack':
            self.data = response.content
        else:
            raise Exception(
                f"Unexpected MIME type: {self.type}.  Response content: {response.content}. Status Code: {response.status_code}")

        self.status = response.status_code
        self.response = response

    def __getattr__(self, key):
        return self.response[key]

    def parse(self):
        if self.type == 'application/json':
            return parse_urllib_response(self)
        elif self.type == 'application/msgpack':
            return msgpack.unpackb(self.data)
        else:
            raise Exception(
                f"Unexpected MIME type: {self.response.headers['Content-Type']}.  Response content: {self.data}. Status Code: {self.response.status_code}")


class FastFetcher:
    """Accelerated request handler for data page fetching."""

    def __init__(self, sedaro_api: 'SedaroApiClient'):
        self.sedaro_api = sedaro_api

    def get(self, url):
        return FastFetcherResponse(self.sedaro_api.request.requests_lib_get(url))


def _get_metadata(_sedaro: 'SedaroApiClient', sim_id: str = None, num_workers: int = None):
    if num_workers is None:
        request_url = f'/data/{sim_id}/metadata'
    else:
        request_url = f'/data/{sim_id}/metadata?numTokens={num_workers}'
    with _sedaro.api_client() as api:
        response = api.call_api(request_url, 'GET', headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json',  # Required for Sedaro firewall
        })
    response_dict = json.loads(response.data)
    return response_dict

def _get_filtered_streams(requested_streams: list, metadata: dict):
    streams_raw = metadata['streams']
    streams_true = {}
    for stream in streams_raw:
        stream_parts = stream.split('.')
        if stream_parts[0] not in streams_true:
            streams_true[stream_parts[0]] = []
        streams_true[stream_parts[0]].append(stream_parts[1])
    filtered_streams = []
    for stream in requested_streams:
        if stream[0] in streams_true:
            if len(stream) == 1:
                for v in streams_true[stream[0]]:
                    filtered_streams.append((stream[0], v))
            else:
                if stream[0] in streams_true:
                    if stream[1] in streams_true[stream[0]]:
                        filtered_streams.append(stream)
    return filtered_streams

def _get_stats_for_sim_id(
    _sedaro: 'SedaroApiClient',
    sim_id: str,
    streams: List[Tuple[str, ...]] = None
):
    request_url = f'/data/{sim_id}/stats/'
    if streams is not None:
        metadata = _get_metadata(_sedaro, sim_id)
        filtered_streams = _get_filtered_streams(streams, metadata)
        encoded_streams = ','.join(['.'.join(x) for x in filtered_streams])
        request_url += f"?streams={encoded_streams}"
    stats = {}

    # get first page
    fast_fetcher = FastFetcher(_sedaro)
    response = fast_fetcher.get(request_url)
    if response.status != 200:
        if response.status == 409: # stats not yet available
            return None, False
        else:
            raise Exception(f"Failed to get stats for sim_id {sim_id}.  Status code: {response.status}.  Response: {response.data}")
    contents = response.parse()
    stats.update(contents['stats'])

    # get additional pages (if applicable)
    while contents['continuationToken'] is not None:
        token = contents['continuationToken']
        request_url = f'/data/{sim_id}/stats/?continuationToken={token}'
        response = fast_fetcher.get(request_url)
        contents = response.parse()
        stats.update(contents['stats'])

    return stats, True
