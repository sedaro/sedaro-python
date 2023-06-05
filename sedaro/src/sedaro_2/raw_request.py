import json
from typing import TYPE_CHECKING, Dict, Optional

from .utils import parse_urllib_response

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class RawRequest:
    def __init__(self, sedaro: 'SedaroApiClient') -> None:
        self.__sedaro = sedaro

    def __request(self, resource_path: str, method: str, body: Optional[Dict] = None):
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
        with self.__sedaro.api_client() as api:
            res = api.call_api(
                resource_path,
                method,
                headers=headers,
                body=body
            )
        return parse_urllib_response(res)

    def get(self, resource_path: str) -> Dict:
        """Send a 'GET' request to the configured Sedaro host."""
        return self.__request(resource_path, 'GET')

    def post(self, resource_path: str, body: Dict) -> Dict:
        """Send a 'POST' request to the configured Sedaro host."""
        return self.__request(resource_path, 'POST', body)

    def put(self, resource_path: str, body: Dict) -> Dict:
        """Send a 'PUT' request to the configured Sedaro host."""
        return self.__request(resource_path, 'PUT', body)

    def patch(self, resource_path: str, body: Dict) -> Dict:
        """Send a 'PATCH' request to the configured Sedaro host."""
        return self.__request(resource_path, 'PATCH', body)

    def delete(self, resource_path: str) -> Dict:
        """Send a 'DELETE' request to the configured Sedaro host."""
        return self.__request(resource_path, 'DELETE')
