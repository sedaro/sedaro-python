from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from sedaro.settings import ID

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


@dataclass
class BaseModel(ABC):
    _raw_data: 'dict'
    _sedaro: 'SedaroApiClient'

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
