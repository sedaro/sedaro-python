from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING

from sedaro.settings import ID

if TYPE_CHECKING:
    from .BaseModelManager import BaseModelManager


@dataclass
class BaseModel(ABC):
    _raw_data: 'dict'
    _model_manager: 'BaseModelManager'

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    @property
    def id(self):
        return self._raw_data[ID]

    def __getattr__(self, name):
        try:
            return self._raw_data[name]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

    def update(self, **kwargs):
        '''Update the model with the given keyword arguments.'''
        mm = self._model_manager
        self._raw_data = mm._sedaro.request.patch(mm._req_url(id=self.id), body=kwargs)

    def refresh(self):
        '''Refresh the model data from the api.'''
        self._raw_data = self._model_manager.get(self.id)._raw_data

    def delete(self):
        '''Delete the corresponding model.'''
        self._delete()

    def _delete(self, query_params: dict = None):
        mm = self._model_manager
        mm._sedaro.request.delete(mm._req_url(id=self.id, query_params=query_params))
