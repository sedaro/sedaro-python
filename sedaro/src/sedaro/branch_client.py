from typing import TYPE_CHECKING, Dict, List, Union

from sedaro_base_client.api_client import ApiResponse
from sedaro_base_client.paths.models_branches_branch_id.get import SchemaFor200ResponseBodyApplicationJson
from .block_class_client import BlockClassClient
from .block_client import BlockClient
from .utils import (
    parse_block_crud_response,
    sanitize_and_enforce_id_in_branch,
    get_snake_and_pascal_case,
    import_if_exists,
    get_class_from_module
)
from .settings import BASE_PACKAGE_NAME

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

    def __getattr__(self, block_type: str) -> BlockClassClient:
        block_snake, block_pascal = get_snake_and_pascal_case(block_type)

        # Valid block class client options that don't have an associated api (won't have a create method)
        bcc_options_without_api = {'ConOps'}
        if block_type in bcc_options_without_api:
            return BlockClassClient(block_pascal, None, self)

        # check if is a valid option for creating a BlockClassClient & get respective api module file
        block_api_module = import_if_exists(
            f'{BASE_PACKAGE_NAME}.apis.tags.{block_snake}_api'
        )

        # Note: use `casefold` due to things like `GpsAlgorithm` vs `GPSAlgorithm`
        block_options = set(b.casefold() for b in self._block_class_to_block_group_map) | \
            {'ConstantLoad'.casefold(), 'Surface'.casefold()}
        # Note: these blocks ^^^ added in manually, b/c aren't in the BG's but are valid block class clients

        if block_type.casefold() not in block_options or block_api_module is None:
            raise AttributeError(
                f'Unable to create a "BlockClassClient" from string: "{block_type}". Please check the name and try again.'
            )

        block_api_class = get_class_from_module(block_api_module)

        return BlockClassClient(block_pascal, block_api_class(self._sedaro_client), self)

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

        # first try with block_type, then try with block_group
        block_type = self._block_id_to_type_map[id]
        try:
            b_c_c: BlockClassClient = getattr(self, block_type)
        except AttributeError as e:
            block_group = self._block_class_to_block_group_map[block_type]
            try:
                b_c_c = BlockClassClient = getattr(self, block_group)
            except AttributeError:
                raise e
        return BlockClient(id, b_c_c)

# TODO: add a method for just sending any request with a URL.
