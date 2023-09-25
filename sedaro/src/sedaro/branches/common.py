from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict

from ..settings import DATA_SIDE, MANY_SIDE, ONE_SIDE, TYPE

if TYPE_CHECKING:
    from .branch import Branch


class Common(ABC):
    """Abstract class for common functionality between `Branch` and `Block` classes."""

    @property
    @abstractmethod
    def data(self) -> Dict:
        '''Access the dictionary corresponding to root or the `Block` this instance is associated with.'''
        pass

    @property
    @abstractmethod
    def _branch(self) -> 'Branch':
        '''Access the `Branch` this instance is associated with.'''
        pass

    @property
    @abstractmethod
    def _relationship_attrs(self) -> Dict:
        '''Access the relationship fields dictionary from the meta attributes corresponding to root or the `Block` this
        instance is associated with.'''
        pass

    def __getattr__(self, key: str) -> any:
        """Allows for dotting into the instance to access keys on the referenced Sedaro `Block` or root. Additionally,
        makes it so dotting into relationship fields returns `Block`s corresponding to the related Sedaro Blocks.

        Args:
            key (str): attribute being keyed into

        Raises:
            AttributeError: if the attribute doesn't exist

        Returns:
            any: the value of the corresponding attribute
        """
        if key not in self.data:
            raise make_attr_error(key, self.data[TYPE])
        val = self.data[key]

        if not self.is_rel_field(key):
            return val

        side_type = self.get_rel_field_type(key)

        if side_type == MANY_SIDE:
            return [self._branch.block(id) for id in val]

        if side_type == DATA_SIDE:
            return {self._branch.block(id): data for id, data in val.items()}

        if side_type == ONE_SIDE:
            return self._branch.block(val)

        raise NotImplementedError(
            f'Unsupported relationship type on "{self.data[TYPE]}", attribute: "{key}".'
        )

    def is_rel_field(self, field: str) -> bool:
        """Checks if the given `field` is a relationship field on the associated Sedaro Block.

        Args:
            field (str): field to check

        Raises:
            TypeError: if the value of `field` is not a string

        Returns:
            bool: indicates if the given `field` is a relationship field on the Sedaro Block or not.
        """
        return field in self._relationship_attrs

    def get_rel_field_type(self, field: str) -> str:
        """Get the type of relationship of the field. Note: first call `is_rel_field` if you need to confirm `field` is
        a relationship field.

        Args:
            field (str): the field to get the relationship type for

        Raises:
            TypeError: if the value of `field` is not a string or not a relationship field on this type of Sedaro Block
            KeyError: if the value of `field` does not correspond to any field on the associated Sedaro Block

        Returns:
            str: a string indicating the type of relationship field
        """
        if not self.is_rel_field(field):
            raise TypeError(
                f'The given field "{field}" is not a relationship field on "{self.data[TYPE]}".')

        return self._relationship_attrs[field][TYPE]


# ------ helper function and vars for this file only ------


def make_attr_error(field: str, block_name: str) -> str:
    return AttributeError(f'There is no "{field}" attribute on "{block_name}"')
