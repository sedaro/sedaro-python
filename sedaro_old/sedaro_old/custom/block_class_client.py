from importlib import import_module
from dataclasses import dataclass
from sedaro_old.api_client import Api
from typing import TYPE_CHECKING, Dict, Literal, Union
from pydash.strings import snake_case


from .settings import CREATE, UPDATE, PACKAGE_NAME
from .block import Block
from .utils import get_snake_and_pascal_case

if TYPE_CHECKING:
    from .sedaro_api_client import SedaroApiClient
    from .branch import Branch


@dataclass
class BlockClassClient:
    '''Class for interacting with all Blocks of this class type'''
    block_name: str
    branch: 'Branch'

    def __str__(self) -> str:
        return f'BlockClassClient(block_name={self.block_name}, branch={self.branch.id})'

    @property
    def sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClassClient` was accessed through'''
        return self.branch.sedaro_client

    @property
    def create_class(self) -> type:  # FIXME
        '''The model class to instantiate with appropriate kwargs when creating a Sedaro Block'''
        return self._get_create_or_update_block_model(CREATE)

    @property
    def update_class(self) -> type:  # FIXME
        '''The model class to instantiate with appropriate kwargs when updating a Sedaro Block'''
        return self._get_create_or_update_block_model(UPDATE)

    @property
    def _block_openapi_instance(self) -> Api:
        '''The api instance instantiated with the appropriate `SedaroApiClient` to interact with when CRUDing Blocks'''
        block_snake, block_pascal = get_snake_and_pascal_case(self.block_name)
        block_api_module = import_module(f'{PACKAGE_NAME}.apis.tags.{block_snake}_api')
        return getattr(block_api_module, f'{block_pascal}Api')(self.sedaro_client)

    @property
    def block_group(self) -> str:
        '''The name of the Sedaro `BlockGroup` this type of `Block` is stored in'''
        return self.branch.data['blockToBlockGroupMapWithSuperBlockClasses'][self.block_name]

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

        block_snake, block_pascal = get_snake_and_pascal_case(self.block_name)

        crud_module_path = f'{PACKAGE_NAME}.model.{block_snake}'

        return getattr(
            import_module(f'{crud_module_path}_{create_or_update}'),
            f'{block_pascal}{create_or_update.capitalize()}'
        )

    def create(self, body: Dict, **kwargs) -> Dict:  # FIXME: return value
        """Creates a Sedaro `Block` of the given type in the Sedaro database.

        Args:
            body (Dict): a dictionary containing key/value pairs for the Sedaro `Block`

        Returns:
            _type_: _description_
            FIXME: ^^^^^^
        """
        res = getattr(self._block_openapi_instance, f'{CREATE}_{snake_case(self.block_name)}')(
            body=self.create_class(**body),
            **kwargs,
            path_params={'branchId': self.branch.id},
        )
        block_id = self.branch._process_block_crud_response(res)

        return Block(id=block_id, block_class_client=self)

    def get(self, id: Union[str, int]) -> Block:
        """Gets a `Block` from of the type of this `BlockClassClient`.

        Args:
            id (Union[str, int]): An integer or string version of the desired `Block` `id`.

        Raises:
            KeyError: if no corresponding `Block` exists.

        Returns:
            Block: the corresponding `Block`
        """
        if type(id) == int:
            id = str(id)

        if id not in self.branch.data[self.block_group]:
            raise KeyError(
                f'There is no {self.block_name} in the {self.block_group} BlockGroup with id {id}.')

        return Block(id=id, block_class_client=self)
