import json
from contextlib import contextmanager
from typing import Any, Dict, Generator, List, Optional, Tuple

from sedaro_2.raw_request import RawRequest
from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from .branch_clients import AgentTemplateBranch, BranchClient, ScenarioBranch
from .exceptions import SedaroApiException
from .settings import COMMON_API_KWARGS
from .sim_client import SimClient
from .utils import body_from_res, parse_urllib_response


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(self, api_key, host='https://api.sedaro.com'):
        self._api_key = api_key
        self._api_host = host

        # FIXME: remove this init when can
        return super().__init__(
            configuration=Configuration(host=host),
            header_name='X_API_KEY',
            header_value=api_key
        )

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

    # FIXME: delete this method
    def get_branch(self, id: int) -> BranchClient:
        """Gets a Sedaro Branch based on the given `id` and creates a `BranchClient` from the response. The branch must
        be accessible to this `SedaroApiClient` via the `api_key`.

        Args:
            id (int): the id of the desired Sedaro Branch

        Returns:
            BranchClient: A `BranchClient` object used to interact with the data attached to the corresponding Sedaro
            Branch.
        """
        branches_api_instance = branches_api.BranchesApi(self)
        # res = branches_api_instance.get_branch(path_params={'branchId': id}) # TODO: temp_crud
        # return BranchClient(res.body, self)
        res = branches_api_instance.get_branch(
            path_params={'branchId': id}, **COMMON_API_KWARGS)
        return BranchClient(body_from_res(res), self)

    def get_data(self,
                 id,
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
        response = self.call_api(url, 'GET')
        _response = None
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if _response and 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        return _response

    def get_sim_client(self, branch_id: int):
        """Creates and returns a Sedaro SimClient

        Args:
            branch_id (int): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs)

        Returns:
            SimClient: a Sedaro SimClient
        """
        return SimClient(self, branch_id)

    @property
    def request(self):
        return RawRequest(self)
