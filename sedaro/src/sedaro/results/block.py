import gzip
import json
from pathlib import Path
from typing import Generator, Union

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, HFILL, hfill


class SedaroBlockResult:

    def __init__(self, structure, series: dict, axis: str):
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
        self.__axis = axis
        self.__variables = [variable for data in self.__series.values() for variable in data['series']]

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        for module in self.__series:
            if name in self.__series[module]['series']:
                return SedaroSeries(
                    name,
                    self.__series[module]['time'],
                    self.__series[module]['series'][name],
                    self.__axis
                )
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
        '''Save agent result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'structure': self.__structure, 'series': self.__series, 'axis': self.__axis}
            json.dump(contents, json_file)
            if verbose:
                print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load agent result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['structure'], contents['series'], contents['axis'])

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print("Sedaro Simulation Block Result Summary".center(HFILL))
        if self.name != '<Unnamed Block>':
            print(f"'{self.name}'".center(HFILL))
        hfill()

        print("🧩 Simulated Modules")
        for module in self.modules:
            print(f'    • {ENGINE_EXPANSION[module]}')

        print("\n📋 Variables Available")
        for variable in self.variables:
            print(f'    • {variable}')
        hfill()
        print("❓ Query variables with .<VARIABLE_NAME>")

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}
