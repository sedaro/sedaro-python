from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass

if TYPE_CHECKING:
    from .block_group_single_class import BlockGroupSingleClass


@dataclass
class Block:
    id: int
    data: Dict
    block_group_single_class: 'BlockGroupSingleClass'
    '''Class for interacting with all Blocks of this class type'''
    block_group: str
    '''Corresponds to actual Sedaro BlockGroup name'''

    def __str__(self) -> str:
        return f'Block(id={self.id}, data={self.data}, block_group={self.block_group})'
