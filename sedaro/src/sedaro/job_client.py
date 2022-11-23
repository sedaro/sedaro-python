from typing import TYPE_CHECKING

from sedaro_base_client.apis.tags import jobs_api
from sedaro_base_client.api_client import ApiResponse

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class JobClient(jobs_api.JobsApi):
    """A client to interact with the Sedaro API jobs routes"""
    branch_id: int

    def __init__(self, sedaro_api_client: 'SedaroApiClient', branch_id: int):
        """Instantiate a Sedaro JobClient

        Args:
            sedaro_api_client (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations/jobs.
        """
        super().__init__(sedaro_api_client)
        self.branch_Id = branch_id

    def start_simulation(self) -> ApiResponse:
        """Starts simulation corresponding to the Sedaro Scenario Branch id that this `JobClient` was instantiated with.

        Returns:
            ApiResponse: response from the start simulation request
        """
        return super().start_simulation(
            path_params={'branchId': self.branch_Id}
        )

    def get_latest_simulation(self) -> ApiResponse:
        """Gets the latest running simulation corresponding to the Sedaro Scenario Branch id that this `JobClient` was
        instantiated with.

        Returns:
            ApiResponse: response from the get job request
        """
        return super().get_simulations(
            path_params={'branchId': self.branch_Id},
            query_params={'latest': ''}
        )

    def terminate_simulation(self, job_id: int) -> ApiResponse:
        """Terminate simulation corresponding to the Sedaro Scenario Branch id that this `JobClient` was instantiated
        with and the passed in `job_id`.

        Args:
            job_id (`int`): id of the job to termiante.

        Returns:
            ApiResponse: response from the termiante job request
        """
        return super().terminate_simulation(
            path_params={
                'branchId': self.branch_Id,
                'jobId': job_id
            }
        )
