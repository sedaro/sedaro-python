import time
from concurrent.futures import ThreadPoolExecutor
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Generator, List, Optional, Tuple, Union

from sedaro_base_client.apis.tags import externals_api, jobs_api
from urllib3.response import HTTPResponse

from sedaro.branches.scenario_branch.download import DownloadWorker, ProgressBar
from sedaro.results.simulation_result import SimulationResult

from ...exceptions import (NoSimResultsError, SedaroApiException,
                           SimInitializationError)
from ...settings import (BAD_STATUSES, COMMON_API_KWARGS, PRE_RUN_STATUSES,
                         QUEUED, RUNNING, STATUS)
from ...utils import body_from_res, progress_bar
from .utils import FastFetcher, _get_filtered_streams, _get_metadata, _get_stats_for_sim_id

if TYPE_CHECKING:
    import dask.dataframe as dd

    from ...branches import ScenarioBranch
    from ...sedaro_api_client import SedaroApiClient


def serdes(v):
    import numpy as np
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
        else:  # concat stream parts
            concat_stream(main[stream], other[stream], stream)


def update_metadata(main, other):
    for k in other['counts']:
        if k not in main['counts']:
            main['counts'][k] = 0
        main['counts'][k] += other['counts'][k]


def set_numeric_as_list(d):
    if isinstance(d, dict):
        if all(key.isdigit() for key in d.keys()):  # Check if all keys are array indexes in string form
            return [set_numeric_as_list(d[key]) for key in sorted(d.keys(), key=int)]
        else:
            return {k: set_numeric_as_list(v) for k, v in d.items()}
    return d


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

    def start(
        self, 
        wait=False, 
        timeout=None, 
        label=None,
        capacity=None,
        seed=None,
        **kwargs,
    ) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Args:
            wait (bool, optional): Triggers waiting for simulation to deploy and transition to `RUNNING` before returning. Defaults to `False`.
            timeout (int, optional): Seconds to wait for simulation to deploy and transition to `RUNNING` before raising an error. Defaults to `None`.
            label (str, optional): A label to assign to the simulation job. Defaults to `None`.
            capacity (int, optional): The capacity to allocate to the simulation. Defaults to using the lesser of the Workspace capacity and the number of Agents in the Scenario.
            seed (int, optional): The pseudorandom seed to use for the simulation. Defaults to the Simulation Service's default.
            **kwargs: Additional keyword arguments to pass to the simulation job as part of the HTTP request body.

        Returns:
            SimulationHandle
        """
        body = {**kwargs}
        if label is not None:
            body['label'] = label
        if capacity is not None:
            body['capacity'] = capacity
        if seed is not None:
            body['seed'] = seed
            
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                body,
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        handle = SimulationHandle(body_from_res(res), self)
        if not wait:
            return handle

        t = 0
        while t < (timeout or float('inf')):
            if (handle := handle.status())[STATUS] in PRE_RUN_STATUSES:
                time.sleep(0.1)
                t += 0.1
            elif handle[STATUS] in BAD_STATUSES:
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
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: str = None,
        usesStreamTokens: bool = False,
        download_manager: DownloadWorker = None,
    ):
        if sampleRate is None and continuationToken is None:
            sampleRate = 1

        fast_fetcher = FastFetcher(self.__sedaro)

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
        if not usesStreamTokens:
            streams = streams or []
            if len(streams) > 0:
                encodedStreams = ','.join(['.'.join(x) for x in streams])
                url += f'&streams={encodedStreams}'
        elif streams is not None:
            url += f'&streamsToken={streams}'
        url += f'&axisOrder=TIME_MINOR'
        if sampleRate is not None:
            url += f'&sampleRate={sampleRate}'
        if continuationToken is not None:
            url += f'&continuationToken={continuationToken}'
        url += '&encoding=msgpack'

        response = fast_fetcher.get(url)
        _response = None
        has_nonempty_ctoken = False
        try:
            _response = response.parse()
            if 'version' in _response['meta'] and _response['meta']['version'] == 3:
                is_v3 = True
                download_manager.ingest(_response['series'])
                download_manager.add_metadata(_response['meta'])
                if 'continuationToken' in _response['meta'] and _response['meta']['continuationToken'] is not None:
                    has_nonempty_ctoken = True
                    ctoken = _response['meta']['continuationToken']
                if 'stats' in _response:
                    download_manager.update_stats(_response['stats'])
            else:
                is_v3 = False
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        if is_v3:  # keep fetching pages until we get an empty continuation token
            if has_nonempty_ctoken:  # need to fetch more pages
                while has_nonempty_ctoken:
                    # fetch page
                    request_url = f'/data/{id}?&continuationToken={ctoken}'
                    page = fast_fetcher.get(request_url)
                    _page = page.parse()
                    download_manager.ingest(_page['series'])
                    download_manager.update_metadata(_page['meta'])
                    try:
                        if 'stats' in _page:
                            download_manager.update_stats(_page['stats'])
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
        download_manager.finalize()

    def __downloadInParallel(self, sim_id, streams, params, download_manager, usesStreamTokens):
        try:
            start = params['start']
            stop = params['stop']
            sampleRate = params['sampleRate']
            streams_formatted = []
            if usesStreamTokens:
                streams_formatted = streams
            else:  # not usesStreamTokens
                for stream in streams:
                    if type(stream) == tuple:
                        streams_formatted.append(stream)
                    else:
                        streams_formatted.append(tuple(stream.split('.')))
            self.__fetch(
                id=sim_id, streams=streams_formatted, sampleRate=sampleRate, start=start,
                stop=stop, usesStreamTokens=usesStreamTokens, download_manager=download_manager
            )
        except Exception as e:
            return e

    def __results(
        self,
        job: 'SimulationHandle' = None,
        start: float = None,
        stop: float = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        num_workers: int = 2
    ) -> "dict[str, dd.DataFrame]":

        if streams is not None and len(streams) > 0:
            usesTokens = False
            metadata = _get_metadata(self.__sedaro, sim_id := job['dataArray'])
            filtered_streams = _get_filtered_streams(streams, metadata)
            num_workers = min(num_workers, len(filtered_streams))
            workers = [[] for _ in range(num_workers)]
            for i, stream in enumerate(filtered_streams):
                workers[i % num_workers].append(stream)
        else:
            usesTokens = True
            if num_workers > 1:
                metadata = _get_metadata(self.__sedaro, sim_id := job['dataArray'], num_workers)
                try:
                    filtered_streams = metadata['streamsTokens']
                except KeyError:
                    raise Exception(
                        f"No series data found for simulation {sim_id}. This indicates that the simulation has just started running. Please try again after a short wait.")
                # len(filtered_streams) may be less than num_workers if there are fewer streams than that number
                num_workers = len(filtered_streams)
                workers = filtered_streams
            else:
                metadata = _get_metadata(self.__sedaro, sim_id := job['dataArray'])

        download_bar = ProgressBar(
            metadata['start'],
            metadata['stop'],
            len(metadata['streams'] if 'streams' in metadata else metadata['streamsTokens']),
            "Downloading..."
        )
        download_managers = [DownloadWorker(download_bar) for _ in range(num_workers)]
        params = {'start': start, 'stop': stop, 'sampleRate': sampleRate}
        if num_workers > 1:
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                exceptions = executor.map(
                    self.__downloadInParallel, [sim_id] * num_workers, workers,
                    [params] * num_workers, download_managers, [usesTokens] * num_workers
                )
                executor.shutdown(wait=True)
            for e in exceptions:
                if e is not None:
                    raise e
        else:
            self.__downloadInParallel(sim_id, None, params, download_managers[0], usesTokens)
        download_bar.complete()

        stream_results = {}
        for download_manager in download_managers:
            stream_results.update(download_manager.streams)
        return {
            'meta': download_managers[0].finalize_metadata(download_managers[1:]),
            'stats': download_managers[0].finalize_stats(download_managers[1:]),
            'series': stream_results,
        }

    def results(
        self,
        job_id: str = None,
        start: float = None,
        stop: float = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        num_workers: int = 2,
    ) -> SimulationResult:
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
            start (float, optional): Start time of the data to fetch. Defaults to `None`, which means the start of the sim.
            stop (float, optional): End time of the data to fetch. Defaults to `None`, which means the end of the sim.
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.
            sampleRate (int, optional): the resolution at which to fetch the data. Must be a positive integer power of two, or 0.\
                The value n provided, if not 0, corresponds to data at 1/n resolution. For instance, 1 means data is fetched at\
                full resolution, 2 means every second data point is fetched, 4 means every fourth data point is fetched, and so on.\
                If the value provided is 0, data is fetched at the lowest resolution available. If no argument is provided, data\
                is fetched at full resolution (sampleRate 1).
            num_workers (int, optional): Number of parallel workers to use for downloading data. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        '''Query latest scenario result.'''
        job = self.status(job_id)
        data = self.__results(
            job, start=start, stop=stop, streams=streams, sampleRate=sampleRate, num_workers=num_workers
        )
        return SimulationResult(job, data, self.__sedaro)

    def results_poll(
        self,
        job_id: str = None,
        start: float = None,
        stop: float = None,
        streams: List[Tuple[str, ...]] = None,
        sampleRate: int = None,
        num_workers: int = 2,
        retry_interval: int = 2,
        timeout: int = None,
        wait_on_stats: bool = False,
    ) -> SimulationResult:
        """Query latest scenario result and wait for sim to finish if it's running. If a `job_id` is passed, query for
        corresponding sim results rather than latest. See `results` method for details on using the `streams` kwarg.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            start (float, optional): Start time of the data to fetch. Defaults to `None`, which means the start of the sim.
            stop (float, optional): End time of the data to fetch. Defaults to `None`, which means the end of the sim.
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`. See `results` method for details.
            sampleRate (int, optional): the resolution at which to fetch the data. Must be a positive integer power of two, or 0.\
                The value n provided, if not 0, corresponds to data at 1/n resolution. For instance, 1 means data is fetched at\
                full resolution, 2 means every second data point is fetched, 4 means every fourth data point is fetched, and so on.\
                If the value provided is 0, data is fetched at the lowest resolution available. If no argument is provided, data\
                is fetched at full resolution (sampleRate 1).
            num_workers (int, optional): Number of parallel workers to use for downloading data. Defaults to `2`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.
            wait_on_stats (bool, optional): Wait not just until the sim is done, but also until the stats are available, and then\
                fetch the stats alongside the results. Defaults to `False`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        job = self.status(job_id)
        options = PRE_RUN_STATUSES | {RUNNING}
        start_time = time.time()

        while job[STATUS] in options and (not timeout or time.time() - start_time < timeout):
            if job[STATUS] == QUEUED:
                print('Simulation is queued...', end='\r')
            elif job[STATUS] in PRE_RUN_STATUSES:
                print('Simulation is building...', end='\r')
            else:
                progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        data = self.__results(
            job, start=start, stop=stop, streams=streams, sampleRate=sampleRate, num_workers=num_workers
        )
        if wait_on_stats and not data['stats']:
            success = False
            while not success:
                result, success = _get_stats_for_sim_id(self.__sedaro, job['dataArray'], streams=streams)
                if success:
                    data['stats'] = result
                    break
                time.sleep(retry_interval)
        return SimulationResult(job, data, self.__sedaro)

    def poll(
        self,
        job_id: str = None,
        retry_interval: int = 2,
        timeout: int = None,
    ) -> str:
        """
        Wait for sim to finish if it's running. If a `job_id` is passed, query for corresponding sim rather than latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            str: the ultimate status of the simulation.
        """
        job = self.status(job_id)
        options = PRE_RUN_STATUSES | {RUNNING}
        start_time = time.time()

        while job[STATUS] in options and (not timeout or time.time() - start_time < timeout):
            if job[STATUS] == QUEUED:
                print('Simulation is queued...', end='\r')
            elif job[STATUS] in PRE_RUN_STATUSES:
                print('Simulation is building...', end='\r')
            else:
                progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        return job[STATUS]

    def stats(self, job_id: str = None, streams: List[Tuple[str, ...]] = None, wait: bool = False) -> dict:
        """Query latest scenario stats. If a `job_id` is passed, query for corresponding sim stats rather than latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch stats. Defaults to `None`.
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`.
            wait (bool, optional): If `True`, wait for stats to be available. If `False`, raise
                an exception if stats are not available. Defaults to `False`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: a dictionary of stats for the sim.
        """
        job = self.status(job_id)
        result, success = _get_stats_for_sim_id(self.__sedaro, job['dataArray'], streams=streams)
        if success:
            return result
        else:
            if wait:
                retry_interval = 2
                while not success:
                    result, success = _get_stats_for_sim_id(self.__sedaro, job['dataArray'], streams=streams)
                    if success:
                        return result
                    time.sleep(retry_interval)
            else:
                raise NoSimResultsError(reason=
                    'No stats available for simulation. Simulation may not have completed yet, or the simulation has completed but stats are still in progress.'
                )

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
    def __enter__(self): return self
    def __exit__(self, *args): 
        try:
            self.terminate()
        except:
            pass

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

    def results(
        self,
        start: float = None,
        stop: float = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        num_workers: int = 2,
    ) -> SimulationResult:
        """Query simulation results.

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
            start (float, optional): Start time of the data to fetch. Defaults to `None`, which means the start of the sim.
            stop (float, optional): End time of the data to fetch. Defaults to `None`, which means the end of the sim.
            streams (Optional[List[Tuple[str, ...]]], optional): Streams to query for. Defaults to `None`.
            sampleRate (int, optional): the resolution at which to fetch the data. Must be a positive integer power of two, or 0.\
                The value n provided, if not 0, corresponds to data at 1/n resolution. For instance, 1 means data is fetched at\
                full resolution, 2 means every second data point is fetched, 4 means every fourth data point is fetched, and so on.\
                If the value provided is 0, data is fetched at the lowest resolution available. If no argument is provided, data\
                is fetched at full resolution (sampleRate 1).
            num_workers (int, optional): Number of parallel workers to use for downloading data. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.
            SedaroApiException: if no simulation has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results(job_id=self.__job['id'], start=start, stop=stop, streams=streams, sampleRate=sampleRate, num_workers=num_workers)

    def results_poll(
        self,
        start: float = None,
        stop: float = None,
        streams: List[Tuple[str, ...]] = None,
        sampleRate: int = None,
        num_workers: int = 2,
        retry_interval: int = 2,
        timeout: int = None,
        wait_on_stats: bool = False,
    ) -> SimulationResult:
        """Query simulation results but wait for sim to finish if it's running. See `results` method for details on using the `streams` kwarg.

        Args:
            start (float, optional): Start time of the data to fetch. Defaults to `None`, which means the start of the sim.
            stop (float, optional): End time of the data to fetch. Defaults to `None`, which means the end of the sim.
            streams (List[Tuple[str, ...]], optional): Streams to query for. Defaults to `None`. See `results` method for details.
            sampleRate (int, optional): the resolution at which to fetch the data. Must be a positive integer power of two, or 0.\
                The value n provided, if not 0, corresponds to data at 1/n resolution. For instance, 1 means data is fetched at\
                full resolution, 2 means every second data point is fetched, 4 means every fourth data point is fetched, and so on.\
                If the value provided is 0, data is fetched at the lowest resolution available. If no argument is provided, data\
                is fetched at full resolution (sampleRate 1).
            num_workers (int, optional): Number of parallel workers to use for downloading data. Defaults to `2`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.
            wait_on_stats (bool, optional): Wait not just until the sim is done, but also until the stats are available, and then\
                fetch the stats alongside the results. Defaults to `False`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        return self.__sim_client.results_poll(
            job_id=self.__job['id'],
            start=start,
            stop=stop,
            streams=streams,
            sampleRate=sampleRate,
            num_workers=num_workers,
            retry_interval=retry_interval,
            timeout=timeout,
            wait_on_stats=wait_on_stats,
        )

    def poll(
        self,
        retry_interval: int = 2,
        timeout: int = None,
    ) -> str:
        """
        Wait for sim to finish if it's running. If a `job_id` is passed, query for corresponding sim rather than latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            str: the ultimate status of the simulation.
        """
        return self.__sim_client.poll(job_id=self.__job['id'], retry_interval=retry_interval, timeout=timeout)
 
    def stats(self, job_id: str = None, streams: List[Tuple[str, ...]] = None, wait: bool = False) -> dict:
        return self.__sim_client.stats(job_id=job_id or self.__job['id'], streams=streams, wait=wait)

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
