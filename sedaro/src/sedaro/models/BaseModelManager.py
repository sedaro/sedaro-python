from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, overload

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient
    from .BaseModel import BaseModel


@dataclass
class BaseModelManager(ABC):

    _sedaro: 'SedaroApiClient'

    _MODEL: 'ClassVar[type[BaseModel]]'

    @overload
    def get(self) -> 'list[BaseModel]':
        ...

    @overload
    def get(self, id: str) -> 'BaseModel':
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

    @abstractmethod
    def create(cls): ...

    @abstractmethod
    def update(cls): ...

    @abstractmethod
    def delete(cls): ...
