from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar, overload
from urllib.parse import urlencode

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
        '''Get a all accessible models or a single model by id'''
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
        '''Create a new model with the given keyword arguments'''
        w = self._sedaro.request.post(self._BASE_PATH, body)
        return self._MODEL(w, self)

    __NO_EXPAND = {'expand': {}}

    def _req_url(self, *, id: str = None, query_params: 'dict' = None) -> 'str':
        '''Return the request url for the given id and query parameters'''
        if query_params is None:
            query_str = f'?{urlencode(self.__NO_EXPAND)}'
        else:
            query_str = f'?{urlencode(query_params | self.__NO_EXPAND)}'

        id_str = f'/{id}' if id is not None else ""
        return f'{self._BASE_PATH}{id_str}{query_str}'
