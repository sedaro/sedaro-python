from typing import ClassVar

from ..BaseModelManager import BaseModelManager
from .Workspace import Workspace


class WorkspaceManager(BaseModelManager[Workspace]):

    _BASE_PATH: 'ClassVar[str]' = '/workspaces'
    _MODEL: 'ClassVar[type[Workspace]]' = Workspace
