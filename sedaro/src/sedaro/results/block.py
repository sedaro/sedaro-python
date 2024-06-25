import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Generator, Union

from .series import SedaroSeries
from .utils import (ENGINE_EXPANSION, ENGINE_MAP, HFILL,
                    FromFileAndToFileAreDeprecated, get_column_names,
                    get_parquets, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd


class SedaroBlockResult(FromFileAndToFileAreDeprecated):

    def __init__(self, structure, series: dict, stats: dict, column_index: dict, prefix: str, stats_to_plot: list = None):
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
        for k in stats:
            self.__stats[k] = {kk: vv for kk, vv in stats[k].items() if kk.startswith(prefix)}
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

    def save(self, path: Union[str, Path]):
        '''Save the block result to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(
                    f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SedaroBlockResult'}, fp)
        os.mkdir(f"{path}/data")
        parquet_files = []
        for engine in self.__series:
            engine_parquet_path = f"{path}/data/{(pname := engine.replace('/', '.'))}"
            parquet_files.append(pname)
            df: 'dd' = self.__series[engine]
            df.to_parquet(engine_parquet_path)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({
                'structure': self.__structure,
                'column_index': self.__column_index,
                'prefix': self.__prefix,
                'parquet_files': parquet_files,
                'stats': self.__stats,
            }, fp)
        print(f"Block result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a block result from the specified path.'''
        import dask.dataframe as dd

        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SedaroBlockResult':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        with open(f"{path}/meta.json", "r") as fp:
            meta = json.load(fp)
            structure = meta['structure']
            column_index = meta['column_index']
            prefix = meta['prefix']
            stats = meta['stats'] if 'stats' in meta else {}
        engines = {}
        try:
            for agent in meta['parquet_files']:
                df = dd.read_parquet(f"{path}/data/{agent}")
                engines[agent.replace('.', '/')] = df
        except KeyError:
            for agent in get_parquets(f"{path}/data/"):
                df = dd.read_parquet(f"{path}/data/{agent}")
                engines[agent.replace('.', '/')] = df
        return cls(structure, engines, stats, column_index, prefix)

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
        print("❓ Query statistics with .<VARIABLE_NAME>.stats('<STAT_NAME_1>', '<STAT_NAME_2>', ...)")
        print("📊 Variables with statistics available are marked with a \033[0;32m*\033[0;0m")

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