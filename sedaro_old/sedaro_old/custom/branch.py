from typing import TYPE_CHECKING, Dict, Tuple
from dataclasses import dataclass

from sedaro_old.api_client import ApiResponse
from .block_class_client import BlockClassClient
from .utils import parse_block_crud_response
from .settings import CREATE, UPDATE, DELETE

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


@dataclass
class Branch:
    id: int
    data: Dict
    sedaro_client: 'SedaroApiClient'

    def __str__(self):
        return f'Branch(id: {self.id})'

    def __getattr__(self, block_name: str) -> BlockClassClient:
        block_open_api_instance = self.sedaro_client._get_block_open_api_instance(block_name)
        block_create_class = self.sedaro_client._get_create_or_update_block_model(
            block_name,
            'create'
        )
        return BlockClassClient(
            block_name=block_name,
            block_openapi_instance=block_open_api_instance,
            create_class=block_create_class,
            branch=self
        )

    def _process_block_crud_response(self, block_crud_response: ApiResponse) -> Tuple[str, str]:
        block_id, block_data, block_group, action = parse_block_crud_response(
            block_crud_response
        )
        action = action.casefold()

        if action == CREATE.casefold():
            self.data[block_group][block_id] = block_data

        elif action == UPDATE.casefold():
            self.data[block_group][block_id].update(block_data)

        elif action == DELETE.casefold():
            del self.data[block_group][block_id]

        else:
            raise NotImplementedError(f'Unsupported action type: "{action}"')

        return block_id, block_group
