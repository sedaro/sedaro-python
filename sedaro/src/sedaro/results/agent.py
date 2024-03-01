import dask.dataframe as dd
import json
import os
from pathlib import Path
from typing import Generator, List, Union, Dict
from functools import lru_cache, cached_property

from pydash import merge

from .block import SedaroBlockResult
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, bsearch, hfill, FromFileAndToFileAreDeprecated


class SedaroAgentResult(FromFileAndToFileAreDeprecated):
    def __init__(self, name: str, block_structures: dict, series: dict, column_index: dict, initial_state: dict = None):
        '''Initialize a new agent result.

        Agent results are typically created through the .agent method of
        SedaroSimulationResult or the .from_file method of this class.
        '''
        self.__name = name
        self.__column_index = column_index
        self.__block_structures = block_structures
        self.__series = series
        self.__block_uuids = [k for k in self.__column_index]
        self.__block_ids = sorted(set(
            block_id.split('.')[0] if block_id.split('.')[0] in self.__block_uuids else 'root'
            for module in self.__series
            for block_id in self.__series[module].columns.tolist()
        ),
            reverse=True
        )
        self.__initial_state = initial_state

    def __iter__(self) -> Generator:
        '''Iterate through blocks on this agent.'''
        return (self.block(id_) for id_ in self.__block_ids)

    def __contains__(self, id_: str) -> bool:
        '''Check if this agent result contains a certain block ID.'''
        return id_ in self.__block_ids

    @property
    def dataframe(self) -> Dict[str, dd.DataFrame]:
        '''Get the raw Dask DataFrames for this agent.'''
        return self.__series

    @property
    def name(self) -> str:
        return self.__name

    @property
    def blocks(self) -> List[str]:
        return self.__block_ids

    @cached_property
    def block_name_to_id(self) -> Dict[str, str]:
        return { self.__block_structures[block_id].get('name', None): block_id for block_id in self.__block_ids if block_id in self.__block_structures }

    @cached_property
    def block_id_to_name(self) -> Dict[str, str]:
        return { block_id: self.__block_structures[block_id].get('name', None) for block_id in self.__block_ids if block_id in self.__block_structures }


    def block(self, id_: str) -> SedaroBlockResult:
        '''Query results for a particular block by ID.'''
        id_ = str(id_)
        if id_ not in self.__block_ids:
            matching_id = [entry for entry in self.__block_ids if entry.startswith(id_)]
            if len(matching_id) == 1:
                id_ = matching_id[0]
            elif len(matching_id) == 0:
                raise ValueError(f"ID '{id_}' not found.")
            else:
                raise ValueError(f'Found multiple matching IDs for {id_}: {matching_id}.')

        prefix = '' if id_ == 'root' else id_ + '.'
        block_structure = self.__block_structures[id_] if id_ != 'root' else id_
        block_streams = {}
        for stream in self.__series:
            if stream in self.__column_index[id_]:
                block_streams[stream] = self.__series[stream]
        return SedaroBlockResult(block_structure, block_streams, self.__column_index[id_], prefix)

    def block_name(self, name:str) -> SedaroBlockResult:
        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_structures[block_id].get('name', None)
                if name == block_name:
                    return self.block(block_id)
        raise ValueError(f"Block name '{name}' not found.")

    def save(self, path: Union[str, Path]):
        '''Save the agent result to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SedaroAgentResult'}, fp)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({
                'name': self.__name,
                'initial_state': self.__initial_state,
                'block_structures': self.__block_structures,
                'column_index': self.__column_index,
            }, fp)
        os.mkdir(f"{path}/data")
        for engine in self.__series:
            engine_parquet_path = f"{path}/data/{engine.replace('/', '.')}"
            df : dd = self.__series[engine]
            df.to_parquet(engine_parquet_path)
        print(f"Agent result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load an agent result from the specified path.'''
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroAgentResult':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            meta = json.load(fp)
            name = meta['name']
            block_structures = meta['block_structures']
            initial_state = meta['initial_state']
            column_index = meta['column_index']
        engines = {}
        parquets = os.listdir(f"{path}/data/")
        for engine in parquets:
            df = dd.read_parquet(f"{path}/data/{engine}")
            engines[engine.replace('.', '/')] = df
        return cls(name, block_structures, engines, column_index, initial_state)

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print(f"Agent Result Summary".center(HFILL))
        print(f"'{self.__name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.__series:
            print(f'    • {ENGINE_EXPANSION[ENGINE_MAP[module.split("/")[1]]]}')

        print("\n📦 Available Blocks")
        print('    ' + '-' * 58)
        print('    |' + 'id'.center(38) + 'name'.center(30-12) + '|')
        print('    ' + '-' * 58)

        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_structures[block_id].get('name', None)
                block_id_col = f"{block_id[:26]}"
                if block_name is not None:
                    name_id_col = f'{block_name[:25]}'
                else:
                    name_id_col = f'<Unnamed Block>'
            else:
                block_id_col = f"root"
                name_id_col = ''
            print(f"    | {block_id_col:26s} | {name_id_col:25s} |")
        print('    ' + '-' * 58)

        no_data_blocks = len(self.__block_structures) - len(self.__block_ids)
        if no_data_blocks > 0:
            print(f"\n    {no_data_blocks} block(s) with no associated data")

        hfill()
        print("❓ Query block results with .block(<ID>) or .block(<PARTIAL_ID>) or .blockname(<name>)")
        hfill()
        print("⍆ The following commands have an optional variables argument which is a list of blockname.variable prefixes to filter on.")
        print("📊 Display agent modules variables statistics with .stats( module ) ")
        print(f"🧩        Where module must be one of the following: { [module for module in self.__series] } ")
        print("📊 Display all agent module variables histograms for a study simulation with .sim_histogram( module, output_html=False, variables=None )")
        print("📈📉 Display block variables scatter matrix plot  ")
        print("📉📈      for a study simulation with .sim_scatter_matrix( sim_id, variables=None )") 


    @lru_cache
    def create_dataframe(self, module, variables=None):
        try:
            import pandas as pd
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
        except ImportError:
            raise ValueError('Statistics is disabled because pandas could not be imported. (pip install pandas)')

        var_dfs = []
        def add_to_df_list(first_value, column_name, data):
            if type(first_value) is list:
                list_len = len(first_value)
                columns = [ f'{column_name}.{index}' for index in range(list_len)]
                var_dfs.append( pd.DataFrame(data, columns=columns ) )
            else:
                var_dfs.append( pd.DataFrame(data, columns=[column_name]) )

        for block_id in self.__series[module]['series']:
            block_results = self.block(block_id)
            block_name = block_results.name

            for variable_name in block_results.variables:
                variable_data = block_results.variable(variable_name)
                column_name   = f'{block_name}.{variable_name}'

                if variable_data.has_subseries:
                    for key, subtype in variable_data.subtypes:                    
                        data = [value for value in variable_data[key].values if value is not None]
                        first_value = data[0] if len(data) > 0 else None
                        if first_value is None:
                            continue
                        column_name_key = f'{column_name}.{key}'
                        if variables is not None and not any([ column_name_key.startswith(variable) for variable in variables]):
                            continue
                        add_to_df_list(first_value, column_name_key, data)
                else: 
                    if variables is not None and not any([ column_name.startswith(variable) for variable in variables]):
                        continue                  
                    data = [ value for value in variable_data.values if value is not None]
                    first_value = data[0] if len(data) > 0 else None
                    if first_value is None:
                        continue
                    add_to_df_list(first_value, column_name, data)
                
        block_dfs = pd.concat( var_dfs, axis=1) 
        return block_dfs
     
    def stats(self, module, variables=None):
        if module not in self.__series:
            print(f"Module: '{module}' not found with this agent results object. Available modules are { [module for module in self.__series] }")
            return
        
        block_dfs = self.create_dataframe(module, variables)
   
        try:
            from IPython.display import display
            display(block_dfs.describe(include='all').T)
        except:
            print(block_dfs.describe(include='all').T)

    def histogram(self, module, output_html=False, variables=None):
        print('⚠️ Rendering the histogram plots can take some time if the module has a large number of blocks/variables')
        try:
            import sweetviz as sv
        except ImportError:
            print( "Histogram plots require the sweetviz library to be installed. (pip install sweetviz)")
        else:
            block_dfs = self.create_dataframe(module, variables)
            sv.config_parser['Layout']['show_logo'] = '0' 
            sv_report = sv.analyze(block_dfs, pairwise_analysis="off" )

            if output_html:
                sv_report.show_html(filepath=f'agent_{self.name}_Report.html')
            else:
                sv_report.show_notebook(w="90%", h="full", layout='vertical')  

    def scatter_matrix(self, module, variables=None):
        try:
            import pandas as pd
            import matplotlib.pyplot as plt
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
        except ImportError:
            raise ValueError('Statistics is disabled because pandas and/or matplotlib could not be imported. (pip install pandas matplotlib)')

        block_dfs = self.create_dataframe(module, variables)
        just_numbers = block_dfs.select_dtypes(include=['number'])
        no_distint_cols = just_numbers[[c for c in list(just_numbers)
                                                if len(just_numbers[c].unique()) > 1]]
        sm = pd.plotting.scatter_matrix(no_distint_cols, alpha=0.2, figsize=(12,12), diagonal='kde')
        # Change label rotation
        [s.xaxis.label.set_rotation(90) for s in sm.reshape(-1)]
        [s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]
        [s.get_yaxis().set_label_coords(-2.0,0.5) for s in sm.reshape(-1)]
        [s.set_xticks(()) for s in sm.reshape(-1)]
        [s.set_yticks(()) for s in sm.reshape(-1)]
        plt.show()      

    def __model_at(self, mjd):
        # Rough out model
        blocks = {block_id: self.block(block_id).value_at(mjd) for block_id in self.__block_ids}
        model = {'blocks': blocks, **blocks['root']}
        del blocks['root']

        # Merge with initial state to fill in missing values
        # This order will overwrite any values in the initial state with values from the simulation
        return merge({}, self.__initial_state, model)

    def model_at(self, mjd):
        if not self.__initial_state:
            raise ValueError(
                'A time-variable model is not available for this agent. This is likely because the Agent is peripheral in the simulation.')

        # find closest MJD for each dataframe
        trimmed_engines = {}
        for engine in self.__series:
            bsearch_index = bsearch(engine_mjds := self.__series[engine].index.values.compute(), mjd)
            floor = engine_mjds[bsearch_index]
            try:
                ceil = engine_mjds[bsearch_index + 1]
            except IndexError:
                ceil = floor
            trimmed_engines[engine] = self.__series[engine].loc[floor:ceil].compute()

        return SedaroAgentResult(self.__name, self.__block_structures, trimmed_engines, self.__column_index, self.__initial_state).__model_at(mjd)
