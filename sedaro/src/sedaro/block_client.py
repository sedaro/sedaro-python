from functools import lru_cache
from typing import TYPE_CHECKING, Dict, Union, Tuple
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
                # TODO: this is often not True when it should be b/c so many values become the `DynamicSchema` class
                # Figure out how to fix this
                v = f"'{v}'"
            attrs += f'\n   {k}={v}'
        return f'\n{self._block_name}({attrs}\n)\n'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self):
        # allows a BlockClient to be a key in a dict and @lru_cache wrapper to work on methods on this class
        return hash(self.__class__.__name__ + self.id)

    def __getattr__(self, key: str) -> any:
        """Allows for dotting into the `BlockClient` to access keys on the referenced Sedaro Block. Additionally, makes
        it so dotting into relationship fields returns `BlockClient`s corresponding to the related Sedaro Blocks.

        Args:
            key (str): attribute being keyed into

        Raises:
            AttributeError: if the attribute doesn't exist on the refrenced Sedaro Block

        Returns:
            any: the value of the corresponding attribute on the referenced Sedaro Block
        """
        if key not in self.data:
            raise make_attr_error(key, self._block_name)

        val = self.data[key]

        if not self.is_rel_field(key) or val in (None, [], {}):
            return val

        side_type = self.get_rel_field_type(key)
        branch_client = self._branch_client

        if side_type == MANY_SIDE:
            return [branch_client.get_block_client(id) for id in val]

        if side_type == MANY_SIDE_DATA:
            return {branch_client.get_block_client(id): data for id, data in val.items()}

        if side_type == ONE_SIDE:
            return branch_client.get_block_client(val)

        # TODO: wasn't able to use this below, because the types are sometimes of DynamicSchema and not the actual
        # primitive types... Need to figure this out.
        # if isinstance(val, list):
        #     return [branch_client.get_block_client(id) for id in val]

        # if isinstance(val, dict):
        #     return {branch_client.get_block_client(id): data for id, data in val.items()}

        # if isinstance(val, str):
        #     return branch_client.get_block_client(val)

        raise NotImplementedError(
            f'Unsupported relationship type on "{self._block_name}", attribute: "{key}".'
        )

    @property
    def data(self) -> Dict:
        '''The properties of the corresponding Sedaro Block as a dictionary'''
        self.enforce_still_exists()
        return self._branch_client.data[self._block_group][self.id]

    @property
    def _block_name(self) -> str:
        '''The name of the Sedaro Block class associated with this `BlockClient`'''
        try:
            # NOTE: can't use `check_still_exists` instead of try/except, b/c that method calls this one
            return self._branch_client._block_id_to_type_map[self.id]
        except KeyError:
            # this won't be as specific, but allows to know at least the parent type even after a block was deleted
            return self._block_class_client._block_name

    @property
    def _block_group(self) -> str:
        '''The name of the Sedaro Block Group this type of `BlockClient`'s associated Sedaro Block is stored in'''
        return self._branch_client._block_class_to_block_group_map[self._block_name]

    @property
    def _branch_client(self) -> 'BranchClient':
        '''The `BranchClient` this `BlockClient` is connected to'''
        return self._block_class_client._branch_client

    @property
    def _block_openapi_instance(self) -> Api:
        '''The api instance instantiated with the appropriate `SedaroApiClient` to interact with when CRUDing Blocks'''
        return self._block_class_client._block_openapi_instance

    @property
    def _sedaro_client(self) -> 'SedaroApiClient':
        '''The `SedaroApiClient` this `BlockClient` was accessed through'''
        return self._branch_client._sedaro_client

    def check_still_exists(self) -> bool:
        """Checks whether the Sedaro Block this `BlockClient` references still exists.

        Returns:
            bool: indication of whether or not the referenced Sedaro Block still exists
        """
        return self.id in self._branch_client.data[self._block_group]

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
            timeout (Union[int, Tuple], optional): the timeout used by the REST client. Defaults to `None`.
            **attrs_to_update (Dict): desired attributes to update on the Sedaro Block

        Returns:
            BlockClient: updated `BlockClient` (Note: the previous `BlockClient` reference is also updated)
        """
        # NOTE: `self.data` calls `self.enforce_still_exists()`, so don't need to call here
        body = self.data | attrs_to_update

        res = getattr(self._block_openapi_instance, f'{UPDATE}_{snake_case(self._block_name)}')(
            body=self._block_class_client._update_class(**body),
            path_params={
                'branchId': self._branch_client.id,
                'blockId': int(self.id)
            },
            timeout=timeout
        )
        self._branch_client._process_block_crud_response(res)
        return self

    def delete(self) -> str:
        """Deletes the associated Sedaro Block

        Returns:
            str: `id` of the deleted Sedaro Block
        """
        self.enforce_still_exists()

        id = self.id
        res = getattr(self._block_openapi_instance, f'{DELETE}_{snake_case(self._block_name)}')(
            path_params={
                'branchId': self._branch_client.id,
                "blockId": int(id)
            }
        )
        return self._branch_client._process_block_crud_response(res)

    def get_schema(self) -> dict:
        """Gets the schema for the associated Sedaro Block type

        Returns:
            dict: the associated Block's schema
        """
        return self._branch_client.data_schema['definitions'][self._block_name]

    @lru_cache(maxsize=None)
    def get_field_schema(self, field: str) -> dict:
        """Gets the field schema of the corresponding attribute on the Sedaro Block.

        Args:
            field (str): field to get the schema for

        Raises:
            TypeError: if the value of `field` is not a string
            AttributeError: if the value of `field` does not correspond to any field on the associated Sedaro Block

        Returns:
            dict: the field schema
        """
        if type(field) is not str:
            raise TypeError(
                f'The value of the "{field}" argument must be a string, not a {type(field).__name__}')

        properties = self.get_schema()['properties']

        if field not in properties:
            raise make_attr_error(field, self._block_name)

        return properties[field]

    @lru_cache(maxsize=None)
    def is_rel_field(self, field: str) -> bool:
        """Checks if the given `field` is a relationship field on the associated Sedaro Block.

        Args:
            field (str): field to check

        Raises:
            TypeError: if the value of `field` is not a string
            KeyError: if the value of `field` does not correspond to any field on the associated Sedaro Block

        Returns:
            bool: indicates if the given `field` is a relationship field on the Sedaro Block or not.
        """
        field_schema = self.get_field_schema(field)

        title: str = field_schema.get('title')
        description: str = field_schema.get('description')

        # all rel fields have a title and description
        if None in (title, description):
            return False

        # all rel fields have these strings in title and description
        return 'ID' in title and all(s in description for s in ['Relationship', '`', 'block', 'On delete'])

    def get_rel_field_type(self, field: str) -> str:
        """Get the type of relationship of the field. Note: first call `is_rel_field` if you need to confirm `field` is
        a relationship field.

        Args:
            field (str): the field to get the relationship type for

        Raises:
            TypeError: if the value of `field` is not a string or not a relationship field on this type of Sedaro Block
            KeyError: if the value of `field` does not correspond to any field on the associated Sedaro Block
            NotImplementedError: if the relationship type is not able to be parsed from the field schema

        Returns:
            str: a string indicating the type of relationship field
        """
        if not self.is_rel_field(field):
            raise TypeError(
                f'The given field "{field}" is not a relationship field on "{self._block_name}".')

        description: str = self.get_field_schema(field).get('description')

        # NOTE: order of if statements matters
        if 'with data to one or more' in description:
            return MANY_SIDE_DATA

        if 'to one or more' in description:
            return MANY_SIDE

        if any(s in description for s in ['to a', 'to zero or one']):
            return ONE_SIDE

        raise NotImplementedError(
            f'Unsupported relationship type on "{self._block_name}", attribute: "{field}".'
        )


# ------ helper function and vars for this file only ------
MANY_SIDE = 'many-side'
MANY_SIDE_DATA = 'many-side-with-data'
ONE_SIDE = 'one-side'


def make_attr_error(field: str, block_name: str) -> str:
    return AttributeError(f'There is no "{field}" attribute on "{block_name}"')
