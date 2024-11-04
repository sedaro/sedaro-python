from typing import ClassVar, overload

from ..BaseModelManager import BaseModelManager
from .Workspace import Workspace


class WorkspaceManager(BaseModelManager):

    _BASE_PATH: 'ClassVar[str]' = '/workspaces'
    _MODEL: 'ClassVar[type[Workspace]]' = Workspace

    @overload
    def get(self) -> 'list[Workspace]':
        ...

    @overload
    def get(self, id: str) -> 'Workspace':
        ...

    def get(self, id: 'str' = None, /):
        if id is None:
            return [
                self._MODEL(w, self) for w in
                self._sedaro.request.get(self._BASE_PATH)
            ]

        return self._MODEL(
            self._sedaro.request.get(f'{self._BASE_PATH}/{id}'),
            self
        )

    def create(self): ...

    def update(self): ...

    def delete(self): ...
