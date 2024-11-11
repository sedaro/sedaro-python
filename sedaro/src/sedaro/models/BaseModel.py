from __future__ import annotations

import json
from abc import ABC
from dataclasses import dataclass, field
from functools import cache
from typing import TYPE_CHECKING, TypeVar

from sedaro.settings import BLOCKS, ID

if TYPE_CHECKING:
    from .BaseModelManager import BaseModelManager
    M = TypeVar('M', bound='BaseModel')


@dataclass
class BaseModel(ABC):
    _raw_data: 'dict'
    _model_manager: 'BaseModelManager' = field(repr=False)

    def __update_data(self, data: 'dict'):
        self._raw_data.update(data)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def __getattr__(self, name):
        try:
            return self._raw_data[name]
        except KeyError:
            raise AttributeError(f"{self.__class__.__name__} has no attribute '{name}'")

    def __hash__(self):
        return hash(json.dumps(self._raw_data, sort_keys=True))

    def __eq__(self, other):
        if not (isinstance(other, self.__class__) and (self.id == other.id)):
            return False

        if set(self._raw_data) != set(other._raw_data):
            return False

        return hash(self) == hash(other)

    @property
    def id(self):
        '''The id of the model.'''
        return self._raw_data[ID]

    def update(self, **kwargs):
        '''Update the model with the given keyword arguments.'''
        mod_man = self._model_manager
        res = mod_man._sedaro.request.patch(mod_man._req_url(id=self.id), body=kwargs)
        self.__update_data(res)

    def refresh(self):
        '''Refresh the model data from the api.'''
        res = self._model_manager.get(self.id)._raw_data
        self.__update_data(res)
        self._get_rel.cache_clear()

    def delete(self):
        '''Delete the corresponding model.'''
        self._delete()

    def _delete(self, *, query_params: dict = None):
        mod_man = self._model_manager
        mod_man._sedaro.request.delete(mod_man._req_url(id=self.id, query_params=query_params))

    @cache
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
