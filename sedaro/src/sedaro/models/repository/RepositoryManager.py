from typing import ClassVar

from ..BaseModelManager import BaseModelManager
from .Repository import Repository


class RepositoryManager(BaseModelManager[Repository]):

    _BASE_PATH: 'ClassVar[str]' = '/repositories'
    _MODEL: 'ClassVar[type[Repository]]' = Repository
