from dataclasses import dataclass
from sedaro_old.api_client import Api
from typing import Dict
from pydash.strings import snake_case

from .settings import CREATE


@dataclass
class BlockGroupSingleClass:
    block_name: str
    block_openapi_instance: Api
    create_class: type
    branch_id: int

    def create(self, body: Dict, **kwargs) -> Dict:  # FIXME: return value
        """Creates a Sedaro `Block` of the given type in the Sedaro database.

        Args:
            body (Dict): a dictionary containing key/value pairs for the Sedaro `Block`

        Returns:
            _type_: _description_
            FIXME: ^^^^^^
        """
        return getattr(self.block_openapi_instance, f'{CREATE}_{snake_case(self.block_name)}')(
            body=self.create_class(**body),
            **kwargs,
            path_params={'branchId': self.branch_id},
        )
