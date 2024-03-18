import json
from typing import TYPE_CHECKING, Dict, Literal, Optional, Union, overload

import requests
from urllib3.response import HTTPResponse

from .utils import parse_urllib_response

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class PlainRequest:
    def __init__(self, sedaro: 'SedaroApiClient') -> None:
        self.__sedaro = sedaro

    def __request(self, resource_path: str, method: str, body: Optional[Dict] = None, raw: bool = False):
        """Send a request to the Sedaro server

        Args:
            resource_path (str): url path (everything after the host) for desired route
            method (str): HTTP method ('GET', 'POST', 'DELETE'...etc)
            body (Optional[Union[str, bytes]], optional): Body of the request. Defaults to None.
            raw (optional, bool): triggers returning the raw response rather than a dictionary of the response data.\
                Defaults to `False`.

        Returns:
            Dict: dictionary from the response body
        """
        headers = {}

        if body is not None:
            body = json.dumps(body)
            headers['Content-Type'] = 'application/json'

        with self.__sedaro.api_client() as api:
            res = api.call_api(
                resource_path,
                method,
                headers=headers,
                body=body
            )
        if raw:
            return res

        return parse_urllib_response(res)

    @overload
    def get(self, resource_path: str, *, raw: Literal[True]) -> HTTPResponse: ...
    @overload
    def get(self, resource_path: str, *, raw: Literal[False]) -> Dict: ...

    def get(self, resource_path: str, *, raw: bool = False) -> Union[Dict, HTTPResponse]:
        """Send a 'GET' request to the configured Sedaro host.

        Returns a dictionary of the response data unless `raw` is set to `True`, in which case it returns a `urllib3`
        `HTTPResponse`.
        """
        return self.__request(resource_path, 'GET', raw=raw)

    def requests_lib_get(self, url: str) -> requests.Response:
        '''Get request using the requests library'''

        auth_header_name, auth_header_value = self.__sedaro._auth_header()

        kwargs = {
            'url': f'{self.__sedaro._api_host}{url}',
            'headers': {auth_header_name: auth_header_value}
        }

        if self.__sedaro._csrf_token:
            kwargs['headers']['X-CSRFToken'] = self.__sedaro._csrf_token

        if self.__sedaro._proxy_url and self.__sedaro._proxy_url.startswith('http'):
            protocol = self.__sedaro._proxy_url.split('://')[0]
            kwargs['proxies'] = {protocol: self.__sedaro._proxy_url}
            kwargs['headers'] |= self.__sedaro._proxy_headers

        return requests.get(**kwargs)

    @overload
    def post(self, resource_path: str, body: Dict, *, raw: Literal[True]) -> HTTPResponse: ...
    @overload
    def post(self, resource_path: str, body: Dict, *, raw: Literal[False]) -> Dict: ...

    def post(self, resource_path: str, body: Dict, *, raw: bool = False) -> Union[Dict, HTTPResponse]:
        """Send a 'POST' request to the configured Sedaro host.

        Returns a dictionary of the response data unless `raw` is set to `True`, in which case it returns a `urllib3`
        `HTTPResponse`.
        """
        return self.__request(resource_path, 'POST', body, raw=raw)

    @overload
    def put(self, resource_path: str, body: Dict, *, raw: Literal[True]) -> HTTPResponse: ...
    @overload
    def put(self, resource_path: str, body: Dict, *, raw: Literal[False]) -> Dict: ...

    def put(self, resource_path: str, body: Dict, *, raw: bool = False) -> Union[Dict, HTTPResponse]:
        """Send a 'PUT' request to the configured Sedaro host.

        Returns a dictionary of the response data unless `raw` is set to `True`, in which case it returns a `urllib3`
        `HTTPResponse`.
        """
        return self.__request(resource_path, 'PUT', body, raw=raw)

    @overload
    def patch(self, resource_path: str, body: Dict, *, raw: Literal[True]) -> HTTPResponse: ...
    @overload
    def patch(self, resource_path: str, body: Dict, *, raw: Literal[False]) -> Dict: ...

    def patch(self, resource_path: str, body: Dict, *, raw: bool = False) -> Union[Dict, HTTPResponse]:
        """Send a 'PATCH' request to the configured Sedaro host.

        Returns a dictionary of the response data unless `raw` is set to `True`, in which case it returns a `urllib3`
        `HTTPResponse`.
        """
        return self.__request(resource_path, 'PATCH', body, raw=raw)

    @overload
    def delete(self, resource_path: str, *, raw: Literal[True]) -> HTTPResponse: ...
    @overload
    def delete(self, resource_path: str, *, raw: Literal[False]) -> Dict: ...

    def delete(self, resource_path: str, *, raw: bool = False) -> Union[Dict, HTTPResponse]:
        """Send a 'DELETE' request to the configured Sedaro host.

        Returns a dictionary of the response data unless `raw` is set to `True`, in which case it returns a `urllib3`
        `HTTPResponse`.
        """
        return self.__request(resource_path, 'DELETE', raw=raw)
