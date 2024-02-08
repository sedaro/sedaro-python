import gzip
import json
from pathlib import Path
from typing import Generator, List, Union, Dict

from pydash import merge

from .block import SedaroBlockResult
from .utils import ENGINE_EXPANSION, HFILL, hfill


class SedaroAgentResult:

    def __init__(self, name: str, block_structures: dict, series: dict, initial_state: dict = None):
        '''Initialize a new agent result.

        Agent results are typically created through the .agent method of
        SedaroSimulationResult or the .from_file method of this class.
        '''
        self.__name = name
        self.__block_structures = block_structures
        self.__series = series
        self.__block_ids = sorted(set(
            block_id
            for module in self.__series
            for block_id in self.__series[module]['series']
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
    def name(self) -> str:
        return self.__name

    @property
    def blocks(self) -> List[str]:
        return self.__block_ids

    @property
    def blockNameToID(self) -> Dict[str, str]:
        return { self.__block_structures[block_id].get('name', None): block_id for block_id in self.__block_ids if block_id in self.__block_structures }

    @property
    def blockIdToName(self) -> Dict[str, str]:
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

        block_data = {}
        for module in self.__series:
            if id_ in self.__series[module]['series']:
                if module not in block_data:
                    block_data[module] = {}
                block_data[module]['time'] = self.__series[module]['time']
                block_data[module]['series'] = self.__series[module]['series'][id_]
        block_structure = self.__block_structures[id_] if id_ != 'root' else id_
        return SedaroBlockResult(block_structure, block_data)

    def blockname(self, name:str) -> SedaroBlockResult:
        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_structures[block_id].get('name', None)
                if name == block_name:
                    return self.block(block_id)
        raise ValueError(f"Block name '{name}' not found.")

    def to_file(self, filename: Union[str, Path], verbose=True) -> None:
        '''Save agent result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {
                'name': self.__name,
                'block_structures': self.__block_structures,
                'series': self.__series,
            }
            json.dump(contents, json_file)
            if verbose:
                print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load agent result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['name'], contents['block_structures'], contents['series'])

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print(f"Agent Result Summary".center(HFILL))
        print(f"'{self.__name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.__series:
            print(f'    • {ENGINE_EXPANSION[module]}')

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
            print( "Histogram plots require the sweetviz library to be imported. (pip import sweetviz)")
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
            raise ValueError('Statistics is disabled because pandas and/or matplotlib could not be imported. (pip install pandas)')

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

    def model_at(self, mjd):
        if not self.__initial_state:
            raise ValueError(
                'A time-variable model is not available for this agent. This is likely because the Agent is peripheral in the simulation.')

        # Rough out model
        blocks = {block_id: self.block(block_id).value_at(mjd) for block_id in self.__block_ids}
        model = {'blocks': blocks, **blocks['root']}
        del blocks['root']

        # Merge with initial state to fill in missing values
        # This order will overwrite any values in the initial state with values from the simulation
        return merge({}, self.__initial_state, model)
