from typing import TYPE_CHECKING, Dict, Literal, Union, Tuple
from dataclasses import dataclass
from pydash import snake_case

from sedaro_base_client.api_client import Api
from .settings import UPDATE, DELETE
from .exceptions import NonexistantBlockError

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
        return f'\n{self._block_name}({attrs}\n)\n'

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, key: str) -> any:
        """Allows for dotting into the `BlockClient` to access keys on the referenced Sedaro Block

        Args:
            key (str): attribute being keyed into

        Raises:
            KeyError: if the attribute doesn't exist on the refrenced Sedaro Block

        Returns:
            any: the value of the corresponding attribute on the referenced Sedaro Block
        """
        if key not in self.data:
            raise make_key_error(key, self._block_name)
        return self.data[key]

    @property
    def data(self) -> Dict:
        '''The attributes of the corresponding Sedaro Block as a dictionary'''
        self.enforce_still_exists()
        return self._branch.data[self._block_group][self.id]

    @property
    def _block_name(self) -> str:
        '''The name of the Sedaro Block class associated with this `Block`'''
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

    def check_still_exists(self) -> bool:
        """Checks whether the Sedaro Block this `BlockClient` references still exists.

        Returns:
            bool: indication of whether or not the referenced Sedaro Block still exists
        """
        return self.id in self._branch.data[self._block_group]

    def enforce_still_exists(self) -> None:
        """Raises and error if the Sedaro Block this `BlockClient` references no longer exists.

        Raises:
            NonexistantBlockError: indication that the Block no longer exists.
        """
        if not self.check_still_exists():
            raise NonexistantBlockError(
                f'The referenced "{self._block_name}" (id: {self.id}) no longer exists.'
            )

    def update(self, timeout: Union[int, Tuple] = None, **attrs_to_update) -> 'BlockClient':
        """Update attributes of the corresponding Sedaro Block

        Args:
            timeout (Union[int, Tuple], optional): the timeout used by the rest client. Defaults to `None`.
            **attrs_to_update (Dict): all remaining kwargs form the `attrs_to_update` (attributes to update) on the Sedaro Block

        Returns:
            BlockClient: updated `BlockClient` (Note: the previous `BlockClient` reference is also updated)
        """
        # NOTE: `self.data` calls `self.enforce_still_exists()`, so don't need to call here
        body = self.data | attrs_to_update

        res = getattr(self._block_openapi_instance, f'{UPDATE}_{snake_case(self._block_name)}')(
            body=self._block_class_client._update_class(**body),
            path_params={
                'branchId': self._branch.id,
                'blockId': int(self.id)
            },
            timeout=timeout
        )
        self._branch._process_block_crud_response(res)
        return self

    def delete(self) -> str:
        """Deletes the associated Sedaro Block

        Returns:
            str: `id` of the deleted `Block`
        """
        self.enforce_still_exists()

        id = self.id
        res = getattr(self._block_openapi_instance, f'{DELETE}_{snake_case(self._block_name)}')(
            path_params={'branchId': self._branch.id, "blockId": int(id)}
        )
        return self._branch._process_block_crud_response(res)

    def is_rel_field(self, field: str) -> Union[str, Literal[False]]:
        """Checks if the given `field` is a relationship field on the associated Sedaro Block.

        Args:
            field (str): field to check

        Raises:
            TypeError: if the value of `field` is not a string
            KeyError: if the value of `field` does not correspond to any field on the associated Sedaro Block

        Returns:
            Union[str, Literal[False]]: `str` of the Block type the relationship field points to if `field` is a
            relationship field, otherwise `False`
        """
        if type(field) is not str:
            raise TypeError(
                f'The value of the "{field}" argument must be a string, not a {type(field).__name__}')

        properties = self._branch.data_schema['definitions'][self._block_name]['properties']

        if field not in properties:
            raise make_key_error(field, self._block_name)

        field_schema: dict = properties[field]

        title: str = field_schema.get('title')
        description: str = field_schema.get('description')
        # all rel fields have title and description
        if None in (title, description):
            return False

        # make sure is a rel field
        if not 'ID' in title and all(s in description for s in ['Relationship', '`', 'block', 'On delete']):
            return False

        return description.split('`')[1]


# Utils for this file only
def make_key_error(field: str, block_name: str) -> str:
    return KeyError(f'There is no "{field}" attribute on "{block_name}"')
