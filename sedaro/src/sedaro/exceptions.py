class SedaroException(Exception):
    """Base exception for all exceptions raised in the Sedaro Python Client"""
    pass


class SedaroValueError(SedaroException):
    pass


class SedaroKeyError(SedaroException):
    pass


class SedaroTypeError(SedaroException):
    pass
