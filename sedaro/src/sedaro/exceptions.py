from sedaro_base_client.exceptions import ApiException

class SedaroException(Exception):
    """Base exception for all exceptions raised by the Sedaro Python Client"""

class SedaroApiException(ApiException, SedaroException):
    """
    Base exception for ApiExceptions exceptions raised by the Sedaro Python Client, inherits from sedaro_base_client's
    ApiException
    """
    pass


class NonexistantBlockError(SedaroException):
    pass


class NoBlockFoundError(SedaroException):
    pass
