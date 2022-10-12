import json
from functools import cache
from pydash.strings import snake_case, pascal_case
from urllib3.response import HTTPResponse


@cache
def get_snake_and_pascal_case(s: str):
    '''Returns a tuple of the string in snake and pascal case'''
    return snake_case(s), pascal_case(s, strict=False)


def parse_urllib_response(response: HTTPResponse):
    return json.loads(response.data.decode('utf-8'))
