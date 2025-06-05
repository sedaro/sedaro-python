import asyncio
import logging
import math
import signal
import sys
import threading
import time
import traceback
from concurrent.futures import ThreadPoolExecutor
from contextlib import asynccontextmanager, contextmanager
from typing import TYPE_CHECKING, Any, Generator, List, Optional, Tuple, Union

from sedaro_base_client.apis.tags import externals_api, jobs_api

from sedaro.branches.scenario_branch.download import DownloadWorker, ProgressBar
from sedaro.grpc_client import CosimClient
from sedaro.results.simulation_result import SimulationResult

from ...exceptions import NoSimResultsError, SedaroApiException, SimInitializationError
from ...settings import BAD_STATUSES, COMMON_API_KWARGS, PRE_RUN_STATUSES, QUEUED, RUNNING, STATUS
from ...utils import body_from_res, progress_bar, serdes
from .utils import FastFetcher, _get_filtered_streams, _get_metadata, _get_stats_for_sim_id

if TYPE_CHECKING:
    import dask.dataframe as dd

    from ...branches import ScenarioBranch
    from ...sedaro_api_client import SedaroApiClient


def dump_tracebacks(signalnum=None, frame=None):
    """Prints full detailed stack traces of all running threads, including source code lines."""
    print("\n=== Dumping all thread tracebacks ===", file=sys.stderr)

    for thread in threading.enumerate():
        print(f"\n--- Thread {thread.name} (ID: {thread.ident}) ---", file=sys.stderr)
        stack = traceback.format_stack(sys._current_frames().get(thread.ident, None))
        if stack:
            print("".join(stack), file=sys.stderr)
        else:
            print("No stack trace available.", file=sys.stderr)

    sys.exit(1)  # Ensure program exits after traceback dump


