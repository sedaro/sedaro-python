from typing import ClassVar

from ..BaseModelManager import BaseModelManager
from .Repository import Repository


class RepositoryManager(BaseModelManager[Repository]):

    _BASE_PATH: 'ClassVar[str]' = '/models/repositories'
    _MODEL = Repository
