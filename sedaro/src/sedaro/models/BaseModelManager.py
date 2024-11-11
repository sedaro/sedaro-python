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
    '''The SedaroApiClient instance'''

    _MODEL: 'ClassVar[type[M]]'
    '''The model class that this manager manages'''
    _BASE_PATH: 'ClassVar[str]'
    '''The base path for the model'''

    _model_to_model_manager: 'ClassVar[dict[type[BaseModel], type[BaseModelManager]]]' = {}
    '''Mapping of model to model manager, automatically set by __init_subclass__'''

    def __init_subclass__(cls):
        if cls._MODEL in cls._model_to_model_manager:
            raise ValueError(
                f'Attempting to have multiple managers ({cls} and {cls._model_to_model_manager[cls._MODEL]}) for the same model: {cls._MODEL}'
            )
        cls._model_to_model_manager[cls._MODEL] = cls
        return super().__init_subclass__()

    @overload
    def get(self) -> 'list[M]': ...
    @overload
    def get(self, id: str) -> 'M': ...

    def get(self, id: 'str' = None, /) -> 'list[M] | M':
        '''Get a all accessible models or a single model by id'''
        if id is None:
            return [
                self._MODEL(w, self) for w in
                self._sedaro.request.get(self._req_url())
            ]

        return self._MODEL(
            self._sedaro.request.get(self._req_url(id=id)),
            self
        )

    def create(self, **body) -> 'M':
        '''Create a new model with the given keyword arguments'''
        w = self._sedaro.request.post(self._req_url(), body)
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