# Register SIGINT handler (used to get tracebacks from inside ThreadPoolExecutor threads on KeyboardInterrupt)
signal.signal(signal.SIGINT, dump_tracebacks)

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

    def get_sedaro(self):
        return self.__sedaro

    def start(
        self,
        wait=False,
        timeout=None,
        label=None,
        capacity=None,
        seed=None,
        verbose=False,
        **kwargs,
    ) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Args:
            wait (bool, optional): Triggers waiting for simulation to deploy and transition to `RUNNING` before returning. Defaults to `False`.
            timeout (int, optional): Seconds to wait for simulation to deploy and transition to `RUNNING` before raising an error. Defaults to `None`.
            label (str, optional): A label to assign to the simulation job. Defaults to `None`.
            capacity (int, optional): The capacity to allocate to the simulation. Defaults to using the lesser of the Workspace capacity and the number of Agents in the Scenario.
            seed (int, optional): The pseudorandom seed to use for the simulation. Defaults to the Simulation Service's default.
            verbose (bool, optional): If `True`, periodically print the sim's status to the console while waiting for it to start. Defaults to `False`.
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
                if verbose and math.isclose(t % 10.0, 0.0, abs_tol=0.01):
                    print(f'Current simulation status: {handle[STATUS]}')
            elif handle[STATUS] in BAD_STATUSES:
                raise SimInitializationError(handle['message'])
            else:
                return handle
        raise TimeoutError(
            f'Simulation did not deploy before timeout of {timeout}.')

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

    def dmlog(self, download_manager: Optional[DownloadWorker], msg):
        if download_manager is not None:
            download_manager.log(msg)

    def __fetch(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        streams: Optional[List[Tuple[str, ...]]] = None,
        sampleRate: int = None,
        continuationToken: str = None,
        usesStreamTokens: bool = False,
        download_manager: DownloadWorker = None,
    ):
        self.dmlog(download_manager, f"Starting __fetch. Streams: {streams} (is token ID? {usesStreamTokens})")

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

        def get_and_parse_page_with_retry(
            fetcher: FastFetcher,
            request_url: str,
            download_manager: DownloadWorker,
            max_retries: int = 5,
        ):
            for attempt in range(max_retries):
                self.dmlog(download_manager, f"Calling URL: {request_url}")
                raw_response = fetcher.get(request_url)
                if raw_response.status == 500:
                    # retry on 500 error
                    self.dmlog(download_manager,
                        f"Attempt #{attempt+1}/{max_retries}: received 500 error from {request_url}. Retrying...")
                    time.sleep(1.5 ** attempt)
                    continue
                elif raw_response.status != 200:
                    error_response = raw_response.parse()
                    # raise an exception for any other error
                    raise SedaroApiException(
                        status=raw_response.status,
                        reason=error_response['error']['message'] if 'error' in error_response else 'An unknown error occurred.'
                    )
                self.dmlog(download_manager,
                    f"Got response from {request_url} -- status: {raw_response.status}. Parsing response...")
                parsed_response = raw_response.parse()
                self.dmlog(download_manager, f"Parsed response from {request_url}")
                return parsed_response
            raise SedaroApiException(
                status=500,
                reason=f"Failed to successfully fetch data at {request_url} after {max_retries} attempts."
            )

        def process_parsed_page(parsed_page: dict, download_manager: DownloadWorker):
            download_manager.update_metadata(parsed_page['meta'])
            download_manager.ingest(parsed_page['series'])
            if 'stats' in parsed_page:
                download_manager.update_stats(parsed_page['stats'])
            if 'derived' in parsed_page:
                if 'series' in parsed_page['derived']:
                    download_manager.ingest_derived(parsed_page['derived']['series'])
                if 'static' in parsed_page['derived']:
                    download_manager.update_static_data(parsed_page['derived']['static'])
            if 'continuationToken' in parsed_page['meta'] and parsed_page['meta']['continuationToken'] is not None:
                return parsed_page['meta']['continuationToken']
            else:
                return None

        # fetch one page of data at a time, until end, and process data as it comes in
        is_first_page = True
        ctoken = None
        while is_first_page or ctoken is not None:
            if ctoken is not None:
                url = f'/data/{id}?&continuationToken={ctoken}'
            page = get_and_parse_page_with_retry(fast_fetcher, url, download_manager)
            ctoken = process_parsed_page(page, download_manager)
            is_first_page = False

    def __downloadInParallel(self, sim_id, streams, params, download_manager: DownloadWorker, usesStreamTokens):
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
            import traceback
            download_manager.log(f"Worker failed: {traceback.format_exc()})")
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
            len(metadata['streams']
                if 'streams' in metadata else metadata['streamsTokens']),
            "Downloading..."
        )
        download_managers = [DownloadWorker(
            download_bar, i + 1) for i in range(num_workers)]
        params = {'start': start, 'stop': stop, 'sampleRate': sampleRate}
        if num_workers > 1:
            with ThreadPoolExecutor(max_workers=num_workers) as executor:
                try:
                    exceptions = executor.map(
                        self.__downloadInParallel, [sim_id] * num_workers, workers,
                        [params] * num_workers, download_managers, [usesTokens] * num_workers
                    )
                    executor.shutdown(wait=True)
                except KeyboardInterrupt:
                    print(f"Ctrl-C detected. Shutting down workers...", file=sys.stderr)
                    executor.shutdown(wait=False)
                    dump_tracebacks(signal.SIGINT, None)
            for e in exceptions:
                if e is not None:
                    raise e
        else:
            self.__downloadInParallel(sim_id, filtered_streams, params, download_managers[0], usesTokens)
        download_bar.complete()
        print("Processing downloaded data...")
        for download_manager in download_managers:
            download_manager.finalize()

        stream_results = {}
        for download_manager in download_managers:
            stream_results.update(download_manager.streams)
        result = {
            'meta': download_managers[0].finalize_metadata(download_managers[1:]),
            'stats': download_managers[0].finalize_stats(download_managers[1:]),
            'static': download_managers[0].finalize_static_data(download_managers[1:]),
            'series': stream_results,
        }
        return result

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
        job = self.poll(job_id=job_id, retry_interval=retry_interval, timeout=timeout)

        data = self.__results(
            job, start=start, stop=stop, streams=streams, sampleRate=sampleRate, num_workers=num_workers
        )
        if wait_on_stats and not data['stats']:
            success = False
            while not success:
                result, success = _get_stats_for_sim_id(
                    self.__sedaro, job['dataArray'], streams=streams)
                if success:
                    data['stats'] = result
                    break
                time.sleep(retry_interval)
        return SimulationResult(job, data, self.__sedaro)

    async def results_poll_async(
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
        """Asynchronously query latest scenario result and wait for sim to finish if it's running. If a `job_id` is 
        passed, query for corresponding sim results rather than latest. See `results` method for details on using the 
        `streams` kwarg.

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
        await self.poll_async(job_id=job_id, retry_interval=retry_interval, timeout=timeout)

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
                await asyncio.sleep(retry_interval)
        return SimulationResult(job, data, self.__sedaro)

    def poll(
        self,
        job_id: str = None,
        retry_interval: int = 2,
        timeout: int = None,
    ) -> 'SimulationHandle':
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

        return job

    async def poll_async(
        self,
        job_id: str = None,
        timeout: int = None,
        retry_interval: int = 2,
    ) -> str:
        """
        Asynchronously wait for sim to finish if it's running. If a `job_id` is passed, query for corresponding sim 
        rather than latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

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
            await asyncio.sleep(retry_interval)

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
        result, success = _get_stats_for_sim_id(
            self.__sedaro, job['dataArray'], streams=streams)
        if success:
            return result
        else:
            if wait:
                retry_interval = 2
                while not success:
                    result, success = _get_stats_for_sim_id(
                        self.__sedaro, job['dataArray'], streams=streams)
                    if success:
                        return result
                    time.sleep(retry_interval)
            else:
                raise NoSimResultsError(reason='No stats available for simulation. Simulation may not have completed yet, or the simulation has completed but stats are still in progress.'
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
        self._job = SimulationJob(job)
        self._sim_client = sim_client

    def __getitem__(self, key): return self._job[key]
    def get(self, key, default=None): return self._job.get(key, default)
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
        return (self := self._sim_client.status(self._job['id'], err_if_empty=err_if_empty))

    def terminate(self):
        """Terminate the running simulation.

        Returns:
            SimulationHandle (self)
        """
        self._sim_client.terminate(self._job['id'])
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
        return self._sim_client.results(job_id=self._job['id'], start=start, stop=stop, streams=streams, sampleRate=sampleRate, num_workers=num_workers)

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
        return self._sim_client.results_poll(
            job_id=self._job['id'],
            start=start,
            stop=stop,
            streams=streams,
            sampleRate=sampleRate,
            num_workers=num_workers,
            retry_interval=retry_interval,
            timeout=timeout,
            wait_on_stats=wait_on_stats,
        )

    async def results_poll_async(
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
        """Asynchronously query simulation results but wait for sim to finish if it's running. See `results` method for
        details on using the `streams` kwarg.

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
        return await self._sim_client.results_poll_async(
            job_id=self._job['id'],
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
    ) -> 'SimulationHandle':
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
        return self._sim_client.poll(job_id=self._job['id'], retry_interval=retry_interval, timeout=timeout)

    async def poll_async(
        self,
        timeout: int = None,
        retry_interval: int = 2,
    ) -> str:
        """
        Asynchronously wait for sim to finish if it's running. If a `job_id` is passed, query for corresponding sim 
        rather than latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            timeout (int, optional): Maximum time to wait for the simulation to finish. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            str: the ultimate status of the simulation.
        """
        return await self._sim_client.poll_async(job_id=self._job['id'], retry_interval=retry_interval, timeout=timeout)

    def stats(self, job_id: str = None, streams: List[Tuple[str, ...]] = None, wait: bool = False) -> dict:
        return self._sim_client.stats(job_id=job_id or self._job['id'], streams=streams, wait=wait)

    def consume(self, agent_id: str, external_state_id: str, time: float = None):
        with self._sim_client.externals_client() as externals_client:
            response = externals_client.get_external(
                path_params={
                    'jobId': self._job['id'],
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
        with self._sim_client.externals_client() as externals_client:
            response = externals_client.put_external(
                path_params={
                    'jobId': self._job['id'],
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

    @asynccontextmanager
    async def async_channel(self, grpc_host: str = None, insecure=False):
        """
        Asynchronous context manager for cosimulation sessions.
        Automatically opens a cosimulation grpc session on entry and closes it on exit.

        Usage:
            async with simulation_handle.async_channel(grpc_host="...") as cosim_client:
                # ...
        """
        sedaro = self._sim_client.get_sedaro()
        host = sedaro._api_host
        grpc_host = grpc_host or sedaro._grpc_host

        status = self._sim_client.status(job_id=self._job['id'])
        address = status.get("clusterAddr")
        job_id = status.get("id")

        cosim_client = CosimClient(
            grpc_host=grpc_host,
            address=address,
            job_id=job_id,
            host=host,
            insecure=insecure,
            sedaro=sedaro,
        )

        try:
            async with cosim_client:
                yield cosim_client
        except Exception as e:
            logging.error(f"Cosimulation session encountered an error: {e}")
            raise e
