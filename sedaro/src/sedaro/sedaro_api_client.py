from contextlib import contextmanager
from typing import Any, Dict, Generator, Tuple

import requests
from sedaro_base_client import Configuration
from sedaro_base_client.api_client import ApiClient
from sedaro_base_client.apis.tags import branches_api
from urllib3.exceptions import InsecureRequestWarning
from urllib3.response import HTTPResponse

from .branches import AgentTemplateBranch, Branch, ScenarioBranch
from .models.branch import BranchManager
from .models.project import ProjectManager
from .models.repository import RepositoryManager
from .models.workspace import WorkspaceManager
from .plain_request import PlainRequest
from .settings import COMMON_API_KWARGS
from .utils import body_from_res


class SedaroApiClient(ApiClient):
    """A client to interact with the Sedaro API"""

    def __init__(
        self,
        api_key: 'str' = None,
        host='https://api.sedaro.com',
        *,
        auth_handle: 'str' = None,
        proxy_url: str = None,
        proxy_headers: Dict[str, str] = None,
        suppress_insecure_transport_warnings: bool = False,
    ):
        '''Instantiate a SedaroApiClient. Either `api_key` or `auth_handle` must be provided.

        Args:
            api_key (str, optional): API key to authenticate with the Sedaro API
            host (str, optional): URL of the Sedaro API
            auth_handle (str, optional): Authentication handle to authenticate with the Sedaro API
            proxy_url (str, optional): URL of the proxy server
            proxy_headers (Dict[str, str], optional): Headers to send to the proxy server

        Note: for proxy kwargs, refer to https://urllib3.readthedocs.io/en/stable/reference/urllib3.poolmanager.html#urllib3.ProxyManager
        '''

        if (api_key and auth_handle) or not (api_key or auth_handle):
            raise ValueError('Either provide an `api_key` or an `auth_handle` and not both.')

        if host[-1] == '/':
            host = host[:-1]  # remove trailing forward slash

        self._api_host = host

        self._api_key = api_key
        self._auth_handle = auth_handle

        self._proxy_url = proxy_url
        self._proxy_headers = proxy_headers
        self._verify_ssl = True
        if self._proxy_url and not self._proxy_url.startswith('https'):
            self._verify_ssl = False

        # Optionally suppress insecure transport warning if a proxy is being used
        if not self._verify_ssl and suppress_insecure_transport_warnings:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        self._csrf_token = None

    @contextmanager
    def api_client(self) -> Generator[ApiClient, Any, None]:
        """Instantiate ApiClient from sedaro_base_client

        Yields:
            Generator[ApiClient, Any, None]: ApiClient
        """
        header_name, header_value = self._auth_header()

        configuration = Configuration(host=self._api_host)
        configuration.proxy = self._proxy_url
        configuration.proxy_headers = self._proxy_headers
        if self._proxy_url:
            configuration.verify_ssl = self._verify_ssl

        with ApiClient(
            configuration=configuration,
            header_name=header_name,
            header_value=header_value
        ) as api:
            yield api

    def _auth_header(self) -> Tuple[str, str]:
        """Get the auth header name and value for the Sedaro API"""
        if self._auth_handle is not None:
            return 'X_AUTH_HANDLE', self._auth_handle
        else:
            return 'X_API_KEY', self._api_key

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
            # return Branch(res.body, self)
            res = branches_api_instance.get_branch(
                path_params={'branchId': branch_id}, **COMMON_API_KWARGS)

            res_: HTTPResponse = res.response
            for cookie in res_.headers.get_all('Set-Cookie'):
                if 'csrf' in cookie:
                    self._csrf_token = cookie.split(';')[0].split('=')[1]
                    break

            return body_from_res(res)

    def agent_template(self, branch_id: str) -> AgentTemplateBranch:
        """Instantiate an `AgentTemplateBranch` object associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            AgentTemplateBranch: `AgentTemplateBranch` object
        """
        return AgentTemplateBranch(self.__get_branch(branch_id), self)

    def scenario(self, branch_id: str) -> ScenarioBranch:
        """Instantiate an `ScenarioBranch` object associated with the Sedaro `Branch` with `branch_id`

        Args:
            branch_id (str): `id` of the Sedaro Agent Template `Branch` to get

        Returns:
            ScenarioBranch: `ScenarioBranch` object
        """
        return ScenarioBranch(self.__get_branch(branch_id), self)

    def branch(self, branch_id: 'str') -> 'Branch':
        """Instantiate a `Branch` object associated with the Sedaro `Branch` with `branch_id`. The `Branch` object has
        methods and attributes for interacting with the `Block`s and attributes of the Sedaro `Branch`.

        Note that the `agent_template` and `scenario` methods return more specific objects and may be used when the type
        of the `Branch` is known.

        Args:
            branch_id (str): `id` of the Sedaro `Branch` to get

        Returns:
            Branch: `Branch` object
        """
        return Branch(self.__get_branch(branch_id), self)

    @property
    def request(self) -> PlainRequest:
        """API for sending raw `get`, `post`, `put`, `patch`, and `delete` requests to the configured Sedaro host."""
        return PlainRequest(self)

    # ==================================================================================================================
    # Model Managers
    # ==================================================================================================================

    @property
    def Workspace(self):
        return WorkspaceManager(_sedaro=self)

    @property
    def Repository(self):
        return RepositoryManager(_sedaro=self)

    @property
    def Project(self):
        return ProjectManager(_sedaro=self)

    @property
    def Branch(self):
        return BranchManager(_sedaro=self)
