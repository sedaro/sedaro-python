import importlib
import inspect
import json
import re
from types import ModuleType
from typing import TYPE_CHECKING, Union

import orjson
from urllib3.response import HTTPResponse

from .data_utils import concat_results, update_metadata
from .exceptions import SedaroApiException
from .settings import BLOCKS, COMMON_API_KWARGS, STATUS

if TYPE_CHECKING:
    from sedaro_base_client.api_client import ApiResponseWithoutDeserialization

    from .branches.branch import Branch


def serdes(v):
    import numpy as np
    if type(v) is dict and 'ndarray' in v:
        return np.array(v['ndarray'])
    if type(v) is np.ndarray:
        return {'ndarray': v.tolist()}
    if type(v) is dict:
        return {k: serdes(v) for k, v in v.items()}
    if type(v) in {list, tuple}:
        return [serdes(v) for v in v]
    return v


def is_likely_html(content: str) -> bool:
    """Check if the given content (str) is likely HTML."""
    return content.lstrip().lower().startswith('<!doctype html') or re.search(r'<html\b', content, re.IGNORECASE)


def parse_urllib_response(response: "HTTPResponse") -> "Union[dict, list[dict]]":
    '''Parses a json response from urllib3.response.HTTPResponse into a dictionary or list'''
    data = response.data
    try:
        return orjson.loads(data)
    except:
        if not data:
            raise SedaroApiException(status=response.status, reason="Empty response cannot be parsed as JSON")
        try:
            data = data.decode('utf-8')
        except UnicodeDecodeError:
            raise SedaroApiException(status=response.status, reason=f"Binary data cannot be parsed as JSON")
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            if is_likely_html(data):  # not parsable and looks like html
                max_len = 1_000
                preview = data[:max_len] + "...\n\n(long html truncated)" if len(data) > max_len else data
                data = f"HTML content detected. This may indicate a proxy, firewall, or server error page.\n\n{preview}"
            raise SedaroApiException(
                status=response.status,
                reason=f"Failed to parse response as JSON: {e}\n\nResponse content:\n\n{data}"
            ) from e


def check_for_res_error(response: 'dict'):
    """Checks for an 'error' key in the response dictionary and raises that error if present.

    Args:
        response (dict): response from an api request after parse_urllib_response

    Raises:
        SedaroApiException: if error present
    """
    if not isinstance(response, dict):
        return
    err = response.get('error', None)
    if err is not None:
        raise SedaroApiException(status=err[STATUS], reason=f"{err['code']}: {err['message']}")


def enforce_id_in_branch(branch: 'Branch', id: str):
    """Makes sure `id` exists in the Sedaro Branch associated with the `Branch`

    Args:
        branch (Branch): the `Branch` instance associated with the Sedaro Branch to check for the `id`
        id (str): `id` of the Sedaro Block to sanitize and check

    Raises:
        KeyError: if no corresponding Block exists in the Branch
    """
    if id not in branch.data[BLOCKS]:
        raise KeyError(f'There is no Block with id "{id}" in this Branch.')


def body_from_res(res: "ApiResponseWithoutDeserialization"):
    """
    Returns `res.body` unless `skip_deserialization` is true, then parses body from `res.response` Should be used when
    `COMMON_API_KWARGS` is spread in auto-generated HTTP request methods.
    """
    return parse_urllib_response(res.response) if COMMON_API_KWARGS['skip_deserialization'] else res.body


def progress_bar(progress):
    """Prints a progress bar to the console"""
    if progress is not None:
        blocks = int(progress * 50 / 100)
        bar = '[' + ('■' * blocks + '□'*(50 - blocks)).ljust(50) + f'] ({progress:.2f}%)'
        print(bar, end='\r')


# ======================================================================================================================
# Below were used in the past and may be helpful in the future
# ======================================================================================================================

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


def get_class_from_module(module: ModuleType, target_class: str = None) -> type:
    """Gets a class from the passed in module.

    Args:
        module (ModuleType): python module (file)
        target_class (str, optional): name of the class to search for. Defaults to None.

    Raises:
        AttributeError: if no class is found to return

    Returns:
        type: If `target_class` not provided, returns first class defined in the module. If `target_class`
        is provided, returns class with a matching name (case-insensitive).
    """

    def filter_desired_class_from_file(kls):
        if not inspect.isclass(kls):
            return False
        if target_class is not None:
            return kls.__name__.casefold() == target_class.casefold()
        # if not searching for specific class name, return all that are defined in this module
        return kls.__module__ == module.__name__

    filtered_classes = inspect.getmembers(
        module,
        filter_desired_class_from_file
    )

    if not len(filtered_classes):
        if target_class is not None:
            err_msg = f'Module "{module.__name__}" has not attribute "{target_class}".'
        else:
            err_msg = f'There is no class defined in the module "{module.__name__}" to import.'
        raise AttributeError(err_msg)

    return filtered_classes[0][1]


def concat_pages(pages: list[dict]) -> dict:
    """Concatenates a list of Data Service pages into a single dictionary object.

    Args:
        pages (list[dict]): list of Data Service pages

    Returns:
        dict: concatenated data from all pages
    """
    result = {
        'meta': {},
        'series': {},
        'stats': {},
        'derived': {
            'static': {},
            'series': {},
        }
    }

    first_page = True
    for page in pages:
        if first_page:
            result['meta'] = page['meta']
            first_page = False
        else:
            update_metadata(result['meta'], page['meta'])
        concat_results(result['series'], page['series'])
        if 'stats' in page:
            result['stats'].update(page['stats'])
        if 'derived' in page:
            if 'static' in page['derived']:
                result['derived']['static'].update(page['derived']['static'])
            if 'series' in page['derived']:
                concat_results(result['derived']['series'], page['derived']['series'])
    return result


def extract_host(url):
    pattern = r'https?://(?:api\.)?([^:/]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None
