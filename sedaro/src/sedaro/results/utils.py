import math
import numpy as np
from pathlib import Path
from typing import Union

DEFAULT_HOST = 'https://api.sedaro.com'
ENGINE_MAP = {
    '0': 'gnc',
    '1': 'cdh',
    '2': 'power',
    '3': 'thermal',
}
ENGINE_EXPANSION = {
    'gnc': 'Guidance, Navigation, & Control',
    'cdh': 'Command & Data Handling',
    'power': 'Power',
    'thermal': 'Thermal',
}
STATUS_ICON_MAP = {
    "SUCCEEDED": "✅",
    "FAILED": "❌",
    "TERMINATED": "❌",
    "PAUSED": "⏸️",
    "PENDING": "⌛",
    "RUNNING": "⌛",
    "ERROR": "❌"
}
HFILL = 75


def hfill(char="-", len=HFILL):
    print(char * len)


def _element_id_dict(agent_data):
    '''Break out all blocks into a dict where each key is an ID.'''
    out = {}
    for entry in agent_data.values():
        if isinstance(entry, dict):
            for id_, value in entry.items():
                if 'id' in value:
                    if id_ in out:
                        raise ValueError(f"Duplicate ID {id_}")
                    else:
                        out[id_] = value

    return out


def _block_type_in_supers(block_type: str, meta_supers: dict, super_type: str = 'Agent') -> bool:
    if block_type == super_type:
        return True
    elif block_type in meta_supers:
        supertypes = meta_supers[block_type]
        if len(supertypes) == 0:
            return False
        return any(_block_type_in_supers(supertype, meta_supers, super_type=super_type) for supertype in supertypes)
    else:
        return False


def _get_agent_id_name_map(meta):
    '''Get mapping from agent ID to name.'''
    return {
        id_: entry['name']
        for id_, entry in meta['structure']['scenario']['blocks'].items()
        if _block_type_in_supers(entry['type'], meta['structure']['scenario']['_supers'])
    }


def _simplify_series(engine_data: dict, blocks: dict) -> dict:
    '''Build a simplified series data structure

    Creates a dictionary with the following hierarchy:
        Block ID (or root)
            Variable Name
    '''
    data = {'root': {}}
    for key, value in engine_data.items():
        if key in blocks:
            data[key] = {}
            for subkey, subvalue in value.items():
                data[key][subkey] = subvalue
        elif "/" in key:
            # Ignore engine variables
            continue
        else:
            data['root'][key] = value
    return data


def _get_agent_mapping(series, agents, meta):
    agent_mapping = {}
    block_structures = {}
    for series_key in series:
        agent_id = series_key.split("/")[0]
        agent_mapping[agent_id] = agents[agent_id]
        if agent_id not in block_structures:
            block_structures[agent_id] = _element_id_dict(meta['structure']['agents'].get(agent_id, {}))
    return agent_mapping, block_structures


def _get_series_type(series):
    for entry in series:
        if entry is not None:
            return type(entry).__name__
    else:
        return "None"


def bsearch(ordered_series, value):
    '''Binary search for a value in an ordered series.

    Returns the index of the value in the series, or the index of the immediately
    lower value if the value is not present.
    '''
    def _bsearch(low, high):
        if high == low:
            return low
        mid = math.ceil((high + low) / 2)
        if ordered_series[mid] == value:
            return mid
        elif ordered_series[mid] > value:
            return _bsearch(low, mid-1)
        else:
            return _bsearch(mid, high)
    if value < ordered_series[0]:
        return -1
    return _bsearch(0, len(ordered_series) - 1)

class FromFileAndToFileAreDeprecated:
    def from_file(self, filename: Union[str, Path]):
        print("Warning: `from_file` is deprecated. Use `load` instead. Calling `load`.")
        return self.load(filename)

    def to_file(self, filename: Union[str, Path]):
        print("Warning: `to_file` is deprecated. Use `save` instead. Calling `save`.")
        return self.save(filename)