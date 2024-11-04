from typing import TYPE_CHECKING, Any

from sedaro_base_client.paths.models_branches_branch_id.get import SchemaFor200ResponseBodyApplicationJson

from ..settings import BLOCKS, RELATIONSHIPS, ROOT, TYPE
from ..utils import enforce_id_in_branch
from .blocks import Block, BlockType
from .common import Common

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class Branch(Common):
    _data: 'dict[str, Any]'
    id: 'str'
    """Branch `id`"""

    def __ingest_branch_res(self, branch_res_dict: dict):
        for k, v in branch_res_dict.items():
            k = '_data' if k == 'data' else k  # b/c `data` must be property overwriting abstract method of parent class
            setattr(self, k, v)

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        self.__ingest_branch_res(body)
        self._sedaro = sedaro

    def __str__(self):
        return f'{self.__class__.__name__}(id: {self.id}, name: "{self.name}")'

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, block_type_or_attr: str) -> BlockType | Any:

        if block_type_or_attr in self.data['_supers']:
            return BlockType(block_type_or_attr, self)

        try:
            return super().__getattr__(block_type_or_attr)
        except AttributeError:
            raise AttributeError(
                f'Unable to find an attribute or create a "{BlockType.__name__}" from string: "{block_type_or_attr}". Please check the name and try again.')

    @property
    def type(self) -> str:
        """`Metamodel` type of the branch"""
        return self.data[TYPE]

    @property
    def data(self) -> 'dict':
        return self._data

    @property
    def _branch(self) -> 'Branch':
        return self

    @property
    def _relationship_attrs(self) -> dict:
        return self.data[RELATIONSHIPS][ROOT]

    def crud(
        self,
        *,
        root: 'dict[str, Any]' = None,
        blocks: 'list[dict]' = None,
        delete: 'list[str]' = None
    ) -> 'dict':
        """Method to perform multiple CRUD operations at the same time.

        In this method, relationship fields can point at existing `BlockID`'s or "ref id"s. A "ref id" is similar to a
        json "reference" and is used as follows:
        - It is any string starting with `'$'`.
        - It must be in the `id` field of a single `Block` dictionary created in this transaction.
        - It can be referenced in any relationship field on root or any `Block` dictionary in this transaction.
        - All instances of the "ref id" will be resolved to the corresponding created `Block`'s id.

        Args:
            root (dict, optional): a `dict` of field/value pairs to update on the `root` of the branch template this\
                method is called on. Defaults to `None`.
            blocks (list, optional): a `list` of `Block` dictionaries. `Block` dictionaries with no `id` or a "ref id"\
                will be created, otherwise they should have an `id` field referencing an existing block and the\
                dictionary will be used to update the `Block`. Defaults to `None`.
            delete (list, optional): a list of `id`s of `Block`s to be deleted. Defaults to `None`.

        Raises:
            SedaroApiException: if there is an error in the response

        Returns:
            dict: the response dictionary from the request
        """
        root = {} if root is None else root
        blocks = [] if blocks is None else blocks
        delete = [] if delete is None else delete

        if not isinstance(root, dict):
            raise ValueError('The "root" arg must be an dictionary.')
        if not all(isinstance(el, list) for el in [blocks, delete]):
            raise ValueError('Each of the following args must be lists: "blocks" and "delete".')
        if blocks == [] and delete == [] and root == {}:
            raise ValueError(
                'Must provide at least one or more of the following args: "root" as a non-empty object, "blocks" and/or "delete" as non-empty arrays.')

        res = self._sedaro.request.patch(
            f'/models/branches/{self.id}/template/',
            {
                'root': root,
                'blocks': blocks,
                'delete': delete
            },
        )

        self.__ingest_branch_res(res['branch'])

        return res

    def block(self, id: str | int):
        """A general method to instantiate a `Block` object associated with the Sedaro Block of the given `id`. Use the
        `BlockType` properties on the Branch to instantiate `Block` objects narrowed to a specific type.

        Args:
            id (str | int): `id` of the desired Sedaro Block

        Raises:
            KeyError: if no corresponding Block exists in the Branch

        Returns:
            Block: a client to interact with the corresponding Sedaro Block
        """
        enforce_id_in_branch(self, id)
        return Block(
            id,
            getattr(self, self.data[BLOCKS][id][TYPE])
        )

    def update(
        self,
        blocks: 'list[dict]' = None,
        delete: 'list[str]' = None,
        include_response: 'bool' = False,
        **fields
    ) -> 'Branch':
        '''
        Method to perform updates to a model with support for bulk update operations.

        In this method, relationship fields can point at existing `BlockID`'s or "ref id"s. A "ref id" is similar to a
        json "reference" and is used as follows:
        - It is any string starting with `'$'`.
        - It must be in the `id` field of a single `Block` dictionary created in this transaction.
        - It can be referenced in any relationship field on root or any `Block` dictionary in this transaction.
        - All instances of the "ref id" will be resolved to the corresponding created `Block`'s id.

        Args:
            blocks (list, optional): a `list` of `Block` dictionaries. `Block` dictionaries with no `id` or a "ref id"\
                will be created, otherwise they should have an `id` field referencing an existing block and the\
                dictionary will be used to update the `Block`. Defaults to `None`.
            delete (list, optional): a list of `id`s of `Block`s to be deleted. Defaults to `None`.
            include_response (bool, optional): whether to return the response dictionary from the request. Defaults to `False`. `self` otherwise.
            **kwargs (dict, optional): field/value pairs to update on the `root` of the branch template this method is called on.

        Returns:
            Branch: updated `Branch` (Note: the previous `Branch` reference is also updated) if include_response is falsey, else the response dictionary
        '''

        res = self._branch.crud(root=fields, blocks=blocks, delete=delete)
        return self if not include_response else res
