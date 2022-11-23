from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api

from .utils import parse_urllib_response
from .branch_client import BranchClient
from .exceptions import SedaroApiException


class SedaroApiClient(ApiClient):
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
        res = branches_api_instance.get_branch(path_params={'branchId': id})
        return BranchClient(res.body, self)

    def get_data(self, id, start: float = None, stop: float = None, binWidth: float = None):
        """Simplified Data Service getter with significantly higher performance over the Swagger-generated client."""
        url = f'/data/?id={id}'
        if start is not None:
            url += f'&start={start}'
        if stop is not None:
            url += f'&stop={stop}'
        if binWidth is not None:
            url += f'&binWidth={binWidth}'
        response = self.call_api(url, 'GET')
        try:
            _response = parse_urllib_response(response)
            if response.status != 200:
                raise Exception()
        except:
            reason = _response['error']['message'] if 'error' in _response else 'An unknown error occurred.'
            raise SedaroApiException(status=response.status, reason=reason)
        return _response
