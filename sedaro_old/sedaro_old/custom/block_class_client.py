from dataclasses import dataclass
from sedaro_old.api_client import Api
from typing import TYPE_CHECKING, Dict
from pydash.strings import snake_case

from .settings import CREATE
from .block import Block

if TYPE_CHECKING:
    from .branch import Branch


@dataclass
class BlockClassClient:
    '''Class for interacting with all Blocks of this class type'''
    block_name: str
    block_openapi_instance: Api
    create_class: type
    branch: 'Branch'

    def __str__(self) -> str:
        return f'BlockClassClient(block_name={self.block_name}, branch={self.branch.id})'

    def create(self, body: Dict, **kwargs) -> Dict:  # FIXME: return value
        """Creates a Sedaro `Block` of the given type in the Sedaro database.

        Args:
            body (Dict): a dictionary containing key/value pairs for the Sedaro `Block`

        Returns:
            _type_: _description_
            FIXME: ^^^^^^
        """
        res = getattr(self.block_openapi_instance, f'{CREATE}_{snake_case(self.block_name)}')(
            body=self.create_class(**body),
            **kwargs,
            path_params={'branchId': self.branch.id},
        )
        body = res.body
        block_id, block_group = body['block']['id'], body['block']['group']
        block_data = body['branch']['data'][block_group][block_id]
        return Block(
            id=block_id,
            data=block_data,
            block_group_single_class=self,
            block_group=block_group
        )
