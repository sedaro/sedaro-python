import gzip
import json


from typing import Generator, Union, List
from pathlib import Path
from sedaro.results.block import SedaroBlockResult
from sedaro.results.utils import hfill, HFILL, ENGINE_EXPANSION


class SedaroAgentResult:

    def __init__(self, name: str, block_structures: dict, series: dict):
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

    def to_file(self, filename: Union[str, Path]) -> None:
        '''Save agent result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {
                'name': self.__name,
                'block_structures': self.__block_structures,
                'series': self.__series,
            }
            json.dump(contents, json_file)
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
        print("❓ Query block results with .block(<ID>) or .block(<PARTIAL_ID>)")
