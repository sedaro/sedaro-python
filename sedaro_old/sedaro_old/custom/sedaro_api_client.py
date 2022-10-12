from importlib import import_module
from typing import Literal
# FIXME: figure out how to require pydash dynamically.

from sedaro_old.api_client import ApiClient
from sedaro_old.api_client import Api
from .configuration import config
from .utils import get_snake_and_pascal_case, parse_urllib_response
from .settings import PACKAGE_NAME, CREATE, UPDATE
from .branch import Branch


class SedaroApiClient(ApiClient):
    def __init__(self, api_key, *args, **kwargs):
        return super().__init__(
            configuration=config,
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

    def get_branch(self, branch_id: int) -> Branch:
        """Gets a Sedaro Branch based on the give `branch_id`. Must be accessible to this `SedaroApiClient` via the
        `api_key`.

        Args:
            branch_id (int): the id of the desired Sedaro Branch

        Returns:
            Branch: A `Branch` object that has various helpful methods on it.
        """
        res = self.call_api(f'/models/branches/{branch_id}', 'GET')
        return Branch(
            id=branch_id,
            data=parse_urllib_response(res)['data'],
            sedaro_client=self
        )

    def _get_block_open_api_instance(self, block_name: str) -> Api:
        """Get a open api block api instance that can be used to call various methods.

        Args:
            block_name (str): name of an official Sedaro `Block`

        Returns:
            Api: The corresponding block api instance instantiated with the Sedaro client passed in.
        """
        block_snake, block_pascal = get_snake_and_pascal_case(block_name)
        block_api_module = import_module(f'{PACKAGE_NAME}.apis.tags.{block_snake}_api')
        return getattr(block_api_module, f'{block_pascal}Api')(self)

    def _get_create_or_update_block_model(self, block_name: str, create_or_update: Literal['create', 'update']):
        """Gets the class to used to validate the data to create or update a `Block` 

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
