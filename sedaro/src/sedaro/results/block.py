import gzip
import json
from pathlib import Path
from typing import Generator, Union

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, hfill


class SedaroBlockResult:

    def __init__(self, structure, series: dict):
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
        
        self.__variables = set()
        for module in self.__series:
            to_rename = {}
            for column_name in self.__series[module].columns.tolist():
                if column_name.split('.')[0] == module:
                    # rename to engine name
                    module_name = ENGINE_EXPANSION[ENGINE_MAP[module.split('/')[1]]]
                    self.__variables.add(module_name)
                    new_column_name = f"{module_name}.{'.'.join(column_name.split('.')[1:])}"
                    to_rename[column_name] = new_column_name
                else:
                    self.__variables.add(column_name.split('.')[0])
            if len(to_rename) > 0:
                self.__series[module] = self.__series[module].rename(columns=to_rename)
        self.__variables = sorted(list(self.__variables))

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        for module in self.__series:
            for column_name in self.__series[module].columns.tolist():
                selected_columns = []
                if column_name.split('.')[0] == name:
                    # this is the module containing the variable
                    selected_columns.append(column_name)
                if len(selected_columns) > 0:
                    variable_dataframe = self.__series[module][selected_columns]
                    return SedaroSeries(name, variable_dataframe)
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

    def to_file(self, filename: Union[str, Path], verbose=True) -> None:
        '''Save block result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'structure': self.__structure, 'series': self.__series}
            json.dump(contents, json_file)
            if verbose:
                print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load block result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['structure'], contents['series'])

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

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}
