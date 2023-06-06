import time
from contextlib import contextmanager
from typing import (TYPE_CHECKING, Any, Dict, Generator, List, Optional, Tuple,
                    Union)

from sedaro_base_client.api_client import ApiResponse
from sedaro_base_client.apis.tags import jobs_api

from .exceptions import NoSimResultsError, SedaroApiException
from .results import SimulationResult
from .settings import COMMON_API_KWARGS
from .utils import body_from_res, parse_urllib_response, progress_bar

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class SimClient:
    """A client to interact with the Sedaro API simulation (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch_id: int):
        """Instantiate a Sedaro SimClient

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

    def start(self) -> ApiResponse:
        """Starts simulation corresponding to the Sedaro Scenario Branch id that this `SimClient` was instantiated with.

        Returns:
            ApiResponse: response from the start simulation (job) request
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_simulation(
                path_params={'branchId': self.__branch_id},
                **COMMON_API_KWARGS
            )
        return body_from_res(res)

    def latest_raw(self, *, err_if_empty: bool = False) -> Union[Dict, None]:
        """Gets the latest simulation (job) corresponding to the Sedaro Scenario Branch id that this `SimClient` was
        instantiated with. This can return a response even before the simulation is done.

        Args:
            err_if_empty (bool, optional): Triggers raising an error if no simulation results and `err_if_empty`.\
                Defaults to `False`.

        Raises:
            NoSimResultsError: if no simulation results and `err_if_empty`

        Returns:
            Union[Dict, None]: dictionary from response body from the get latest simulation (job) request, otherwise\
                `None` if there is no latest simulation.
        """
        with self.__jobs_client() as jobs:
            res = jobs.get_simulations(
                path_params={'branchId': self.__branch_id},
                query_params={'latest': ''},
                **COMMON_API_KWARGS
            )
        if len(body := body_from_res(res)):
            return body[0]
        if err_if_empty:
            raise NoSimResultsError(
                status=404,
                reason=f'Could not find any simulation results for scenario: {self.__branch_id}'
            )
        return None

    def terminate(self, job_id: int = None, latest: bool = False) -> ApiResponse:
        """Terminate simulation corresponding to the Sedaro Scenario Branch id that this `SimClient` was instantiated
        with and the passed in `job_id`.

        Args:
            job_id (`int`, optional): id of the simulation (job) to termiante.
            latest (`bool`, optional): indicates terminating the latest running job.

        Returns:
            ApiResponse: response from the termiante simulation (job) request
        """
        if job_id is not None and latest:
            raise ValueError('Cannot set both "job_id" and "latest".')

        if latest:
            job_id = self.latest_raw(err_if_empty=True)['id']

        with self.__jobs_client() as jobs:

            res = jobs.terminate_simulation(
                path_params={
                    'branchId': self.__branch_id,
                    'jobId': job_id
                },
                **COMMON_API_KWARGS
            )
        return body_from_res(res)

    def __get_data(
        self,
        id: str,
        start: float = None,
        stop: float = None,
        binWidth: float = None,
        limit: float = None,
        axisOrder: str = None,
        streams: Optional[List[Tuple[str, ...]]] = None
    ):
        """Simplified Data Service getter with significantly higher performance over the Swagger-generated client."""
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
        _response = None
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        return _response

    def latest(self, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
        '''Query latest scenario result.'''
        latest = self.latest_raw(err_if_empty=True)
        data = self.__get_data(latest['dataArray'], streams=streams or [])
        return SimulationResult(latest, data)
