from importlib import import_module
from dataclasses import dataclass
from typing import Dict
from pydash.strings import snake_case, pascal_case
# FIXME: figure out how to require pydash dynamically.

from sedaro_base_client import ApiClient
from .configuration import config
from sedaro_base_client import Api

PACKAGE_NAME = 'sedaro'


@dataclass
class BlockClient:
    _block_snake_case: str
    _BlockCreate: type
    _BlockUpdate: type
    _branch_id: int
    block_open_api_instance: Api

    def create(self, body: Dict, **kwargs) -> Dict:  # FIXME: return value
        """Creates a Sedaro `Block` of the given type in the Sedaro database.

        Args:
            body (Dict): a dictionary containing key/value pairs for the Sedaro `Block`

        Returns:
            _type_: _description_
            FIXME: ^^^^^^
        """
        return getattr(self.block_open_api_instance, f'create_{self._block_snake_case}')(
            body=self._BlockCreate(**body),
            **kwargs,
            path_params={'branchId': self._branch_id},
        )

    def update(self, block_id: str, body: Dict, **kwargs) -> Dict:  # FIXME: return value
        """_summary_

        Args:
            block_id (str): `id` of the Sedaro `Block` to update
            body (Dict): a dictionary containing key/value pairs to update on the Sedaro `Block`

        Returns:
            _type_: _description_
            FIXME: ^^^^^^
        """
        return getattr(self.block_open_api_instance, f'update_{self._block_snake_case}')(
            body=self._BlockUpdate(**body),
            **kwargs,
            path_params={'branchId': self._branch_id, 'blockId': block_id},
        )


class SedaroApiClient(ApiClient):
    def __init__(self, api_key, *args, **kwargs):
        return super().__init__(
            configuration=config,
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

    def get_block_client(self, branch_id: int, block_name: str) -> BlockClient:
        """Returns the api instance associated with the block corresponding to the `block_name` passed in.

        Args:
            branch_id (int): id of the Sedaro `Branch` to interact with
            block_name (str): name of an official Sedaro `Block`. Can use any standard string case that can be parsed to
            pascal case (ie. `"BatteryCell"`, `"batteryCell"`, `"battery_cell"`, `"BATTERY_CELL"` all become
            `"BatteryCell"`).

        Returns:
            Api: the associated `Api` instance corresponding to the Sedaro `Block`
        """
        block_snake_case = snake_case(block_name)
        block_pascal_case = pascal_case(block_name, strict=False)

        block_api_module = import_module(
            f'{PACKAGE_NAME}.apis.tags.{block_snake_case}_api')
        block_open_api_instance: Api = getattr(
            block_api_module, f'{block_pascal_case}Api')(self)

        crud_module_path = f'{PACKAGE_NAME}.model.{block_snake_case}'

        BlockCreate = getattr(
            import_module(f'{crud_module_path}_create'),
            f'{block_pascal_case}Create'
        )
        BlockUpdate = getattr(
            import_module(f'{crud_module_path}_update'),
            f'{block_pascal_case}Update'
        )

        return BlockClient(
            _block_snake_case=block_snake_case,
            _BlockCreate=BlockCreate,
            _BlockUpdate=BlockUpdate,
            _branch_id=branch_id,
            block_open_api_instance=block_open_api_instance
        )
