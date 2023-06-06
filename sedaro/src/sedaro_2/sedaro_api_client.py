from contextlib import contextmanager
from typing import Any, Dict, Generator

from sedaro_2.raw_request import RawRequest
from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from .branch_clients import AgentTemplateBranch, ScenarioBranch
from .settings import COMMON_API_KWARGS
from .utils import body_from_res


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(self, api_key, host='https://api.sedaro.com'):
        self._api_key = api_key
        self._api_host = host

    @contextmanager
    def api_client(self) -> Generator[ApiClient, Any, None]:
        """Instantiate ApiClient from sedaro_base_client

        Yields:
            Generator[ApiClient, Any, None]: ApiClient
        """
        with ApiClient(
            configuration=Configuration(host=self._api_host),
            header_name='X_API_KEY',
            header_value=self._api_key
        ) as api:
            yield api

    def __get_branch(self, branch_id: str) -> Dict:
        """Get Sedaro `Branch` with given `branch_id` from `host`

        Args:
            branch_id (str): `id` of the Sedaro `Branch` to get

        Returns:
            Dict: `body` of the response as a `dict`
        """
        with self.api_client() as api:
            branches_api_instance = branches_api.BranchesApi(api)
            # res = branches_api_instance.get_branch(path_params={'branchId': id}) # TODO: temp_crud
            # return BranchClient(res.body, self)
            res = branches_api_instance.get_branch(
                path_params={'branchId': branch_id}, **COMMON_API_KWARGS)
            return body_from_res(res)

    def agent_template_branch(self, branch_id: str) -> AgentTemplateBranch:
        """Instantiate an `AgentTemplateBranch` client associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            AgentTemplateBranch: `AgentTemplateBranch` client
        """
        return AgentTemplateBranch(self.__get_branch(branch_id), self)

    def scenario_branch(self, branch_id: str) -> ScenarioBranch:
        """Instantiate an `ScenarioBranch` client associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            ScenarioBranch: `ScenarioBranch` client
        """
        return ScenarioBranch(self.__get_branch(branch_id), self)

    @property
    def request(self):
        """API for sending raw `get`, `post`, `put`, `patch`, and `delete` requests to the configured Sedaro host."""
        return RawRequest(self)
