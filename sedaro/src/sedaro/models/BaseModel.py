from abc import ABC, abstractmethod
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

    def delete(self):
        mm = self._model_manager
        mm._sedaro.request.delete(f"{mm._BASE_PATH}/{self.id}")
