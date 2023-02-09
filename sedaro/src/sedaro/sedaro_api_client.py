import json
from typing import Optional, Dict

from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from .utils import parse_urllib_response
from .branch_client import BranchClient
from .exceptions import SedaroApiException
from .sim_client import SimClient
from .settings import COMMON_API_KWARGS


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(self, api_key, host='https://api.sedaro.com', *args, **kwargs):
        return super().__init__(
            configuration=Configuration(host=host),
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

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
        body = res.body
        if COMMON_API_KWARGS['skip_deserialization']:
            body = parse_urllib_response(res.response)
        return BranchClient(body, self)

    def get_data(self, id, start: float = None, stop: float = None, binWidth: float = None, limit: float = None):
        """Simplified Data Service getter with significantly higher performance over the Swagger-generated client."""
        url = f'/data/?id={id}'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            url += f'&binWidth={binWidth}'
        elif limit is not None:
            url += f'&limit={limit}'
        response = self.call_api(url, 'GET')
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if 'error' in _response else 'An unknown error occurred.'
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

    def send_request(self, resource_path: str, method: str, body: Optional[Dict] = None):
        """Send a request to the Sedaro server

        Args:
            resource_path (str): url path (everything after the host) for desired route
            method (str): HTTP method ('GET', 'POST', 'DELETE'...etc)
            body (Optional[Union[str, bytes]], optional): Body of the request. Defaults to None.

        Returns:
            Dict: dictionary from the response body
        """
        headers = {}
        if body is not None:
            body = json.dumps(body)
            headers['Content-Type'] = 'application/json'
        res = self.call_api(
            resource_path,
            method.upper(),
            headers=headers,
            body=body
        )
        return parse_urllib_response(res)
