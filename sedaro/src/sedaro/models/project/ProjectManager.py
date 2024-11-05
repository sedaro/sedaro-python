from typing import ClassVar

from ..BaseModelManager import BaseModelManager
from .Project import Project


class ProjectManager(BaseModelManager[Project]):

    _BASE_PATH: 'ClassVar[str]' = '/projects'
    _MODEL: 'ClassVar[type[Project]]' = Project
