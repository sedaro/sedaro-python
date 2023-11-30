from concurrent.futures import ThreadPoolExecutor
import json
import os
import pathlib
import shutil
import time
from contextlib import contextmanager
from typing import (TYPE_CHECKING, Any, Generator, List, Optional, Tuple,
                    Union)
import uuid6

import numpy as np
from sedaro.results.simulation_result import SimulationResult
from sedaro_base_client.apis.tags import externals_api, jobs_api
from sedaro.branches.scenario_branch.download import DownloadWorker, ProgressBar
from ...exceptions import (NoSimResultsError, SedaroApiException,
                           SimInitializationError)
from ...settings import COMMON_API_KWARGS
from ...utils import body_from_res, parse_urllib_response, progress_bar

if TYPE_CHECKING:
    from ...branches import ScenarioBranch
    from ...sedaro_api_client import SedaroApiClient


def serdes(v):
    if type(v) is dict and 'ndarray' in v:
        return np.array(v['ndarray'])
    if type(v) is np.ndarray:
        return {'ndarray': v.tolist()}
    if type(v) is dict:
        return {k: serdes(v) for k, v in v.items()}
    if type(v) in {list, tuple}:
        return [serdes(v) for v in v]
    return v

def concat_stream_data(main, other, len_main, len_other):
    assert type(main) == dict and type(other) == dict
    for k in other:
        if k not in main:
            main[k] = [None for _ in range(len_main)]
        main[k].extend(other[k])
    for k in main:
        if k not in other:
            main[k].extend([None for _ in range(len_other)])

def concat_stream(main, other, stream_id):
    len_main = len(main[0])
    len_other = len(other[0])
    main[0].extend(other[0])
    stream_id_short = stream_id.split('/')[0]
    concat_stream_data(main[1][stream_id_short], other[1][stream_id_short], len_main, len_other)

def concat_results(main, other):
    for stream in other:
        if stream not in main:
            main[stream] = other[stream]
        else: # concat stream parts
            concat_stream(main[stream], other[stream], stream)

def update_metadata(main, other):
    for k in other['counts']:
        if k not in main['counts']:
            main['counts'][k] = 0
        main['counts'][k] += other['counts'][k]

def set_numeric_as_list(d):
    if not isinstance(d, dict):
        return d
    new_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            if '0' in v.keys():
                nv = []
                for ik in sorted(list(v.keys()), key=lambda x: int(x)):
                    nv.append(set_numeric_as_list(v[ik]))
            else:
                nv = set_numeric_as_list(v)
        else:
            nv = v
        new_dict[k] = nv
    return new_dict

def __set_nested(results):
    nested = {}
    for k in sorted(list(results.keys())):
        v = results[k]
        try:
            ptr = nested
            tokens = k.split('.')
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
        except TypeError:
            ptr = nested
            for token in tokens[:-1]:
                if type(ptr[token]) == list:
                    del ptr[token]
                    break
                else:
                    ptr = ptr[token]
            ptr = nested
            for token in tokens[:-1]:
                if token not in ptr:
                    ptr[token] = {}
                ptr = ptr[token]
            ptr[tokens[-1]] = v
    return nested

# TODO: edge case where one page has all nones for a SV, then the next page has a bunch of vectors for it
def set_nested(results):
    nested = {}
    for k in results:
        kspl = k.split('/')[0]
        nested[k] = (results[k][0], {kspl: set_numeric_as_list(__set_nested(results[k][1][kspl]))})
    return nested

