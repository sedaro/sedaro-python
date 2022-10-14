import importlib
from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass
from pydash import snake_case

from sedaro_base_client.api_client import ApiResponse
from .block_class_client import BlockClassClient
from .utils import parse_block_crud_response
from .settings import CREATE, UPDATE, DELETE, BASE_PACKAGE_NAME

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


@dataclass
class BranchClient:
    id: int
    data: Dict
    dataSchema: Dict
    _sedaro_client: 'SedaroApiClient'

    def __str__(self):
        return f'Branch(id: {self.id})'

    def __getattr__(self, block_name: str) -> BlockClassClient:
        block_class_module = f'{BASE_PACKAGE_NAME}.model.{snake_case(block_name)}'
        if importlib.util.find_spec(block_class_module) is None:
            raise AttributeError(
                f'Unable to find a Sedaro Block called: "{block_name}". Please check the name and try again.')

        return BlockClassClient(
            _block_name=block_name,
            _branch=self
        )

    def _process_block_crud_response(self, block_crud_response: ApiResponse) -> str:
        """Updates the local `Branch` data according to the CRUD action completed

        Args:
            block_crud_response (ApiResponse): response from a Sedaro Block CRUD action

        Raises:
            NotImplementedError: if the returned CRUD action isn't create, update, or delete

        Returns:
            str: `block_id`
        """
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

        return block_id
