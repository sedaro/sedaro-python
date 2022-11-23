from sedaro_base_client.exceptions import ApiException


class SedaroApiException(ApiException):
    """Base exception for all exceptions raised in the Sedaro Python Client"""
    pass


class NonexistantBlockError(SedaroApiException):
    pass


class NoBlockFoundError(SedaroApiException):
    pass
