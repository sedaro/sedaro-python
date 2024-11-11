from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import TYPE_CHECKING, TypeVar

from sedaro.settings import ID

if TYPE_CHECKING:
    from .BaseModelManager import BaseModelManager
    M = TypeVar('M', bound='BaseModel')


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
        mod_man = self._model_manager
        self._raw_data = mod_man._sedaro.request.patch(mod_man._req_url(id=self.id), body=kwargs)

    def refresh(self):
        '''Refresh the model data from the api.'''
        self._raw_data = self._model_manager.get(self.id)._raw_data

    def delete(self):
        '''Delete the corresponding model.'''
        self._delete()

    def _delete(self, *, query_params: dict = None):
        mod_man = self._model_manager
        mod_man._sedaro.request.delete(mod_man._req_url(id=self.id, query_params=query_params))

    def _get_rel(self, field: 'str', base_model_type: 'type[M]') -> 'M' | list[M]:
        '''Get the related model(s) of the given field.'''
        from .BaseModelManager import BaseModelManager

        if (id_or_ids := self._raw_data.get(field)) in (None, []):
            return id_or_ids

        mod_man_cls = BaseModelManager._model_to_model_manager[base_model_type]
        mod_man = mod_man_cls(self._model_manager._sedaro)

        if isinstance(id_or_ids, list):
            return [mod_man.get(id_) for id_ in id_or_ids]
        return mod_man.get(id_or_ids)