class Simulation:
    """A client to interact with the Sedaro API simulation (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch: 'ScenarioBranch'):
        """Instantiate a Sedaro `Simulation` instance

        Args:
            sedaro (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self.__branch = branch
        self.__branch_id = branch.id
        self.__sedaro = sedaro

    @contextmanager
    def __jobs_client(self) -> Generator['jobs_api.JobsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield jobs_api.JobsApi(api)

    @contextmanager
    def externals_client(self) -> Generator['externals_api.ExternalsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield externals_api.ExternalsApi(api)

    def start(self, wait=False, timeout=None) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Args:
            wait (bool, optional): Triggers waiting for simulation to deploy and transition to `RUNNING` before returning. Defaults to `False`.
            timeout (int, optional): Seconds to wait for simulation to deploy and transition to `RUNNING` before raising an error. Defaults to `None`.

        Returns:
            SimulationHandle
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        handle = SimulationHandle(body_from_res(res), self)
        if not wait:
            return handle

        t = 0
        while t < (timeout or float('inf')):
            if (handle := handle.status())['status'] in {'PENDING', 'QUEUED'}:
                time.sleep(0.1)
                t += 0.1
            elif handle['status'] in {'FAILED', 'ERROR'}:
                raise SimInitializationError(handle['message'])
            else:
                return handle
        raise TimeoutError(f'Simulation did not deploy before timeout of {timeout}.')

    def status(self, job_id: str = None, *, err_if_empty: bool = True) -> 'SimulationHandle':
        """Gets the latest simulation corresponding to the respective Sedaro Scenario Branch id. This can return a
        response even before the simulation is done.

        Args:
            job_id (str, optional): triggers getting the simulation job assocciated with the `id` rather than the\
                default latest.
            err_if_empty (bool, optional): Triggers raising an error if no simulation results and `err_if_empty`.\
                Defaults to `True`.

        Raises:
            NoSimResultsError: if no simulation has been started and `err_if_empty` set to `True`

        Returns:
            SimulationHandle
        """
        if job_id is None:
            with self.__jobs_client() as jobs:
                res = jobs.get_simulations(
                    path_params={'branchId': self.__branch_id},
                    query_params={'latest': ''},
                    **COMMON_API_KWARGS
                )
            if len(body := body_from_res(res)):
                return SimulationHandle(body[0], self)
            if err_if_empty:
                raise NoSimResultsError(
                    status=404,
                    reason=f'Could not find any simulations for scenario: {self.__branch_id}'
                )
            return SimulationHandle(None, self)

        else:
            with self.__jobs_client() as jobs:
                res = jobs.get_simulation(
                    path_params={
                        'branchId': self.__branch_id,
                        'jobId': job_id
                    },
                    **COMMON_API_KWARGS
                )
                return SimulationHandle(body_from_res(res), self)

    def terminate(self, job_id: int = None) -> None:
        """Terminate latest running simulation job corresponding to the respective Sedaro Scenario Branch id. If a
        `job_id` is provided, that simulation job will be terminated rather than the latest.

        Args:
            job_id (`int`, optional): id of the simulation (job) to terminate.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationHandle
        """
        if job_id is None:
            job_id = self.status()['id']

        with self.__jobs_client() as jobs:
            jobs.terminate_simulation(
                path_params={
                    'branchId': self.__branch_id,
                    'jobId': job_id
                },
                **COMMON_API_KWARGS
            )

    def __fetch(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: str = None,
        download_manager = None,
    ):
        if sampleRate is None and continuationToken is None:
            sampleRate = 1

        if id == None:
            id = self.status()['dataArray']
        url = f'/data/{id}?'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            print("WARNING: the parameter `binWidth` is deprecated and will be removed in a future release.")
            url += f'&binWidth={binWidth}'
        elif limit is not None:
            print("WARNING: the parameter `limit` is deprecated and will be removed in a future release.")
            url += f'&limit={limit}'
        streams = streams or []
        if len(streams) > 0:
            encodedStreams = ','.join(['.'.join(x) for x in streams])
            url += f'&streams={encodedStreams}'
        if axisOrder is not None:
            if axisOrder not in {'TIME_MAJOR',  'TIME_MINOR'}:
                raise ValueError(
                    'axisOrder must be either "TIME_MAJOR" or "TIME_MINOR"')
            url += f'&axisOrder={axisOrder}'
        if sampleRate is not None:
            url += f'&sampleRate={sampleRate}'
        if continuationToken is not None:
            url += f'&continuationToken={continuationToken}'
        with self.__sedaro.api_client() as api:
            response = api.call_api(url, 'GET', headers={'Content-Type': 'application/json'})
        _response = None
        has_nonempty_ctoken = False
        try:
            _response = parse_urllib_response(response)
            if 'version' in _response['meta'] and _response['meta']['version'] == 3:
                is_v3 = True
                if download_manager is not None:
                    download_manager.ingest(_response['series'])
                if 'continuationToken' in _response['meta'] and _response['meta']['continuationToken'] is not None:
                    has_nonempty_ctoken = True
                    ctoken = _response['meta']['continuationToken']
            else:
                is_v3 = False
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        if is_v3: # keep fetching pages until we get an empty continuation token
            if has_nonempty_ctoken: # need to fetch more pages
                result = _response
                while has_nonempty_ctoken:
                    # fetch page
                    request_url = f'/data/{id}?&continuationToken={ctoken}'
                    page = api.call_api(request_url, 'GET', headers={'Content-Type': 'application/json'})
                    _page = parse_urllib_response(page)
                    if download_manager is not None:
                        download_manager.ingest(_page['series'])
                    try:
                        if 'continuationToken' in _page['meta'] and _page['meta']['continuationToken'] is not None:
                            has_nonempty_ctoken = True
                            ctoken = _page['meta']['continuationToken']
                        else:
                            has_nonempty_ctoken = False
                        if page.status != 200:
                            raise Exception()
                    except Exception:
                        reason = _page['error']['message'] if _page and 'error' in _page else 'An unknown error occurred.'
                        raise SedaroApiException(status=page.status, reason=reason)
                    concat_results(result['series'], _page['series'])
                    update_metadata(result['meta'], _page['meta'])
                _response = result
            if download_manager is None:
                _response['series'] = set_nested(_response['series'])
        if download_manager is None:
            return _response
        else:
            download_manager.archive()

    def results_plain(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: str = None,
    ):
        """Query latest scenario and return results as a plain dictionary from the Data Service with options to
        customize the response. If an `id` is passed, query for corresponding result rather than latest.

        Args:
            id (str, optional): `id` of the data array to fetch (found on `dataArray` attribute on a response from the\
                `status` or `start` methods)

            start (float, optional): the start time of the data to fetch, in MJD format. Defaults to the start of the\
                simulation.

            stop (float, optional): the end time of the data to fetch, in MJD format. Defaults to the end of the\
                simulation.

            limit (int, optional): the maximum number of points in time for which to fetch data for any stream. If not
                specified, there is no limit and data is fetched at full resolution. If a limit is specified, the\
                duration of the time from `start` to `stop` is divided into the specified number of bins of equal\
                duration, and data is selected from at most one point in time within each bin. Not that it is not\
                guaranteed that you will receive exactly as many points in time as the limit you specify; you may\
                receive fewer, depending on the length of a data stream and/or the distribution of data point timestamps\
                through the simulation.

            binWidth (float, optional): the width of the bins used in downsampling data, as described for `limit`. Note\
                that `binWidth` and `limit` are not meant to be used together; undefined behavior may occur. If you\
                would like to downsample data, use either `limit` or `binWidth`, but not both.

            streams (list, optional): specify which data streams you would like to fetch data for, according to the\
                format described in the docstring for the `results` method below. If no list is provided,\
                data is fetched for all streams.

            axisOrder (enum, optional): the shape of each series in the response. Options: `'TIME_MAJOR'` and\
                `'TIME_MINOR'`. Default value, if not specified, is `'TIME_MAJOR'`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: response from the `get` request
        """

        return self.__fetch(
            id=id,
            start=start,
            stop=stop,
            binWidth=binWidth,
            limit=limit,
            axisOrder=axisOrder,
            streams=streams,
            sampleRate=sampleRate,
            continuationToken=continuationToken,
        )

    def results(self,
                job_id: str = None,
                start: float = None,
                stop: float = None,
                streams: Optional[List[Tuple[str, ...]]] = None,
                sampleRate: int = None) -> SimulationResult:
        """Query latest scenario result. If a `job_id` is passed, query for corresponding sim results rather than
        latest.

        If no argument is provided for `streams`, all data will be fetched. If you pass an argument to `streams`, it
        must be a list of tuples following particular rules:

        - Each tuple in the list can contain either 1 or 2 items.
        - If a tuple contains 1 item, that item must be the agent ID, as a string. Data for all engines of this agent\
            will be fetched. Remember that a 1-item tuple is written like `(foo,)`, NOT like `(foo)`.
        - If a tuple contains 2 items, the first item must be the same as above. The second item must be one of the\
            following strings, specifying an engine: `'GNC`, `'CDH'`, `'Thermal'`, `'Power'`. Data for the specified\
            agent of this engine will be fetched.

        For example, with the following code, `results` will only contain data for all engines of agent `foo` and the
        `Power` and `Thermal` engines of agent `bar`.

        ```py
        selected_streams=[
            ('foo',),
            ('bar', 'Thermal'),
            ('bar', 'Power')
        ]
        results = sim.results(streams=selected_streams)
        ```

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        '''Query latest scenario result.'''
        job = self.status(job_id)
        data = self.results_plain(id=job['dataArray'], start=start, stop=stop, streams=streams or [], sampleRate=sampleRate)
        return SimulationResult(job, data)

    def results_poll(
        self,
        job_id: str = None,
        streams: List[Tuple[str, ...]] = None,
        sampleRate: int = None,
        retry_interval: int = 2,
    ) -> SimulationResult:
        """Query latest scenario result and wait for sim to finish if it's running. If a `job_id` is passed, query for
        corresponding sim results rather than latest. See `results` method for details on using the `streams` kwarg.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        job = self.status(job_id)
        options = {'QUEUED', 'PENDING', 'RUNNING'}

        while job['status'] in options:
            if job['status'] == 'QUEUED':
                print('Simulation is queued...', end='\r')
            if job['status'] == 'PENDING':
                print('Simulation is building...', end='\r')
            else:
                progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        return self.results(streams=streams or [], sampleRate=sampleRate)

    def __get_metadata(self, sim_id: str = None):
        request_url = f'/data/metadata/{sim_id}?'
        with self.__sedaro.api_client() as api:
            response = api.call_api(request_url, 'GET', headers={'Content-Type': 'application/json'})
        response_dict = json.loads(response.data)
        return response_dict

    def __downloadInParallel(self, sim_id, streams, tmpdir, filename, download_bar, archive_bar):
        download_worker = DownloadWorker(tmpdir, filename, download_bar, archive_bar)
        streams_fmt = [tuple(stream.split('.')) for stream in streams]
        self.__fetch(id=sim_id, streams=streams_fmt, sampleRate=1, download_manager=download_worker)

    def download(
        self,
        data_array_id: str = None,
        filename: str = None,
        agent_ids: List[str] = None,
        num_workers: int = 2,
        overwrite: bool = False
    ):

        if not overwrite and pathlib.Path(filename).exists():
            raise FileExistsError(
                f'The file {filename} already exists. Please delete it or provide a different filename via the `filename` argument.')

        job_id = self.status(data_array_id)
        metadata = self.__get_metadata(sim_id := job_id['dataArray'])
        if agent_ids is not None:
            metadata['streams'] = agent_ids
        os.mkdir(tmpdir := f".{uuid6.uuid7()}")

        success = False
        try:
            workers = [[] for _ in range(num_workers)]
            for i, stream in enumerate(metadata['streams']):
                workers[i % num_workers].append(stream)
            download_bar = ProgressBar(metadata['start'], metadata['stop'], len(metadata['streams']), "Downloading...")
            archive_bar = ProgressBar(None, None, len(metadata['streams']), "Archiving...")

            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                executor.map(self.__downloadInParallel,
                            [sim_id] * num_workers,
                            workers,
                            [tmpdir] * num_workers,
                            [filename] * num_workers,
                            [download_bar] * num_workers,
                            [archive_bar] * num_workers)
                executor.shutdown(wait=True)
            download_bar.complete()
            archive_bar.bar.close()

            print("Building zip file...")
            shutil.make_archive(tmpzip := f"{uuid6.uuid7()}", 'zip', tmpdir)
            curr_zip_base = ''
            # if the path is to another directory, make that directory if nonexistent, and move the zip there
            if len(path_split := filename.split('/')) > 1:
                path_dirs = '/'.join(path_split[:-1])
                pathlib.Path(path_dirs).mkdir(parents=True, exist_ok=True)
                shutil.move(f"{tmpzip}.zip", f"{(curr_zip_base := path_dirs)}/{tmpzip}.zip")
                zip_desired_name = path_split[-1]
            else:
                zip_desired_name = filename
            # rename zip to specified name
            if len(curr_zip_base) > 0:
                zip_new_path = f"{curr_zip_base}/{zip_desired_name}"
                curr_zip_name = f"{curr_zip_base}/{tmpzip}"
            else:
                zip_new_path = zip_desired_name
                curr_zip_name = tmpzip
            os.rename(f"{curr_zip_name}.zip", zip_new_path)
            # remove tmpdir
            os.system(f"rm -r {tmpdir}")
            success = True
            print(f"Successfully archived at {zip_new_path}")
        except Exception as e:
            raise e
        finally: # remove tmpdir even if an error occurs
            if not success:
                os.system(f"rm -r {tmpdir}")

class SimulationJob:
    def __init__(self, job: Union[dict, None]): self.__job = job
    def get(self, key, default=None): return self.__job.get(key, default)

    def __getitem__(self, key):
        if self.__job:
            if key in self.__job:
                return self.__job[key]
            else:
                raise KeyError(
                    f'Key {key} not found in SimulationJob object. Available values are: {self.__job.keys()}')
        else:
            raise Exception(
                'No simulation is running. It was either terminated or one was never started.')


class SimulationHandle:

    def __init__(self, job: Union[dict, None], sim_client: Simulation):
        self.__job = SimulationJob(job)
        self.__sim_client = sim_client

    def __getitem__(self, key): return self.__job[key]
    def get(self, key, default=None): return self.__job.get(key, default)

    def status(self, err_if_empty: bool = True):
        """Refreshes the local simulation status.

        Args:
            err_if_empty (bool, optional): Triggers raising an error if no simulation results and `err_if_empty`.\
                Defaults to `True`.

        Raises:
            NoSimResultsError: if no simulation has been started and `err_if_empty` set to `True`

        Returns:
            SimulationHandle (self)
        """
        return (self := self.__sim_client.status(self.__job['id'], err_if_empty=err_if_empty))

    def terminate(self):
        """Terminate the running simulation.

        Returns:
            SimulationHandle (self)
        """
        self.__sim_client.terminate(self.__job['id'])
        return self

    def results_plain(
        self,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: bytes = None,
    ):
        """Query simulation results as a plain dictionary from the Data Service with options to
        customize the response.

        Args:
            start (float, optional): the start time of the data to fetch, in MJD format. Defaults to the start of the\
                simulation.

            stop (float, optional): the end time of the data to fetch, in MJD format. Defaults to the end of the\
                simulation.

            limit (int, optional): the maximum number of points in time for which to fetch data for any stream. If not
                specified, there is no limit and data is fetched at full resolution. If a limit is specified, the\
                duration of the time from `start` to `stop` is divided into the specified number of bins of equal\
                duration, and data is selected from at most one point in time within each bin. Not that it is not\
                guaranteed that you will receive exactly as many points in time as the limit you specify; you may\
                receive fewer, depending on the length of a data stream and/or the distribution of data point timestamps\
                through the simulation.

            binWidth (float, optional): the width of the bins used in downsampling data, as described for `limit`. Note\
                that `binWidth` and `limit` are not meant to be used together; undefined behavior may occur. If you\
                would like to downsample data, use either `limit` or `binWidth`, but not both.

            streams (list, optional): specify which data streams you would like to fetch data for, according to the\
                format described in the previous section. If no list is provided, data is fetched for all streams.

            axisOrder (enum, optional): the shape of each series in the response. Options: `'TIME_MAJOR'` and\
                `'TIME_MINOR'`. Default value, if not specified, is `'TIME_MAJOR'`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: response from the `get` request
        """
        return self.__sim_client.results_plain(
            id=self.__job['dataArray'],
            start=start,
            stop=stop,
            binWidth=binWidth,
            limit=limit,
            axisOrder=axisOrder,
            streams=streams,
            sampleRate=sampleRate,
            continuationToken=continuationToken,
        )

    def results(self, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
        """Query simulaiton results.

        If no argument is provided for `streams`, all data will be fetched. If you pass an argument to `streams`, it
        must be a list of tuples following particular rules:

        - Each tuple in the list can contain either 1 or 2 items.
        - If a tuple contains 1 item, that item must be the agent ID, as a string. Data for all engines of this agent\
            will be fetched. Remember that a 1-item tuple is written like `(foo,)`, NOT like `(foo)`.
        - If a tuple contains 2 items, the first item must be the same as above. The second item must be one of the\
            following strings, specifying an engine: `'GNC`, `'CDH'`, `'Thermal'`, `'Power'`. Data for the specified\
            agent of this engine will be fetched.

        For example, with the following code, `results` will only contain data for all engines of agent `foo` and the
        `Power` and `Thermal` engines of agent `bar`.

        ```py
        selected_streams=[
            ('foo',),
            ('bar', 'Thermal'),
            ('bar', 'Power')
        ]
        results = sim.results(streams=selected_streams)
        ```

        Args:
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results(job_id=self.__job['id'], streams=streams)

    def results_poll(
        self,
        streams: List[Tuple[str, ...]] = None,
        retry_interval: int = 2
    ) -> SimulationResult:
        """Query simulation results but wait for sim to finish if it's running. See `results` method for details on using the `streams` kwarg.

        Args:
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results_poll(
            job_id=self.__job['id'],
            streams=streams,
            retry_interval=retry_interval
        )

    def download(
        self,
        streams: List[Tuple[str, ...]] = None,
        filename: str = None,
        workers: int = 2,
        overwrite: bool = False
    ):
        return self.__sim_client.download(self.__job['id'], filename=filename, workers=workers, agent_ids=streams, overwrite=overwrite)

    def consume(self, agent_id: str, external_state_id: str, time: float = None):
        with self.__sim_client.externals_client() as externals_client:
            response = externals_client.get_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                query_params=({'time': time} if time is not None else {}),
                **COMMON_API_KWARGS,
            )
        return tuple(serdes(v) for v in body_from_res(response))

    def produce(self, agent_id: str, external_state_id: str, values: tuple, timestamp: float = None):
        if type(values) is not tuple:
            raise TypeError(
                '`values` must be passed as a tuple of one or more state variable values (ex. `([x, y, z],)` where `[x, y, z]` is the external state]).')
        with self.__sim_client.externals_client() as externals_client:
            response = externals_client.put_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                body=({
                    **{'values': [serdes(v) for v in values]},
                    **({'timestamp': timestamp} if timestamp is not None else {})
                }),
                **COMMON_API_KWARGS,
            )
        return tuple(serdes(v) for v in body_from_res(response))
