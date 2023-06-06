from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Union

from pydash import is_empty

from ...exceptions import NoBlockFoundError
from ...settings import BLOCKS, CRUD, ID, INDEX, TYPE
from ...utils import enforce_id_in_branch
from .block import Block

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient
    from ..branch_client import Branch


@dataclass
class BlockType:
    '''Class for getting `Block`s associated with Sedaro Blocks of this class type'''
    type: str
    '''Name of the Sedaro Block class this `BlockType` is set up to interact with'''
    _branch_client: 'Branch'
    '''The `Branch` this `BlockType` is connected to'''

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.type}, branch={self._branch_client.id})'

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(f'{self.__class__.__name__}-{self.type}-{self._branch_client.id}')

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockType` was accessed through'''
        return self._branch_client._sedaro_client

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
        if is_empty(fields):
            raise ValueError(f'Must provide fields to create a {self.type}')

        for kwarg in [ID, TYPE]:
            fields.pop(kwarg, None)

        res = self._branch_client.crud(blocks=[{**fields, **{TYPE: self.type}}])
        block_id = res[CRUD][BLOCKS][0]
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
        enforce_id_in_branch(self._branch_client, id)

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
        index = self._branch_client.data[INDEX]

        res = []

        def recurse_get_block_dicts(block_type):
            for type_or_id in index[block_type]:
                if type_or_id in index:
                    recurse_get_block_dicts(type_or_id)
                else:
                    res.append(type_or_id)

        recurse_get_block_dicts(self.type)

        return res

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

        **fields:
            any: keys to check for given values on the Sedaro Blocks

        Returns:
            List['Block']: a filtered list of `Block` instances corresponding to Sedaro Blocks in this\
                Branch
        """
        return [
            b_c for b_c in self.get_all() if all(getattr(b_c, k) == v for k, v in fields.items())
        ]

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
