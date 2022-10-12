from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass

from .block_group_single_class import BlockGroupSingleClass

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


@dataclass
class Branch:
    id: int
    data: Dict
    sedaro_client: 'SedaroApiClient'

    def __str__(self):
        return f'Branch(id: {self.id})'

    def __getattr__(self, block_name: str) -> BlockGroupSingleClass:
        block_open_api_instance = self.sedaro_client._get_block_open_api_instance(block_name)
        block_create_class = self.sedaro_client._get_create_or_update_block_model(
            block_name,
            'create'
        )
        return BlockGroupSingleClass(
            block_name=block_name,
            block_openapi_instance=block_open_api_instance,
            create_class=block_create_class,
            branch_id=self.id
        )
