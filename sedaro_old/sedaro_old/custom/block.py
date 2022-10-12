from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass

if TYPE_CHECKING:
    from .block_class_client import BlockClassClient


@dataclass
class Block:
    id: int
    block_class_client: 'BlockClassClient'
    '''Class for interacting with all Blocks of this class type'''
    block_group: str
    '''Corresponds to actual Sedaro BlockGroup name'''

    def __str__(self) -> str:
        return f'Block(id={self.id}, data={self.data}, block_group={self.block_group})'

    @property
    def data(self):
        return self.block_class_client.branch.data[self.block_group][self.id]
