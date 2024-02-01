import copy
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict

from pydash import is_empty

from ...exceptions import NonexistantBlockError
from ...settings import BLOCKS, CRUD, ID, RELATIONSHIPS, TYPE
from ..common import Common

if TYPE_CHECKING:
    from ..branch import Branch
    from .block_type import BlockType


@dataclass
class Block(Common):
    id: str
    _block_type: 'BlockType'
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
        # allows a Block instance to be a key in a dictionary
        return hash(self.__class__.__name__ + self.id)

    @property
    def type(self) -> str:
        '''Name of the class of the Sedaro Block this `Block` instance is set up to interact with'''
        return self.data[TYPE]

    @property
    def data(self) -> Dict:
        '''The properties of the corresponding Sedaro Block as a dictionary'''
        self.enforce_still_exists()
        return self._branch.data[BLOCKS][self.id]

    @property
    def _branch(self) -> 'Branch':
        '''The `Branch` this `Block` instance is connected to'''
        return self._block_type._branch

    @property
    def _relationship_attrs(self) -> Dict:
        """The relationship fields dictionary from the meta attributes corresponding to the Sedaro Block this `Block`
        instance is associated with."""
        return self._branch.data[RELATIONSHIPS][self.type]

    def check_still_exists(self) -> bool:
        """Checks whether the Sedaro Block this `Block` instance references still exists.

        Returns:
            bool: indication of whether or not the referenced Sedaro Block still exists
        """
        return self.id in self._branch.data[BLOCKS]

    def enforce_still_exists(self) -> None:
        """Raises and error if the Sedaro Block this `Block` instance references no longer exists.

        Raises:
            NonexistantBlockError: indication that the Block no longer exists.
        """
        if not self.check_still_exists():
            raise NonexistantBlockError(
                f'The referenced Block with ID: {self.id} no longer exists.'
            )

    def clone(self) -> 'Block':
        """Creates a copy of the Sedaro Block corresponding to the `Block` instance this method is called on.

        Note:
        - if there is a name attribute, the name of the created `Block`s will have `'(clone)'` appended to it.
        - this will not work if the resulting clone violates unique constraints.

        Returns:
            Block: `Block` associated with the created Sedaro `Block`
        """
        new_block = copy.deepcopy(self.data)
        del new_block[ID]

        if 'name' in new_block:
            new_block['name'] = f'{new_block["name"]} (clone)'

        res = self._branch.crud(
            blocks=[new_block]
        )

        return self._branch.block(res[CRUD][BLOCKS][0])

    def update(self, **fields) -> 'Block':
        """Update attributes of the corresponding Sedaro Block

        Args:
            **fields (Dict): desired field/value pairs to update

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            Block: updated `Block` (Note: the previous `Block` reference is also updated)
        """
        if is_empty(fields):
            raise ValueError(
                f'Must provide fields to update on the {self.type}.')

        if ID in fields and fields[ID] != self.id:
            raise ValueError(
                f'Invalid value for "{ID}". Omit or ensure it is the same as this Block\'s {ID}.')

        # NOTE: `self.data` calls `self.enforce_still_exists()`, so don't need to call here
        self._branch.crud(blocks=[{**self.data, **fields}])
        return self

    def delete(self) -> str:
        """Deletes the associated Sedaro Block

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            str: `id` of the deleted Sedaro Block
        """
        self.enforce_still_exists()
        self._branch.crud(delete=[self.id])
        return self.id
