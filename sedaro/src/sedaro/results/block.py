import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Generator, Union

from .series import SedaroSeries
from .utils import (ENGINE_EXPANSION, ENGINE_MAP, HFILL, SedaroResultBase, get_column_names, get_parquets,
                    get_static_data, get_static_data_engines, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd


class SedaroBlockResult(SedaroResultBase):

    def __init__(
        self,
        structure,
        series: dict,
        stats: dict,
        column_index: dict,
        prefix: str,
        stats_to_plot: list = None,
        static_data: dict[str: dict] = None,
    ):
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
        self.__stats = {}
        if stats is None:
            stats = {}
        for k in stats:
            self.__stats[k] = {kk: vv for kk, vv in stats[k].items() if kk.startswith(prefix)}
        self.__static_data = static_data if static_data is not None else {}
        self.__column_index = column_index
        self.__prefix = prefix
        self.__variables = []
        for stream in self.__column_index:
            for variable in self.__column_index[stream]:
                self.__variables.append(variable)
        self.__variables = sorted(list(self.__variables))
        self.stats_to_plot = stats_to_plot if stats_to_plot is not None else []

    def __getattr__(self, name: str) -> SedaroSeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        prefix = f"{self.__prefix}{name}"
        for stream in self.__column_index:
            if name in self.__column_index[stream]:
                flattened_stats = {}
                for engine in self.__stats:
                    for k in self.__stats[engine]:
                        flattened_stats[k] = self.__stats[engine][k]
                return SedaroSeries(
                    name,
                    self.__series[stream],
                    flattened_stats,
                    self.__column_index[stream][name],
                    prefix,
                    self.stats_to_plot,
                    self.__name
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

    def subst_name(self, key):
        if self.__name == '<Unnamed Block>':
            return key
        else:
            return '.'.join([self.__name] + key.split('.')[1:])

    @property
    def name(self):
        return self.__name

    @property
    def dataframe(self) -> 'Dict[str, dd.DataFrame]':
        '''Get the raw Dask DataFrames for this block.'''
        # only include columns in this block, not columns in the dataframes that are for other blocks
        scoped_data = {}
        for stream in self.__series:
            column_names = get_column_names(self.__column_index[stream], self.__prefix)
            scoped_data[stream] = self.__series[stream][column_names]
        return scoped_data

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

    def _do_save(self, path: Union[str, Path]):
        '''Called by base class's `save` method. Saves the block's series data, and returns associated metadata.'''
        parquet_files = self.save_parquets(self.__series, path)
        return {
            'structure': self.__structure,
            'column_index': self.__column_index,
            'prefix': self.__prefix,
            'parquet_files': parquet_files,
            'stats': self.__stats,
            'static': self.__static_data,
        }

    @classmethod
    def _do_load(cls, path: Union[str, Path], metadata: dict) -> 'SedaroBlockResult':
        '''Load a block's data from the specified path and return a SedaroBlockResult object.'''
        engines = cls.load_parquets(path, metadata)
        # build the block result
        return cls(
            metadata['structure'],
            engines,
            metadata['stats'] if 'stats' in metadata else {},
            metadata['column_index'],
            metadata['prefix'],
            static_data=metadata['static'] if 'static' in metadata else {},
        )

    def __has_stats(self, variable: str) -> bool:
        for engine in self.__stats:
            for series in self.__stats[engine]:
                if series.startswith(self.__prefix + variable):
                    return True
        return False

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
            stats_marker = '\033[0;32m*\033[0;0m' if self.__has_stats(variable) else ' '
            print(f'    • {stats_marker} {variable}')
        hfill()
        print("❓ Query variables with .<VARIABLE_NAME>")
        if self.__stats:
            print("❓ Query statistics with .<VARIABLE_NAME>.stats('<STAT_NAME_1>', '<STAT_NAME_2>', ...)")
            print("📊 Variables with statistics available are marked with a \033[0;32m*\033[0;0m")
        if self.__static_data:
            hfill()
            engines_as_text = ", ".join(get_static_data_engines(self.__static_data))
            print(f"📦 Static data is available for this block in the following engine(s): {engines_as_text}.")
            print("📦 Query with .static_data('<ENGINE_NAME>') for that engine's static data on this block,")
            print("   or .static_data() to get this block's static data for all engines.")

    def value_at(self, mjd):
        return {variable: self.__getattr__(variable).value_at(mjd) for variable in self.variables}

    def stats(self, *args):
        if len(args) == 0:
            cleaned_stats = {}
            for agent in self.__stats:
                for key in self.__stats[agent]:
                    cleaned_stats[self.subst_name(key)] = self.__stats[agent][key]
            return cleaned_stats
        elif len(args) == 1:
            cleaned_stats = {}
            for agent in self.__stats:
                for key in self.__stats[agent]:
                    cleaned_stats[self.subst_name(key)] = self.__stats[agent][key][args[0]]
            return cleaned_stats
        else:
            dicts_to_return = []
            for arg in args:
                cleaned_stats = {}
                for agent in self.__stats:
                    for key in self.__stats[agent]:
                        cleaned_stats[self.subst_name(key)] = self.__stats[agent][key][arg]
                dicts_to_return.append(cleaned_stats)
            return tuple(dicts_to_return)

    def static_data(self, engine=None):
        return get_static_data(self.__static_data, "Block", engine=engine)
