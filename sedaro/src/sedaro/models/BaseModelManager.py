from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar, overload

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient
    from .BaseModel import BaseModel

M = TypeVar('M', bound='BaseModel')


@dataclass
class BaseModelManager(ABC, Generic[M]):

    _sedaro: 'SedaroApiClient'

    _MODEL: 'ClassVar[type[M]]'
    _BASE_PATH: 'ClassVar[str]'

    @overload
    def get(self) -> 'list[M]': ...
    @overload
    def get(self, id: str) -> 'M': ...

    def get(self, id: 'str' = None, /) -> 'list[M] | M':
        if id is None:
            return [
                self._MODEL(w, self) for w in
                self._sedaro.request.get(self._BASE_PATH)
            ]

        return self._MODEL(
            self._sedaro.request.get(f'{self._BASE_PATH}/{id}'),
            self
        )

    def create(self, **body) -> 'M':
        w = self._sedaro.request.post(self._BASE_PATH, body)
        return self._MODEL(w, self)

    # @abstractmethod
    # def update(cls): ...

    # @abstractmethod
    # def delete(cls): ...
