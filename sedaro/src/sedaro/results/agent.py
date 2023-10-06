import gzip
import json
from pathlib import Path
from typing import Generator, List, Union

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

    def summarize(self) -> dict:
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

        blockname_to_id = {}

        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_structures[block_id].get('name', None)
                block_id_col = f"{block_id[:26]}"
                if block_name is not None:
                    name_id_col = f'{block_name[:25]}'
                    blockname_to_id[name_id_col] = block_id
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
        print("📊 Display agent modules variables statistics with .stats( module, output_html=False, make_histogram_plots=False ) ")
        print(f"🧩        Where module must be one of the following: { [module for module in self.__series] } ")

    def stats(self, module, output_html=False, make_histogram_plots=False):
        if module not in self.__series:
            print(f"Module: '{module}' not found with this agent results object. Available modules are { [module for module in self.__series] }")
            return
        try:
            import pandas as pd
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            var_dfs = []

            # todo: move the repeated code to utils
            def add_to_df_list(first_value, column_name, data):
                if type(first_value) is list:
                    list_len = len(first_value)
                    columns = [f'{column_name}_X', f'{column_name}_Y', f'{column_name}_Z']
                    if list_len == 4:
                        columns.append(f'{column_name}_Q') 
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
                            first_value = variable_data[key].values[0]
                            data = variable_data[key].values
                            add_to_df_list(first_value, f'{column_name}.{key}', data)
                    else:
                        first_value = variable_data.values[0]
                        data = variable_data.values
                        add_to_df_list(first_value, column_name, data)
                    
            block_dfs = pd.concat( var_dfs, axis=1)     
            try:
                from IPython.display import display
                display(block_dfs.describe(include='all').T)
            except:
                print(block_dfs.describe(include='all').T)
        except ImportError:
            raise ValueError('Statistics is disabled because pandas could not be imported. (pip install pandas)')

        if make_histogram_plots:
            print('⚠️ Rendering the histogram plots can take some time if the module has a large number of blocks/variables')
            try:
                import sweetviz as sv
            except ImportError:
                print( "Histogram plots require the sweetviz library to be imported. (pip import sweetviz)")
            else:
                sv.config_parser['Layout']['show_logo'] = '0' 
                sv_report = sv.analyze(block_dfs, pairwise_analysis="off" )

                if output_html:
                    sv_report.show_html(filepath=f'agent_{self.name}_Report.html')
                else:
                    sv_report.show_notebook(w="90%", h="full", layout='vertical')        



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
