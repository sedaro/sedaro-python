import math
import numpy as np
from pathlib import Path
from typing import Union
import sweetviz as sv
import pandas as pd
import matplotlib.pyplot as plt
from functools import lru_cache, cached_property

DEFAULT_HOST = 'https://api.sedaro.com'
ENGINE_MAP = {
    '0': 'gnc',
    '1': 'cdh',
    '2': 'power',
    '3': 'thermal',
}
ENGINE_NAME_TO_INDEX = {
    'gnc': 0,
    'cdh': 1,
    'power': 2,
    'thermal': 3,
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


def stats(df):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', None)
    return df.describe().T

def histogram(df, output_html= False):   
    sv_report = sv.analyze(df, pairwise_analysis="on" )
    if output_html:
        sv_report.show_html(filepath=f'Histogram_Report.html')
    else:
        sv_report.show_notebook(w="90%", h="full", layout='vertical') 

def scatter_matrix(df, size=10):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    just_numbers = df.select_dtypes(include=['number'])
    no_distint_cols = just_numbers[[c for c in list(just_numbers)
                                            if len(just_numbers[c].unique()) > 1]]
    sm = pd.plotting.scatter_matrix(no_distint_cols, alpha=0.2, figsize=(size,size), diagonal='kde')
    # Change label rotation
    [s.xaxis.label.set_rotation(90) for s in sm.reshape(-1)]
    [s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]
    [s.get_yaxis().set_label_coords(-2.0,0.5) for s in sm.reshape(-1)]
    [s.set_xticks(()) for s in sm.reshape(-1)]
    [s.set_yticks(()) for s in sm.reshape(-1)]
    plt.show()

def compare_sims(sim_1_df, sim_2_df, output_html, sim_id_1_label, sim_id_2_label):

    compare_report = sv.compare([sim_1_df, sim_id_1_label], [sim_2_df, sim_id_2_label])
    if output_html:
        compare_report.show_html(filepath=f'compare_{sim_id_1_label}_{sim_id_2_label}_Report.html')
    else:
        compare_report.show_notebook(w="90%", h="full", layout='vertical')  

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


def _restructure_data(series, agents, meta):
    agent_mapping = {}
    blocks = {}
    index = {}

    for series_key in series:
        agent_id = series_key.split("/")[0]
        agent_mapping[agent_id] = agents[agent_id]
        if agent_id not in blocks:
            blocks[agent_id] = _element_id_dict(meta['structure']['agents'].get(agent_id, {}))
        if agent_id not in index:
            index[agent_id] = {}
        df = series[series_key]

        columns = df.columns.tolist()
        for column in columns:
            if '/' not in column: # ignore engine variables
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
            return _bsearch(low, mid-1)
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
            if prefix[-1] != '.':
                prefix = f"{prefix}."
        columns = []
        for key in column_index:
            columns.extend(get_column_names(column_index[key], f"{prefix}{key}"))
        return columns


class FromFileAndToFileAreDeprecated:
    @classmethod
    def from_file(self, filename: Union[str, Path]):
        print("Warning: `from_file` is deprecated. Use `load` instead. Calling `load`.")
        return self.load(filename)

    def to_file(self, filename: Union[str, Path]):
        print("Warning: `to_file` is deprecated. Use `save` instead. Calling `save`.")
        return self.save(filename)
    

class StatFunctions:

    @lru_cache(maxsize=10)
    def create_pandas_dataframe(self, module:str=None, filter_string=None):
        if type(self.dataframe) == dict:
            var_dfs = []
            for module_name in self.dataframe.keys():
                module_index =  module_name.split("/")[1]
                if ENGINE_MAP[module_index] == module or module == None:
                    new_df = self.dataframe[module_name].compute()
                    if filter_string:
                        new_df = new_df.filter(like=filter_string)
                    if new_df.count().sum().sum() == 0:
                        continue
                    var_dfs.append(new_df)
            dfs = pd.concat(var_dfs, axis=1)
            return dfs
        else:
            new_df = self.dataframe().compute()
            if filter_string:
                new_df = new_df.filter(like=filter_string)
            return new_df
        
    def scatter_matrix(self, size=10, module:str=None, filter_string=None):
        block_df = self.create_pandas_dataframe(module=module, filter_string=filter_string) 
        scatter_matrix(block_df, size)

    def stats(self, module:str=None,filter_string=None):
        block_df = self.create_pandas_dataframe(module=module,filter_string=filter_string) 
        return stats(block_df)

    def histogram(self, module:str=None, filter_string=None, output_html=False):

        block_df = self.create_pandas_dataframe(module=module,filter_string=filter_string)
        histogram(block_df, output_html)

    def print_stats_section(self):
        print("𝛴 Display statistics with .stats( output_html=False ) ")
        print("📊 Display histograms with .histogram(output_html=False)")
        print("📈📉 ")
        print("📉📈 Display scatter matrix with .scatter_matrix(output_html=False)")