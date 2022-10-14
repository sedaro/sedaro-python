from typing import TYPE_CHECKING, Dict
from dataclasses import dataclass
from pydash import snake_case

from sedaro_base_client.api_client import Api
from .settings import UPDATE, DELETE

if TYPE_CHECKING:
    from .block_class_client import BlockClassClient
    from .sedaro_api_client import SedaroApiClient
    from .branch_client import BranchClient


@dataclass
class BlockClient:
    id: str
    _block_class_client: 'BlockClassClient'
    '''Class for interacting with all Blocks of this class type'''

    def __str__(self) -> str:
        attrs = ''
        for k, v in self.data.items():
            if type(v) is str:
                # FIXME: figure out why we don't know when something is a string, it's this `DynamicSchema` class
                v = f"'{v}'"
            attrs += f'\n   {k}={v}'
        return f'\n{self._name}({attrs}\n)\n'

    def __getattr__(self, key) -> any:
        return self.data[key]

    @property
    def data(self) -> Dict:
        try:
            return self._branch.data[self._block_group][self.id]
        except KeyError as e:
            # if it's KeyError of a string id (block doesn't exist), str(e) is like this: "'1234'"
            if str(e).replace("'", '').isdigit():
                raise KeyError('The referenced Sedaro Block no longer exists.')
            raise e

    @property
    def _name(self) -> str:
        '''The name of the class associated with this `Block`'''
        return self._block_class_client._block_name

    @property
    def _block_group(self) -> str:
        '''The name of the Sedaro `BlockGroup` this type of `Block` is stored in'''
        return self._block_class_client._block_group

    @property
    def _branch(self) -> 'BranchClient':
        '''The `Branch` this `Block` is connected to'''
        return self._block_class_client._branch

    @property
    def _block_openapi_instance(self) -> Api:
        '''The api instance instantiated with the appropriate `SedaroApiClient` to interact with when CRUDing Blocks'''
        return self._block_class_client._block_openapi_instance

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `Block` was accessed through'''
        return self._branch._sedaro_client

    def update(self, body: Dict, **kwargs) -> 'BlockClient':
        """Update attributes of the `Block`

        Args:
            body (Dict): dictionary of attributes to update

        Returns:
            Block: updated version of self (previous reference's data is also updated)
        """
        body = self.data | body

        res = getattr(self._block_openapi_instance, f'{UPDATE}_{snake_case(self._name)}')(
            body=self._block_class_client._update_class(**body),
            **kwargs,
            path_params={'branchId': self._branch.id, "blockId": int(self.id)},
        )
        self._branch._process_block_crud_response(res)
        return self

    def delete(self) -> str:
        """Deletes the associated Sedaro Block from the Sedaro database.

        Returns:
            str: `id` of the deleted `Block`
        """
        id = self.id
        res = getattr(self._block_openapi_instance, f'{DELETE}_{snake_case(self._name)}')(
            path_params={'branchId': self._branch.id, "blockId": int(id)}
        )
        return self._branch._process_block_crud_response(res)
