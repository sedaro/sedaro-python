from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Generator

from sedaro_base_client.api_client import ApiResponse
from sedaro_base_client.apis.tags import jobs_api

from .settings import COMMON_API_KWARGS
from .utils import body_from_res

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
        self.branch_Id = branch_id
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
                path_params={'branchId': self.branch_Id},
                **COMMON_API_KWARGS
            )
        return body_from_res(res)

    def get_latest(self) -> ApiResponse:
        """Gets the latest running simulation (job) corresponding to the Sedaro Scenario Branch id that this `SimClient`
        was instantiated with.

        Returns:
            ApiResponse: response from the get simulation (job) request
        """
        with self.__jobs_client() as jobs:
            res = jobs.get_simulations(
                path_params={'branchId': self.branch_Id},
                query_params={'latest': ''},
                **COMMON_API_KWARGS
            )
        return body_from_res(res)

    def terminate(self, job_id: int) -> ApiResponse:
        """Terminate simulation corresponding to the Sedaro Scenario Branch id that this `SimClient` was instantiated
        with and the passed in `job_id`.

        Note: the `job_id` of the "latest" running simulation can be retrieved via:

        ```py
            res = sim_client.get_latest()
            job_id = res.body[0]['id']
            sim_client.terminate(job_id)
        ```

        Args:
            job_id (`int`): id of the simulation (job) to termiante.

        Returns:
            ApiResponse: response from the termiante simulation (job) request
        """
        with self.__jobs_client() as jobs:

            res = jobs.terminate_simulation(
                path_params={
                    'branchId': self.branch_Id,
                    'jobId': job_id
                },
                **COMMON_API_KWARGS
            )
        return body_from_res(res)
