from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


@dataclass
class BaseModelManager(ABC):

    _sedaro: 'SedaroApiClient'

    @abstractmethod
    def get(cls): ...

    @abstractmethod
    def create(cls): ...

    @abstractmethod
    def update(cls): ...

    @abstractmethod
    def delete(cls): ...
