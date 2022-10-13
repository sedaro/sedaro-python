from importlib import import_module
from dataclasses import dataclass
from sedaro_old.api_client import Api
from typing import TYPE_CHECKING, Dict, Literal
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
    block_openapi_instance: Api
    branch: 'Branch'

    def __str__(self) -> str:
        return f'BlockClassClient(block_name={self.block_name}, branch={self.branch.id})'

    @property
    def sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClassClient` was accessed through'''
        return self.branch.sedaro_client

    @property
    def create_model(self) -> type:  # FIXME
        '''The model class to instantiate with appropriate kwargs when creating a Sedaro Block'''
        return self._get_create_or_update_block_model(self.block_name, CREATE)

    def _get_create_or_update_block_model(self, block_name: str, create_or_update: Literal['create', 'update']):
        """Gets the model class to used to validate the data to create or update a `Block`

        Args:
            block_name (str): name of an official Sedaro `Block`
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

        block_snake, block_pascal = get_snake_and_pascal_case(block_name)

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
        res = getattr(self.block_openapi_instance, f'{CREATE}_{snake_case(self.block_name)}')(
            body=self.create_model(**body),
            **kwargs,
            path_params={'branchId': self.branch.id},
        )
        block_id, block_group = self.branch._process_block_crud_response(res)
        return Block(
            id=block_id,
            block_class_client=self,
            block_group=block_group
        )
