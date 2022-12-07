import json
import importlib
from functools import lru_cache
from pydash.strings import snake_case, pascal_case
from urllib3.response import HTTPResponse
from typing import Dict, Tuple, Union, TYPE_CHECKING

from sedaro_base_client.api_client import ApiResponse
from .settings import DELETE

if TYPE_CHECKING:
    from .branch_client import BranchClient


@lru_cache(maxsize=None)
def get_snake_and_pascal_case(s: str):
    '''Returns a tuple of the string in snake and pascal case'''
    return snake_case(s), pascal_case(s, strict=False)


def parse_urllib_response(response: HTTPResponse) -> Dict:
    '''Parses the response from urllib3.response.HTTPResponse into a dictionary'''
    return json.loads(response.data.decode('utf-8'))


def parse_block_crud_response(response: ApiResponse) -> Tuple[str, dict, str, str]:
    """Parses the response of CRUD-ing a Sedaro Block on a `Branch` into a tuple.

    Args:
        response (ApiResponse): the response from CRUD-ing a Sedaro Block

    Returns:
        Dict: a tuple of: `block_id`, `block_data`, `block_group`, `action`, `branch_data`, `block_id_to_type_map`
    """
    body = response.body
    action = body['action']
    block_id = str(body['block']['id'])
    block_group = body['block']['group']
    branch_data = body['branch']['data']

    block_data = dict(branch_data[block_group][block_id]) if action.casefold() != DELETE.casefold() \
        else None

    return block_id, block_data, block_group, action, branch_data, body['branch']['blockIdToTypeMap']


def sanitize_and_enforce_id_in_branch(branch_client: 'BranchClient', id: Union[str, int]):
    """Makes sure `id` is of the right type and exists in the Sedaro Branch associated with the `BranchClient`

    Args:
        branch_client (BranchClient): the `BranchClient` associated with the Sedaro Branch to check for the `id`
        id (Union[str, int]): `id` of the Sedaro Block to sanitize and check

    Raises:
        TypeError: if the `id` is not an integer or an integer string
        KeyError: if no corresponding Block exists in the Branch

    Returns:
        str: the integer string `id` of the Block
    """
    try:
        og_id = id
        id = str(id)
        assert id.isdigit()
    except:
        raise TypeError(
            f'The "id" argument must be a string of an integer or able to be coerced to such, not a "{type(og_id).__name__}".'
        )

    if id not in branch_client._block_id_to_type_map:
        raise KeyError(f'There is no Block with id "{id}" in this Branch.')

    return id


def import_if_exists(local_path: str):
    """Returns local import if exists, otherwise `None`

    Args:
        path (str): path to desired import

    Returns:
        import or `None`
    """
    if importlib.util.find_spec(local_path) is None:
        return None
    return importlib.import_module(local_path)
