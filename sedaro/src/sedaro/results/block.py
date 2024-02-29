import dask.dataframe as dd
import json
import os
from pathlib import Path
from typing import Generator, Union

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, hfill, FromFileAndToFileAreDeprecated


class SedaroBlockResult(FromFileAndToFileAreDeprecated):

    def __init__(self, structure, series: dict, column_index: dict, prefix: str):
        '''Initialize a new block result.

        Block results are typically created through the .block method of
        SedaroAgentResult or the .from_file method of this class.
        '''
        if 'name' in structure:
            self.__name = structure['name']
        elif structure == 'root':
            self.__name = 'root'
        else:
            self.__name = '<Unnamed Block>'
        self.__structure = structure
        self.__series = series
        self.__column_index = column_index
        self.__prefix = prefix
        self.__variables = []
        for stream in self.__column_index:
            for variable in self.__column_index[stream]:
                self.__variables.append(variable)
        self.__variables = sorted(list(self.__variables))

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        prefix = f"{self.__prefix}{name}"
        for stream in self.__column_index:
            if name in self.__column_index[stream]:
                return SedaroSeries(name, self.__series[stream], self.__column_index[stream][name], prefix)
        else:
            raise ValueError(f'Variable "{name}" not found.')

    def __contains__(self, variable: str) -> bool:
        '''Check if this block contains a variable by name.'''
        return variable in self.variables

    def __iter__(self) -> Generator:
        '''Iterate through variables on this block.'''
        return (self.__getattr__(variable) for variable in self.variables)

    def __repr__(self) -> str:
        return f'SedaroBlockResult({self.name})'

    @property
    def name(self):
        return self.__name

    @property
    def modules(self):
        return self.__series.keys()

    @property
    def variables(self):
        return self.__variables

    def module_to_dataframe(self):
        raise NotImplementedError("")

    def variable(self, name: str) -> SedaroSeries:
        '''Query a particular variable by name.'''
        return self.__getattr__(name)

    def save(self, path: Union[str, Path]):
        '''Save the block result to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SedaroBlockResult'}, fp)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({
                'structure': self.__structure,
                'column_index': self.__column_index,
                'prefix': self.__prefix
            }, fp)
        os.mkdir(f"{path}/data")
        for engine in self.__series:
            engine_parquet_path = f"{path}/data/{engine.replace('/', '.')}"
            df : dd = self.__series[engine]
            df.to_parquet(engine_parquet_path)
        print(f"Block result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a block result from the specified path.'''
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroBlockResult':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            meta = json.load(fp)
            structure = meta['structure']
            column_index = meta['column_index']
            prefix = meta['prefix']
        engines = {}
        parquets = os.listdir(f"{path}/data/")
        for agent in parquets:
            df = dd.read_parquet(f"{path}/data/{agent}")
            engines[agent.replace('.', '/')] = df
        return cls(structure, engines, column_index, prefix)

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print("Sedaro Simulation Block Result Summary".center(HFILL))
        if self.name != '<Unnamed Block>':
            print(f"'{self.name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.modules:
            print(f'    • {ENGINE_EXPANSION[ENGINE_MAP[module.split("/")[1]]]}')

        print("\n📋 Variables Available")
        for variable in self.variables:
            print(f'    • {variable}')
        hfill()
        print("❓ Query variables with .<VARIABLE_NAME>")
        print("📊 Display all block variables statistics with .stats( output_html=False ) ")
        print("📊 Display histograms with .histogram(output_html=False)")
        print("📈📉 Display scatter matrix plot")
        print("📉📈      with .scatter_matrix( block_variable_list )") 
        

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}


    def scatter_matrix(self, size=10, variables=None):
        try:
            import pandas as pd
            import matplotlib.pyplot as plt
        except ImportError:
            raise ValueError('scatter_matrix is disabled because pandas and/or matplotlib could not be imported. (pip install pandas matplotlib)')

        block_dfs = self.create_dataframe(variables) 
        just_numbers = block_dfs.select_dtypes(include=['number'])
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


    def stats(self, variables=None):
        block_dfs = self.create_dataframe(variables) 

        try:
            from IPython.display import display
            display(block_dfs.describe(include='all').T)
        except:
            print(block_dfs.describe(include='all').T)

    def histogram(self, output_html=False, variables=None):
        try:
            import sweetviz as sv
        except ImportError:
            print( "Histogram plots require the sweetviz library to be imported. (pip import sweetviz)")
        else:
            block_dfs = self.create_dataframe(variables)
            sv.config_parser['Layout']['show_logo'] = '0' 
            sv_report = sv.analyze(block_dfs, pairwise_analysis="off" )

            if output_html:
                sv_report.show_html(filepath=f'Block_{self.name}_Report.html')
            else:
                sv_report.show_notebook(w="90%", h="full", layout='vertical')

    def create_dataframe(self, variables=None):
        try:
            import pandas as pd
        except ImportError:
            raise ValueError('Statistics is disabled because pandas could not be imported. (pip install pandas)')

        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        var_dfs = []

        def add_to_df_list(first_value, column_name, data):
            if type(first_value) is list:
                list_len = len(first_value)
                columns = [ f'{column_name}.{index}' for index in range(list_len)]
                var_dfs.append( pd.DataFrame(data, columns=columns ) )
            else:
                var_dfs.append( pd.DataFrame(data, columns=[column_name]) )
        if variables is None:
            variables = self.variables
        for variable_name in variables:
            variable_data = self.variable(variable_name)
                    
            column_name = f'{self.name}.{variable_name}'
            if variable_data.has_subseries:
                for key, subtype in variable_data.subtypes:
                    data = [ value for value in  variable_data[key].values if value is not None]
                    first_value = data[0] if len(data) > 0 else None
                    if first_value is None:
                        continue
                    add_to_df_list(first_value, f'{column_name}.{key}', data)
            else:                    
                data = [ value for value in variable_data.values if value is not None]
                first_value = data[0] if len(data) > 0 else None
                if first_value is None:
                    continue
                add_to_df_list(first_value, column_name, data)
        block_dfs = pd.concat( var_dfs, axis=1)
        return block_dfs

