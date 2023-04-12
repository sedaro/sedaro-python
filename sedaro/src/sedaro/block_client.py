from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict

from pydash import is_empty

from .exceptions import NonexistantBlockError
from .settings import (BLOCKS, DATA_SIDE, ID, MANY_SIDE, ONE_SIDE,
                       RELATIONSHIPS, TYPE)

if TYPE_CHECKING:
    from .block_class_client import BlockClassClient
    from .branch_client import BranchClient
    from .sedaro_api_client import SedaroApiClient


@dataclass
class BlockClient:
    id: str
    _block_class_client: 'BlockClassClient'
    '''Class for interacting with all Blocks of this class type'''

    def __str__(self) -> str:
        return f'{self.data[TYPE]}(id={self.id})'

    def __repr__(self):
        attrs = ''
        for k, v in self.data.items():
            if type(v) is str:
                v = f"'{v}'"
            attrs += f'\n   {k}={v}'
        return f'\n{self.data[TYPE]}({attrs}\n)\n'

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self):
        # allows a BlockClient to be a key in a dict and @lru_cache wrapper to work on methods on this class
        return hash(self.__class__.__name__ + self.id)

    def __getattr__(self, key: str) -> any:
        """Allows for dotting into the `BlockClient` to access keys on the referenced Sedaro Block. Additionally, makes
        it so dotting into relationship fields returns `BlockClient`s corresponding to the related Sedaro Blocks.

        Args:
            key (str): attribute being keyed into

        Raises:
            AttributeError: if the attribute doesn't exist on the refrenced Sedaro Block

        Returns:
            any: the value of the corresponding attribute on the referenced Sedaro Block
        """
        if key not in self.data:
            raise make_attr_error(key, self.data[TYPE])
        val = self.data[key]

        if not self.is_rel_field(key):
            return val

        side_type = self.get_rel_field_type(key)

        if side_type == MANY_SIDE:
            return [self._branch_client.get_block(id) for id in val]

        if side_type == DATA_SIDE:
            return {self._branch_client.get_block(id): data for id, data in val.items()}

        if side_type == ONE_SIDE:
            return self._branch_client.get_block(val)

        raise NotImplementedError(
            f'Unsupported relationship type on "{self.data[TYPE]}", attribute: "{key}".'
        )

    @property
    def type(self) -> str:
        '''Name of the class of the Sedaro Block this `BlockClient` is set up to interact with'''
        return self._block_class_client.type

    @property
    def data(self) -> Dict:
        '''The properties of the corresponding Sedaro Block as a dictionary'''
        self.enforce_still_exists()
        return self._branch_client.data[BLOCKS][self.id]

    @property
    def _branch_client(self) -> 'BranchClient':
        '''The `BranchClient` this `BlockClient` is connected to'''
        return self._block_class_client._branch_client

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClient` was accessed through'''
        return self._branch_client._sedaro_client

    def check_still_exists(self) -> bool:
        """Checks whether the Sedaro Block this `BlockClient` references still exists.

        Returns:
            bool: indication of whether or not the referenced Sedaro Block still exists
        """
        return self.id in self._branch_client.data[BLOCKS]

    def enforce_still_exists(self) -> None:
        """Raises and error if the Sedaro Block this `BlockClient` references no longer exists.

        Raises:
            NonexistantBlockError: indication that the Block no longer exists.
        """
        if not self.check_still_exists():
            raise NonexistantBlockError(
                f'The referenced "{self.type}" (id: {self.id}) no longer exists.'
            )

    def update(self, **fields) -> 'BlockClient':
        """Update attributes of the corresponding Sedaro Block

        Args:
            **fields (Dict): desired attributes to update on the Sedaro Block

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            BlockClient: updated `BlockClient` (Note: the previous `BlockClient` reference is also updated)
        """
        if is_empty(fields):
            raise ValueError(f'Must provide fields to update on the {self.type}.')
        if ID in fields:
            raise ValueError(f'Invalid kwarg for update method: {ID}.')
        # NOTE: `self.data` calls `self.enforce_still_exists()`, so don't need to call here
        self._branch_client.crud(blocks=[{**self.data, **fields}])
        return self

    def delete(self) -> str:
        """Deletes the associated Sedaro Block

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            str: `id` of the deleted Sedaro Block
        """
        self.enforce_still_exists()
        self._branch_client.crud(delete=[self.id])
        return self.id

    def is_rel_field(self, field: str) -> bool:
        """Checks if the given `field` is a relationship field on the associated Sedaro Block.

        Args:
            field (str): field to check

        Raises:
            TypeError: if the value of `field` is not a string

        Returns:
            bool: indicates if the given `field` is a relationship field on the Sedaro Block or not.
        """
        return field in self._branch_client.data[RELATIONSHIPS][self.data[TYPE]]

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

        return self._branch_client.data[RELATIONSHIPS][self.data[TYPE]][field][TYPE]


# ------ helper function and vars for this file only ------
def make_attr_error(field: str, block_name: str) -> str:
    return AttributeError(f'There is no "{field}" attribute on "{block_name}"')
