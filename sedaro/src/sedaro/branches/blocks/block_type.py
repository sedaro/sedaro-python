from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, List, Union

from ...exceptions import NoBlockFoundError
from ...settings import BLOCKS, CRUD, DATA_SIDE, ID, INDEX, MANY_SIDE, ONE_SIDE, TYPE
from ...utils import enforce_id_in_branch
from .block import Block

if TYPE_CHECKING:
    from ..branch import Branch


@dataclass
class BlockType:
    '''Class for getting `Block`s associated with Sedaro Blocks of this class type'''
    type: str
    '''Name of the Sedaro Block class this `BlockType` is set up to interact with'''
    _branch: 'Branch'
    '''The `Branch` this `BlockType` is connected to'''

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.type}, branch={self._branch.id})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(f'{self.__class__.__name__}-{self.type}-{self._branch.id}')

    def create(self, **fields) -> Block:
        """Creates a Sedaro Block of the given type in the corresponding Branch. Note that if 'id' or 'type' are passed
        as kwargs, they will be ignored.

        Args:
            **fields (any): required and optional fields on the corresponding Sedaro Block.

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            Block: a client to interact with the created Sedaro Block
        """

        for kwarg in [ID, TYPE]:
            fields.pop(kwarg, None)

        res = self._branch.crud(blocks=[{**fields, **{TYPE: self.type}}])
        block_id = res[CRUD][BLOCKS][-1]
        return Block(block_id, self)

    def get(self, id: Union[str, int]) -> Block:
        """Gets a `Block` of the desired type associated with the Sedaro Block of the given `id`.

        Args:
            id (Union[str, int]): `id` of the desired Sedaro Block

        Raises:
            KeyError: if no corresponding Block exists of the desired type

        Returns:
            Block: a client to interact with the corresponding Sedaro Block
        """
        enforce_id_in_branch(self._branch, id)

        # in addition to checks in ^^^ also make sure is the correct type for this BlockType
        if id not in self.get_all_ids():
            raise KeyError(
                f'There is no "{self.type}" with id "{id}" in this Branch.')

        return Block(id, self)

    def get_all_ids(self) -> List[str]:
        """Gets a `list` of `id`s corresponding to all Sedaro Blocks of the given type in this Branch. If there are no
        corresponding Blocks, returns an empty `list`.

        Returns:
            List[str]: list of `id`s
        """
        index = self._branch.data[INDEX]

        res = []

        def recurse_get_block_dicts(block_type):
            for type_or_id in index[block_type]:
                if type_or_id in index:
                    recurse_get_block_dicts(type_or_id)
                else:
                    res.append(type_or_id)

        recurse_get_block_dicts(self.type)

        # maintain order & filter out duplicates
        return list(dict.fromkeys(res))

    def get_all(self) -> List['Block']:
        """Gets a `list` of all `Block` instances corresponding to all Sedaro Blocks of the given type in this
        Branch. If there are no corresponding Blocks, returns an empty `list`.

        Returns:
            List['Block']: a list of `Block` instances corresponding to Sedaro Blocks in this Branch
        """
        return [Block(id, self) for id in self.get_all_ids()]

    def get_where(self, **fields) -> List['Block']:
        """
        Gets a filtered `list` of all `Block` instances corresponding to all Sedaro Blocks of the given type in
        this Branch. Blocks are filtered by property/values passed as kwargs. If there are no corresponding Blocks,
        returns an empty `list`.

        If querying via a relationship field, values can be passed as `Block` instances or `id`s. If querying on a Many
        side relationship specifically, the value is compared independent of order.

        **fields:
            any: keys to check for given values on the Sedaro Blocks

        Returns:
            List['Block']: a filtered list of `Block` instances corresponding to Sedaro Blocks in this\
                Branch
        """
        return [
            block for block in self.get_all()
            if all(self.__get_where_check_equality(block, k, v) for k, v in fields.items())
        ]

    def __get_where_check_equality(self, block_to_check: 'Block', attr: 'str', expected_val: Any) -> 'bool':
        '''Checks if the given `block_to_check` has the expected value for the given attribute `attr`. Turn all values
        into `id`s if they are `Block` instances in relationship fields.'''
        MISSING = object()
        # get `actual_val` from `data` rather than the Block itself to avoid rel values turning into Blocks
        if (actual_val := block_to_check.data.get(attr, MISSING)) is MISSING:
            return False

        if not block_to_check.is_rel_field(attr):
            return actual_val == expected_val

        side_type = block_to_check.get_rel_field_type(attr)

        if side_type == MANY_SIDE:
            if not isinstance(expected_val, list):
                return False
            expected_val = [
                v.id if isinstance(v, Block) else v
                for v in expected_val
            ]
            try:
                return set(expected_val) == set(actual_val)
            except:
                return False

        if side_type == DATA_SIDE:
            if not isinstance(expected_val, dict):
                return False
            expected_val = {
                k.id if isinstance(k, Block) else k: v
                for k, v in expected_val.items()
            }
            return expected_val == actual_val

        if side_type == ONE_SIDE:
            expected_val = expected_val.id if isinstance(expected_val, Block) else expected_val
            return actual_val == expected_val

        raise NotImplementedError(
            f'Unsupported relationship type on "{self.type}", attribute: "{attr}".'
        )

    def get_first(self):
        """Returns a `Block` associated with the least recently added (lowest `id`) Sedaro Block of the desired
        type.

        Raises:
            NoBlockFoundError: if no Blocks of the desired type exist in this Branch

        Returns:
            Block: a client to interact with the corresponding Sedaro Block
        """
        all_ids = self.get_all_ids()
        if not len(all_ids):
            raise NoBlockFoundError(
                f'No "{self.type}" Blocks exist in this Branch.'
            )
        return Block(sorted(all_ids)[0], self)

    def get_last(self):
        """Returns a `Block` associated with the most recently added (highest `id`) Sedaro Block of the desired
        type.

        Raises:
            NoBlockFoundError: if no Blocks of the desired type exist in this Branch

        Returns:
            Block: a client to interact with the corresponding Sedaro Block
        """
        all_ids = self.get_all_ids()
        if not len(all_ids):
            raise NoBlockFoundError(
                f'No "{self.type}" Blocks exist in this Branch.'
            )
        return Block(sorted(all_ids)[-1], self)
