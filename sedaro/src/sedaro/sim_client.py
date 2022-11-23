from typing import TYPE_CHECKING

from sedaro_base_client.apis.tags import jobs_api
from sedaro_base_client.api_client import ApiResponse

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class SimClient:
    """A client to interact with the Sedaro API simulation (jobs) routes"""
    branch_id: int
    _base_jobs_api_client: jobs_api.JobsApi

    def __init__(self, sedaro_api_client: 'SedaroApiClient', branch_id: int):
        """Instantiate a Sedaro SimClient

        Args:
            sedaro_api_client (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self._base_jobs_api_client = jobs_api.JobsApi(sedaro_api_client)
        self.branch_Id = branch_id

    def start(self) -> ApiResponse:
        """Starts simulation corresponding to the Sedaro Scenario Branch id that this `SimClient` was instantiated with.

        Returns:
            ApiResponse: response from the start simulation (job) request
        """
        return self._base_jobs_api_client.start_simulation(
            path_params={'branchId': self.branch_Id}
        )

    def get_latest(self) -> ApiResponse:
        """Gets the latest running simulation (job) corresponding to the Sedaro Scenario Branch id that this `SimClient`
        was instantiated with.

        Returns:
            ApiResponse: response from the get simulation (job) request
        """
        return self._base_jobs_api_client.get_simulations(
            path_params={'branchId': self.branch_Id},
            query_params={'latest': ''}
        )

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
        return self._base_jobs_api_client.terminate_simulation(
            path_params={
                'branchId': self.branch_Id,
                'jobId': job_id
            }
        )
