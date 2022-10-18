from importlib import import_module
from dataclasses import dataclass
from sedaro_base_client.api_client import Api
from typing import TYPE_CHECKING, Dict, Literal, Tuple, Union
from pydash.strings import snake_case
from functools import cached_property

from .settings import CREATE, UPDATE, BASE_PACKAGE_NAME
from .block_client import BlockClient
from .utils import get_snake_and_pascal_case

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient
    from .branch_client import BranchClient


@dataclass
class BlockClassClient:
    '''Class for interacting with all Blocks of this class type'''
    _block_name: str
    '''Name of the Sedaro Block class this `BlockClassClient` is set up to interact with'''
    _branch: 'BranchClient'
    '''The `Branch` this `BlockClassClient` is connected to'''

    def __str__(self) -> str:
        return f'BlockClassClient(block_name={self._block_name}, branch={self._branch.id})'

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClassClient` was accessed through'''
        return self._branch._sedaro_client

    @property
    def _create_class(self) -> type:  # FIXME
        '''The model class to instantiate with appropriate kwargs when creating a Sedaro Block'''
        return self._get_create_or_update_block_model(CREATE)

    @property
    def _update_class(self) -> type:  # FIXME
        '''The model class to instantiate with appropriate kwargs when updating a Sedaro Block'''
        return self._get_create_or_update_block_model(UPDATE)

    @property
    def _block_openapi_instance(self) -> Api:
        '''The api instance instantiated with the appropriate `SedaroApiClient` to interact with when CRUDing Blocks'''
        block_snake, block_pascal = get_snake_and_pascal_case(self._block_name)
        block_api_module = import_module(
            f'{BASE_PACKAGE_NAME}.apis.tags.{block_snake}_api')
        return getattr(block_api_module, f'{block_pascal}Api')(self._sedaro_client)

    @cached_property
    def _block_group(self) -> str:
        '''The name of the Sedaro `BlockGroup` this type of `Block` is stored in'''
        return self._branch._block_class_to_block_group_map[self._block_name]

        # Below can get block group if ever choose to not send blockClassToBlockGroupMap in response
        # PROPERTIES = 'properties'
        # REF = '$ref'
        # ANY_OF = 'anyOf'
        # ALL_OF = 'allOf'

        # block_group_type = None

        # # Traverse branch schema to figure out block group type, then traverse again to get matching block group
        # for k, v in self._branch.dataSchema['definitions'].items():
        #     # filter through all block group types
        #     if PROPERTIES in v and all(attr in v[PROPERTIES] for attr in ('name', 'collection', 'data')):
        #         # TODO: `if k.endswith('BG')` <-- evalutes to same as ^^^ if we always follow this convention for naming
        #         # block group classes. Would still like a safer way than either of these options though.
        #         blockClassOrClasses: Dict = v[PROPERTIES]['data']['additionalProperties']

        #         blockTypes = [blockClassOrClasses[REF]] if REF in blockClassOrClasses \
        #             else [v[REF] for v in blockClassOrClasses[ANY_OF]]

        #         if any(bT.endswith(self._block_name) for bT in blockTypes):
        #             block_group_type = k
        #             break

        # # check block group types (`bGT`) of all block groups to find which one matches `block_group_type`
        # for k, v in self._branch.dataSchema[PROPERTIES].items():
        #     if ALL_OF in v and any(bGT[REF].endswith(block_group_type) for bGT in v[ALL_OF]):
        #         return k

        # this shouldn't ever happen:
        # raise ValueError(
        #     f'Unable to find a block group containing the block name {self._block_name}')

    def _get_create_or_update_block_model(self, create_or_update: Literal['create', 'update']):
        """Gets the model class to used to validate the data to create or update a `Block`

        Args:
            create_or_update (Literal['create', 'update']): the action `'create'` or `'update'`

        Raises:
            ValueError: if you don't pass `'create'` or `'update'` for `create_or_update`

        Returns:
            _type_: _description_ FIXME
        """
        create_or_update = create_or_update.lower()
        if create_or_update not in [CREATE, UPDATE]:
            raise ValueError(
                "The create_or_update arg must be either a string of either 'create' or 'update'.")

        block_snake, block_pascal = get_snake_and_pascal_case(self._block_name)

        crud_module_path = f'{BASE_PACKAGE_NAME}.model.{block_snake}'

        return getattr(
            import_module(f'{crud_module_path}_{create_or_update}'),
            f'{block_pascal}{create_or_update.capitalize()}'
        )

    def create(self, timeout: Union[int, Tuple] = None, **body) -> BlockClient:
        """Creates a Sedaro `Block` of the given type in the Sedaro database.

        Args:
            timeout (Union[int, Tuple], optional): the timeout used by the rest client. Defaults to `None`.
            **body (any): all remaining kwargs form the `body`

        Returns:
            BlockClient: a client to interact with the created Sedaro Block
        """
        res = getattr(self._block_openapi_instance, f'{CREATE}_{snake_case(self._block_name)}')(
            body=self._create_class(**body),
            path_params={'branchId': self._branch.id},
            timeout=timeout
        )
        block_id = self._branch._process_block_crud_response(res)

        return BlockClient(id=block_id, _block_class_client=self)

    def get(self, id: Union[str, int]) -> BlockClient:
        """Gets a `BlockClient` from of the type of this `BlockClassClient`.

        Args:
            id (Union[str, int]): An integer or string version of the desired `Block` `id`.

        Raises:
            KeyError: if no corresponding `Block` exists.

        Returns:
            BlockClient: a client to interact with the corresponding Sedaro Block
        """
        if type(id) == int:
            id = str(id)

        if id not in self._branch.data[self._block_group]:
            raise KeyError(
                f'There is no {self._block_name} in the {self._block_group} BlockGroup with id {id}.')

        return BlockClient(id=id, _block_class_client=self)
