class SedaroException(Exception):
    """Base exception for all exceptions raised in the Sedaro Python Client"""
    pass


class NonexistantBlockError(SedaroException):
    pass


class NoBlockFoundError(SedaroException):
    pass
