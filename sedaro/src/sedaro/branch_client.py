import importlib
from typing import TYPE_CHECKING, Dict, List
from dataclasses import dataclass
from pydash import snake_case, pascal_case

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
    data_schema: Dict
    _sedaro_client: 'SedaroApiClient'
    _block_id_to_type_map: Dict[str, str]
    '''Dicationary mapping Sedaro Block ids to the class name of the Block'''
    _block_class_to_block_group_map: Dict[str, str]
    '''Dictionary mapping Block class names to the Sedaro Block Group they are in'''
    _block_group_names: List[str]

    def __str__(self):
        return f'BranchClient(id: {self.id})'

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, block_name: str) -> BlockClassClient:
        block_class_module = f'{BASE_PACKAGE_NAME}.model.{snake_case(block_name)}'
        if importlib.util.find_spec(block_class_module) is None:
            raise AttributeError(
                f'Unable to find a Sedaro Block called: "{block_name}". Please check the name and try again.')

        return BlockClassClient(pascal_case(block_name, strict=False), self)

    def _process_block_crud_response(self, block_crud_response: ApiResponse) -> str:
        """Updates the local `Branch` data according to the CRUD action completed

        Args:
            block_crud_response (ApiResponse): response from a Sedaro Block CRUD action

        Raises:
            NotImplementedError: if the returned CRUD action isn't create, update, or delete

        Returns:
            str: `block_id`
        """
        block_id, block_data, block_group, action, branch_data_incoming, block_id_to_type_map = parse_block_crud_response(
            block_crud_response
        )

        self._block_id_to_type_map = block_id_to_type_map
        branch_data_local = self.data

        # Handle CRUD-ed block
        action = action.casefold()
        if action == CREATE.casefold():
            branch_data_local[block_group][block_id] = block_data

        elif action == UPDATE.casefold():
            branch_data_local[block_group][block_id].update(block_data)

        elif action == DELETE.casefold():
            del branch_data_local[block_group][block_id]

        else:
            raise NotImplementedError(f'Unsupported action type: "{action}"')

        # Loop through all blocks in all block groups
        # -- to deal with cascade deletes, and updates of blocks on other side of relationships
        for b_g in self._block_group_names:
            b_g_incoming = branch_data_incoming[b_g]
            b_g_local = branch_data_local[b_g]

            for id_local, block_data_local in list(b_g_local.items()):

                # Skip block that's already been handled above
                if id_local == block_id:
                    continue

                # Remove block if doesn't exist
                if id_local not in b_g_incoming:
                    del b_g_local[id_local]
                    continue

                # Update block if has changed
                block_data_incoming = b_g_incoming[id_local]
                if block_data_local != block_data_incoming:

                    # delete any keys from local not in incoming
                    for key in list(block_data_local.keys()):
                        if key not in block_data_incoming:
                            del block_data_local[key]

                    # update all key/vals
                    block_data_local.update(block_data_incoming)

            # Add any tangential "auto-created" blocks during the CRUD-ing of this block
            new_ids = set(b_g_incoming.keys()) - set(b_g_local.keys())
            for new_id in new_ids:
                block_data_local[new_id] = block_data_incoming[new_id]

        return block_id
