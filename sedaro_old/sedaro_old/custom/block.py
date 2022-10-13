from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass
from pydash import snake_case

from sedaro_old.api_client import Api
from .settings import UPDATE

if TYPE_CHECKING:
    from .block_class_client import BlockClassClient
    from .sedaro_api_client import SedaroApiClient
    from .branch import Branch


@dataclass
class Block:
    id: str
    block_class_client: 'BlockClassClient'
    '''Class for interacting with all Blocks of this class type'''

    def __str__(self) -> str:
        return f'Block(id={self.id}, data={self.data}, block_group={self.block_group})'

    @property
    def data(self) -> Dict:
        # FIXME: handle when it's deleted... (KeyError)
        return self.branch.data[self.block_group][self.id]

    @property
    def name(self) -> str:
        '''The name of the class associated with this `Block`'''
        return self.block_class_client.block_name

    @property
    def branch(self) -> 'Branch':
        '''The `Branch` this `Block` is connected to'''
        return self.block_class_client.branch

    @property
    def sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `Block` was accessed through'''
        return self.branch.sedaro_client
