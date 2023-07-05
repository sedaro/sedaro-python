import time
from contextlib import contextmanager
from typing import (TYPE_CHECKING, Any, Dict, Generator, List, Optional, Tuple,
                    Union)

from sedaro_base_client.apis.tags import jobs_api
from sedaro_base_client.apis.tags import externals_api

from ...exceptions import NoSimResultsError, SedaroApiException
from ...results import SimulationResult
from ...settings import COMMON_API_KWARGS
from ...utils import body_from_res, parse_urllib_response, progress_bar

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient


def handle_response(response):
    _response = None
    try:
        _response = parse_urllib_response(response)
        if response.status != 200:
            raise Exception()
    except:
        reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
        raise SedaroApiException(status=response.status, reason=reason)
    return _response


class Simulation:
    """A client to interact with the Sedaro API simulation (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch_id: int):
        """Instantiate a Sedaro `Simulation` instance

        Args:
            sedaro (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self.__branch_id = branch_id
        self.__sedaro = sedaro

    @contextmanager
    def __jobs_client(self) -> Generator['jobs_api.JobsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield jobs_api.JobsApi(api)

    @contextmanager
    def __externals_client(self) -> Generator['externals_api.ExternalsApi', Any, None]:
        with self.__sedaro.api_client() as api:
            yield externals_api.ExternalsApi(api)

    def start(self) -> 'SimulationHandle':
        """Starts simulation corresponding to the respective Sedaro Scenario Branch id.

        Returns:
            SimulationHandle
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        return SimulationHandle(body_from_res(res), self)

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

    def terminate(self, job_id: int = None) -> 'SimulationHandle':
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
        return SimulationHandle(None, self)

    def results_plain(
        self,
        *,
        id: str = None,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None
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
                format described in the previous section. If no list is provided, data is fetched for all streams.

            axisOrder (enum, optional): the shape of each series in the response. Options: `'TIME_MAJOR'` and\
                `'TIME_MINOR'`. Default value, if not specified, is `'TIME_MAJOR'`.

        Raises:
            NoSimResultsError: if no simulation has been started.

        Returns:
            dict: response from the `get` request
        """
        if id == None:
            id = self.status()['dataArray']
        url = f'/data/{id}?'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            url += f'&binWidth={binWidth}'
        elif limit is not None:
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
        with self.__sedaro.api_client() as api:
            response = api.call_api(url, 'GET')
        return handle_response(response)

    def results(self, job_id: str = None, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
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
        data = self.results_plain(id=job['dataArray'], streams=streams or [])
        return SimulationResult(job, data)

    def results_poll(
        self,
        job_id: str = None,
        streams: List[Tuple[str, ...]] = None,
        retry_interval: int = 2
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
        options = {'PENDING', 'RUNNING'}

        while job['status'] in options:
            progress_bar(job['progress']['percentComplete'])
            job = self.status()
            time.sleep(retry_interval)

        return self.results(streams=streams or [])


class SimulationJob:
    def __init__(self, job: Union[dict, None]): self.__job = job

    def __getitems__(self, key):
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

    def __getitems__(self, key): return self.__job[key]

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
        self.__job = self.__sim_client.status(
            self.__job['id'], err_if_empty=err_if_empty)
        return self

    def terminate(self):
        """Terminate the running simulation.

        Returns:
            SimulationHandle (self)
        """
        self.__sim_client.terminate(self.__job['id'])
        self.__job = SimulationJob(None)
        return self

    def results_plain(
        self,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None
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
            streams=streams
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

    def consume(self, agent_id: str, external_state_id: str, time: float = None):
        with self.__sim_client.__externals_client() as externals_client:
            response = externals_client.get_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                query_params=({'time': time} if time is not None else {}),
            )
        return handle_response(response)

    def produce(self, agent_id: str, external_state_id: str, values: Union[list, tuple], timestamp: float = None):
        with self.__sim_client.__externals_client() as externals_client:
            response = externals_client.put_external(
                path_params={
                    'jobId': self.__job['id'],
                    'agentId': agent_id,
                    'externalStateBlockId': external_state_id,
                },
                body=(
                    {'values': [*values]} |
                    ({'timestamp': timestamp} if timestamp is not None else {})
                ),
            )
        return handle_response(response)
