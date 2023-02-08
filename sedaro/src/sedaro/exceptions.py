from typing import Any, Union

from sedaro_base_client.exceptions import ApiException


class SedaroException(Exception):
    """Base exception for all exceptions raised by the Sedaro Python Client"""


class SedaroApiException(ApiException, SedaroException):
    """
    Base exception for api exceptions raised by the Sedaro Python Client, inherits from `sedaro_base_client`'s
    `ApiException`
    """
    def __init__(self, status: Union[str, int, None] = None, reason: Union[str, None] = None, api_response: Any = None):
        """Initialize SedaroApiException

        Args:
            status (Union[str, int, None], optional): Defaults to None.
            reason (Union[str, None], optional): Defaults to None.
            api_response (Any, optional): Defaults to None.
        """
        super().__init__(status=status, reason=reason, api_response=api_response)


class NonexistantBlockError(SedaroException):
    pass


class NoBlockFoundError(SedaroException):
    pass
