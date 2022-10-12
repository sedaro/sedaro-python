import json
from functools import cache
from pydash.strings import snake_case, pascal_case
from urllib3.response import HTTPResponse
from typing import Dict, Tuple
from sedaro_old.api_client import ApiResponse


@cache
def get_snake_and_pascal_case(s: str):
    '''Returns a tuple of the string in snake and pascal case'''
    return snake_case(s), pascal_case(s, strict=False)


def parse_urllib_response(response: HTTPResponse) -> Dict:
    '''Parses the response from urllib3.response.HTTPResponse into a dictionary'''
    return json.loads(response.data.decode('utf-8'))


def parse_block_crud_response(response: ApiResponse) -> Tuple:
    """Parses the response of CRUD-ing a Sedaro Block on a `Branch` into a dictionary.

    Args:
        response (ApiResponse): the response from CRUD-ing a Sedaro Block

    Returns:
        Dict: a tuple of: `block_id`, `block_data`, `block_group`, `branch_data`, `action`
    """
    body = response.body
    block_id, block_group = body['block']['id'], body['block']['group']
    branch_data = body['branch']['data']

    return block_id, branch_data[block_group][block_id], block_group, branch_data, body['action']
