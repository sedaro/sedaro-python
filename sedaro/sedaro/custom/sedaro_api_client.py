from importlib import import_module
from pydash.strings import snake_case, pascal_case
# FIXME: figure out how to require pydash dynamically.

from sedaro.api_client import ApiClient
from .configuration import config
from sedaro.api_client import Api


class SedaroApiClient(ApiClient):
    def __init__(self, api_key, *args, **kwargs):
        return super().__init__(
            configuration=config,
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

    def get_block_api(self, block_name: str, temp=False) -> Api:
        """Returns the api instance associated with the block corresponding to the `block_name` passed in.

        Args:
            block_name (str): name of an official Sedaro `Block`. Can use any standard string case that can be parsed to
            pascal case (ie. `"BatteryCell"`, `"batteryCell"`, `"battery_cell"`, `"BATTERY_CELL"` all become
            `"BatteryCell"`).

        Returns:
            Api: the associated `Api` instance corresponding to the Sedaro `Block`
        """
        block_api_module = import_module(f'sedaro.apis.tags.{snake_case(block_name)}_api')
        return getattr(block_api_module, f'{pascal_case(block_name, strict=False)}Api')
