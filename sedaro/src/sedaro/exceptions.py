class SedaroException(Exception):
    """Base exception for all exceptions raised in the Sedaro Python Client"""
    pass


class SedaroNonexistantBlockError(SedaroException):
    pass


class SedaroNoBlockFoundError(SedaroException):
    pass
