import importlib
from typing import TYPE_CHECKING, Dict, List, Union
from dataclasses import dataclass
from pydash import snake_case, pascal_case

from sedaro_base_client.api_client import ApiResponse
from sedaro_base_client.paths.models_branches_branch_id.get import SchemaFor200ResponseBodyApplicationJson
from .block_class_client import BlockClassClient
from .block_client import BlockClient
from .utils import parse_block_crud_response, sanitize_and_enforce_id_in_branch
from .settings import CREATE, UPDATE, DELETE, BASE_PACKAGE_NAME

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient


class BranchClient:

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, client: 'SedaroApiClient'):
        for k, v in body.items():
            setattr(self, k, v)
        self.data_schema: Dict = body['dataSchema']
        self._sedaro_client = client
        self._block_id_to_type_map: Dict[str, str] = body['blockIdToTypeMap']
        '''Dictionary mapping Sedaro Block ids to the class name of the Block'''
        self._block_class_to_block_group_map: Dict[str,
                                                   str] = body['blockClassToBlockGroupMap']
        '''Dictionary mapping Block class names to the Sedaro Block Group they are in'''
        self._block_group_names: List[str] = body['blockGroupNames']

    def __str__(self):
        return f'BranchClient(id: {self.id}, name: "{self.name}")'

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, block_name: str) -> BlockClassClient:
        if block_name not in self._block_class_to_block_group_map:
            raise AttributeError(
                f'Attribute `{block_name}` does not exist on {self}')
        block_class_module = f'{BASE_PACKAGE_NAME}.model.{snake_case(block_name)}'
        if importlib.util.find_spec(block_class_module) is None:
            raise AttributeError(
                f'Unable to find a Sedaro Block called: "{block_name}" in order to create an associated "BlockClassClient". Please check the name and try again.')

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
        self.data = branch_data_incoming

        return block_id

    def get_block_client(self, id: Union[str, int]):
        """Gets a `BlockClient` associated with the Sedaro Block of the given `id`.

        Args:
            id (Union[str, int]): `id` of the desired Sedaro Block

        Raises:
            TypeError: if the `id` is not an integer or an integer string
            KeyError: if no corresponding Block exists in the Branch

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        id = sanitize_and_enforce_id_in_branch(self, id)

        b_c_c: BlockClassClient = getattr(self, self._block_id_to_type_map[id])
        return BlockClient(id, b_c_c)

# TODO: add a method for just sending any request with a URL.
