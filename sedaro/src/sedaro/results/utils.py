import json
import math
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import TYPE_CHECKING, TypeVar, Union

if TYPE_CHECKING:
    import dask.dataframe as dd

T = TypeVar('T', bound='SedaroResultBase')

DEFAULT_HOST = 'https://api.sedaro.com'
ENGINE_MAP = {
    '0': 'gnc',
    '1': 'cdh',
    '2': 'power',
    '3': 'thermal',
}
ENGINE_MAP_REVERSED = {
    'gnc': '0',
    'cdh': '1',
    'power': '2',
    'thermal': '3',
}
ENGINE_MAP_CASED = {
    'gnc': 'GNC',
    'cdh': 'CDH',
    'power': 'Power',
    'thermal': 'Thermal',
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
        except KeyError:  # agent_id corresponding to coupling is not in the metamodel
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
    paths = os.listdir(path)
    return [parquet for parquet in paths if not parquet.startswith('.')]


VLLS = [
    'visibleEarthArea',
    'activeRoutines',
    'availableTransmitters',
    'pseudoranges',
]


def parse_set_string(set_string):
    if set_string is None:
        return None
    # Converts a set represented as a string to a list
    values = set_string.strip("{}").split(",")
    return [item.strip().strip("'") for item in values]


def values_from_df(values, name=None):
    if not name:
        return values
    if name == 'availableTransmitters' or ('.' in name and name.split('.')[-1] == 'availableTransmitters'):
        # data for availableTransmitters is returned as a list of sets (represented as strings) which is not JSON-serializable
        return [parse_set_string(s) for s in values]
    elif name in VLLS or ('.' in name and name.split('.')[-1] in VLLS):
        return [json.loads(item.replace("'", '"')) for item in values]
    else:
        return values


def value_from_df(value, name=None):
    if not name:
        return value
    if name == 'availableTransmitters' or ('.' in name and name.split('.')[-1] == 'availableTransmitters'):
        # data for availableTransmitters is returned as a list of sets (represented as strings) which is not JSON-serializable
        return parse_set_string(value)
    elif name in VLLS or ('.' in name and name.split('.')[-1] in VLLS):
        return json.loads(value.replace("'", '"'))
    else:
        return value


def get_static_data(static_data: dict, object_type: str, engine: str = None):
    if len(static_data) == 0:
        raise ValueError(f"No static data available for this {object_type}.")
    elif engine is None:
        return static_data
    else:
        prefix = list(static_data.keys())[0][:-1]
        if engine.lower() in ENGINE_MAP_REVERSED.keys():
            stream_int = ENGINE_MAP_REVERSED[engine.lower()]
            try:
                return static_data[f"{prefix}{stream_int}"]
            except KeyError:
                raise KeyError(f"No static data available for the specified engine for this {object_type}.")
        else:
            raise ValueError(f"{engine} is not a valid engine identifier.")


def get_static_data_engines(static_data: dict):
    if static_data is None:
        return []
    else:
        return [ENGINE_MAP_CASED[ENGINE_MAP[stream_id[-1]]] for stream_id in static_data.keys()]


def df_schema_for_pyarrow(error: ValueError) -> dict:
    '''
    For columns for which PyArrow failed at schema inference, build a manual schema dict.
    This is necessary because, according to the dask.dataframe.to_parquet documentation [REF 1],
    inferring the PyArrow schema based on the Dask DataFrame metadata "is usually sufficient
    for common schemas, but notably will fail for object dtype columns that contain things other than strings."
    The error message raised by PyArrow has a predictable format [REF 2], containing all the information needed,
    so we can parse it to build a schema dict.
    REF 1: https://docs.dask.org/en/stable/generated/dask.dataframe.to_parquet.html
    REF 2: https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L786-L798
    '''
    class Column:
        def __init__(self, expected: str):
            self.expected = expected

        def set_received(self, received: str):
            self.received = received

        def needs_updating(self):
            return self.expected != self.received

    error_message = str(error)
    lines = error_message.splitlines()[3:-3]  # exclude header and footer information, irrelevant for our purposes
    fields: dict[str, Column] = {}
    for line in lines:
        # first, the expected schema is listed, with a line in format `    <column_name>: <type> ` for each column
        # then, the same is done for the received schema
        if line in ['Expected partition schema:', 'Received partition schema:']:
            continue
        # remove all whitespace (including the space after the colon) from line
        line = line.replace(' ', '')
        if line == '':
            continue
        # split the line into column name and type
        try:
            column_name, column_type = line.split(':')
        except ValueError:
            raise ValueError(f"PyArrow schema harmonization: error parsing message line: {line}")
        # if the column is not in `fields`, add it and its expected type
        if column_name not in fields:
            fields[column_name] = Column(column_type)
        # if the column is already in `fields`, set its received type
        else:
            fields[column_name].set_received(column_type)
    # now, we can build the schema dict
    schema = {}
    for field_name in fields:
        field = fields[field_name]
        # if the received type is different from the expected type, add it to the schema dict
        if field.needs_updating():
            schema[field_name] = field.received
    return schema


class SedaroResultBase(ABC):
    @classmethod
    def from_file(self, filename: Union[str, Path]):
        print("Warning: `from_file` is deprecated. Use `load` instead. Calling `load`.")
        return self.load(filename)

    def to_file(self, filename: Union[str, Path]):
        print("Warning: `to_file` is deprecated. Use `save` instead. Calling `save`.")
        return self.save(filename)

    @staticmethod
    def data_subdir(root_path: Union[str, Path]):
        '''Return the subdirectory where the data is stored.'''
        return f"{root_path}/data"

    @staticmethod
    def agent_name_for_filename(agent_name: str):
        '''Convert agent name to a format that can be used as a file name.'''
        return agent_name.replace('/', '.')

    @staticmethod
    def agent_name_from_filename(filename: str):
        '''Convert a file name back to the original agent name.'''
        return filename.replace('.', '/')

    def save_parquets(self, data: dict, path: Union[str, Path]):
        '''Save the DataFrames as Parquet files in their proper location given the specified save path.'''
        if TYPE_CHECKING:
            import dask.dataframe as dd
        os.mkdir(data_subdir_path := self.data_subdir(path))
        parquet_files = []
        for agent in data:
            agent_parquet_path = f"{data_subdir_path}/{(pq_filename := self.agent_name_for_filename(agent))}"
            parquet_files.append(pq_filename)
            df: dd = data[agent]
            try:
                df.to_parquet(agent_parquet_path)
            except ValueError as e:
                # the ValueError contains details on the schema mismatch, in a predictable format
                # REF: https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L786-L798
                if str(e).startswith("Failed to convert partition to expected pyarrow schema:"):
                    harmonized_df_schema = df_schema_for_pyarrow(e)
                    df.to_parquet(agent_parquet_path, schema=harmonized_df_schema)
                else:
                    raise e
        return parquet_files

    @classmethod
    def load_parquets(cls, path: Union[str, Path], metadata: dict) -> dict:
        '''Load Parquet files from the specified save path and return a dictionary of DataFrames.'''
        import dask.dataframe as dd
        data_subdir_path = cls.data_subdir(path)
        data = {}
        try:
            parquet_files = metadata['parquet_files']
        except KeyError:
            parquet_files = get_parquets(data_subdir_path)
        for agent in parquet_files:
            df = dd.read_parquet(f"{data_subdir_path}/{agent}")
            data[cls.agent_name_from_filename(agent)] = df
        return data

    def save(self, path: Union[str, Path]):
        '''Save the {class_name}'s data to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(
                    f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': self.__class__.__name__}, fp)
        metadata_to_save = self.do_save(path)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump(metadata_to_save, fp)
        print(f"{self.__class__.__name__} saved to {path}.")

    @abstractmethod
    def do_save(self, path: Union[str, Path]) -> dict:
        '''Save the data to the specified path. Return a metadata dict to be saved alongside it.'''
        pass

    @classmethod
    def load(cls: type[T], path: Union[str, Path]) -> T:
        '''Load a {class_name}'s data from the specified path.'''
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != cls.__name__:
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            metadata_dict = json.load(fp)
        return cls.do_load(path, metadata_dict)

    @classmethod
    @abstractmethod
    def do_load(cls: type[T], path: Union[str, Path], metadata_dict: dict) -> T:
        '''Given the metadata dict and the path from which to load data, load the data and return an instance of the class.'''
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.save.__doc__:
            cls.save.__doc__ = cls.save.__doc__.format(class_name=cls.__name__)
        if cls.load.__doc__:
            # since `load` is a classmethod, use `__func__.__doc__` to update the docstring
            cls.load.__func__.__doc__ = cls.load.__doc__.format(class_name=cls.__name__)
