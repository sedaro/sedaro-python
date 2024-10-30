import json
import math
from os import listdir
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
    "PROVISIONING": "⌛",
    "CONFIGURING": "⌛",
    "BUILDING": "⌛",
    "RUNNING": "⌛",
    "ERROR": "❌"
}
HFILL = 75


def hfill(char="-", len=HFILL):
    print(char * len)

def _element_id_dict(agent_data):
    '''Break out all blocks into a dict where each key is an ID.'''
    out = {}
    if 'blocks' in agent_data:
        for id_, value in agent_data['blocks'].items():
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


def _restructure_data(series, agents, meta):
    agent_mapping = {}
    blocks = {}
    index = {}

    for series_key in series:
        agent_id = series_key.split("/")[0]
        try:
            agent_mapping[agent_id] = agents[agent_id]
        except KeyError: # agent_id corresponding to coupling is not in the metamodel
            continue
        if agent_id not in blocks:
            blocks[agent_id] = _element_id_dict(meta['structure']['agents'].get(agent_id, {}))
        if agent_id not in index:
            index[agent_id] = {}
        df = series[series_key]

        columns = df.columns.tolist()
        for column in columns:
            if '/' not in column:  # ignore engine variables
                elements = column.split(".")
                first_element = elements[0]
                if first_element not in blocks[agent_id]:
                    block_id = 'root'
                    path_components = elements
                else:
                    block_id = first_element
                    path_components = elements[1:]
                if block_id not in index[agent_id]:
                    index[agent_id][block_id] = {}
                this_block_index = index[agent_id][block_id]
                if series_key not in this_block_index:
                    this_block_index[series_key] = {}
                ptr = this_block_index[series_key]
                for element in path_components:
                    if element not in ptr:
                        ptr[element] = {}
                    ptr = ptr[element]

    return agent_mapping, blocks, index


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
            return _bsearch(low, mid - 1)
        else:
            return _bsearch(mid, high)
    if value < ordered_series[0]:
        return -1
    return _bsearch(0, len(ordered_series) - 1)


def get_column_names(column_index, prefix):
    """
    For example:
        column_index = {'body_eci': {'0': {}, '1': {}, '2': {}, '3': {}}, 'body_ecef': {'0': {}, '1': {}, '2': {}, '3': {}}}
        prefix = 'attitude'
    Returns:
        [
            'attitude.body_eci.0',
            'attitude.body_eci.1',
            'attitude.body_eci.2',
            'attitude.body_eci.3',
            'attitude.body_ecef.0',
            'attitude.body_ecef.1',
            'attitude.body_ecef.2',
            'attitude.body_ecef.3'
        ]
    """
    if len(column_index) == 0:
        return [prefix]
    else:
        # don't add a dot if prefix is empty (this is the case for the root block)
        if len(prefix) > 0:
            prefix = f"{prefix}."
        columns = []
        for key in column_index:
            columns.extend(get_column_names(column_index[key], f"{prefix}{key}"))
        return columns


def get_parquets(path: str):
    paths = listdir(path)
    return [parquet for parquet in paths if not parquet.startswith('.')]

VLLS = [
    'visibleEarthArea',
    'activeRoutines',
    'availableTransmitters',
    'pseudoranges',
]

def values_from_df(values, name=None):
    if name in VLLS or ('.' in name and name.split('.')[-1] in VLLS):
        return [json.loads(value) for value in values]
    else:
        return values

def value_from_df(value, name=None):
    if name in VLLS or ('.' in name and name.split('.')[-1] in VLLS):
        return json.loads(value)
    else:
        return value

def get_static_data(static_data, object_type, engine=None):
        if engine is None:
            return static_data
        else:
            try:
                return static_data[engine]
            except KeyError:
                if len(static_data) == 0:
                    raise KeyError(f"No static data available for this {object_type}.")
                else:
                    prefix = list(engine.keys())[0][:-1]
                    assert len(ENGINE_EXPANSION) == len(ENGINE_MAP)
                    for i in range(len(ENGINE_EXPANSION)):
                        if engine.lower() in [k.lower() for k in [
                            int(list(ENGINE_MAP.keys())[i]),
                            list(ENGINE_MAP.keys())[i],
                            list(ENGINE_MAP.values())[i],
                            list(ENGINE_EXPANSION.keys())[i],
                            list(ENGINE_EXPANSION.values())[i],
                        ]]:
                            stream_id = prefix + str(i)
                            try:
                                return static_data[stream_id]
                            except KeyError:
                                raise KeyError(f"No static data available for the specified engine for this {object_type}.")
                    else:
                        raise ValueError(f"{engine} is not a valid engine identifier.")


class FromFileAndToFileAreDeprecated:
    @classmethod
    def from_file(self, filename: Union[str, Path]):
        print("Warning: `from_file` is deprecated. Use `load` instead. Calling `load`.")
        return self.load(filename)

    def to_file(self, filename: Union[str, Path]):
        print("Warning: `to_file` is deprecated. Use `save` instead. Calling `save`.")
        return self.save(filename)
