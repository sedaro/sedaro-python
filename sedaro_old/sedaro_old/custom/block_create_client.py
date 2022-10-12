from dataclasses import dataclass
from sedaro_old.api_client import Api
from typing import Dict
from .settings import CREATE


@dataclass
class BlockCreateClient:
    _block_snake_case: str
    _BlockCreate: type
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
        return getattr(self.block_open_api_instance, f'{CREATE}_{self._block_snake_case}')(
            body=self._BlockCreate(**body),
            **kwargs,
            path_params={'branchId': self._branch_id},
        )
