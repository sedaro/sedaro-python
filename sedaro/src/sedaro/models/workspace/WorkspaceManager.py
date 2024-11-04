from typing import ClassVar, overload

from ..BaseModelManager import BaseModelManager
from .Workspace import Workspace


class WorkspaceManager(BaseModelManager[Workspace]):

    _BASE_PATH: 'ClassVar[str]' = '/workspaces'
    _MODEL: 'ClassVar[type[Workspace]]' = Workspace

    def create(self): ...

    def update(self): ...

    def delete(self): ...
