import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Generator, List, Union

from pydash import merge

from .block import SedaroBlockResult
from .utils import (ENGINE_EXPANSION, ENGINE_MAP, HFILL, SedaroResultBase, bsearch, get_parquets, get_static_data,
                    get_static_data_engines, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd


class SedaroAgentResult(SedaroResultBase):
    def __init__(
        self,
        name: str,
        block_structures: dict,
        series: dict,
        column_index: dict,
        initial_state: dict = None,
        stats: dict = None,
        stats_to_plot: list = None,
        static_data: dict[str: dict] = None,
    ):
        '''Initialize a new agent result.

        Agent results are typically created through the .agent method of
        SedaroSimulationResult or the .from_file method of this class.
        '''
        self.__name = name
        self.__column_index = column_index
        self.__block_structures = block_structures
        self.__series = series
        self.__stats = stats if stats is not None else {}
        self.__static_data = static_data if static_data is not None else {}
        self.__block_uuids = [k for k in self.__column_index]
        self.__block_ids = sorted(set(
            block_id.split('.')[0] if block_id.split('.')[0] in self.__block_uuids else 'root'
            for module in self.__series
            for block_id in self.__series[module].columns.tolist()
        ),
            reverse=True
        )
        self.__initial_state = initial_state
        self.stats_to_plot = stats_to_plot if stats_to_plot is not None else []

    def __iter__(self) -> Generator:
        '''Iterate through blocks on this agent.'''
        return (self.block(id_) for id_ in self.__block_ids)

    def __contains__(self, id_: str) -> bool:
        '''Check if this agent result contains a certain block ID.'''
        return id_ in self.__block_ids

    @property
    def dataframe(self) -> 'Dict[str, dd.DataFrame]':
        '''Get the raw Dask DataFrames for this agent.'''
        return self.__series

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

        prefix = '' if id_ == 'root' else id_ + '.'
        block_structure = self.__block_structures[id_] if id_ != 'root' else id_
        block_streams = {}
        for stream in self.__series:
            if stream in self.__column_index[id_]:
                block_streams[stream] = self.__series[stream]
        static_data_for_block = {}
        for stream in self.__static_data:
            static_data_for_block[stream] = {k: v for k,
                v in self.__static_data[stream].items() if k.startswith(prefix)}
        return SedaroBlockResult(block_structure, block_streams, self.__stats, self.__column_index[id_],
            prefix, self.stats_to_plot, static_data_for_block)

    def do_save(self, path: Union[str, Path]):
        '''Called by base class's `save` method. Saves the agent's series data, and returns associated metadata.'''
        os.mkdir(data_subdir_path := self.data_subdir(path))
        parquet_files = []
        for engine in self.__series:
            engine_parquet_path = f"{data_subdir_path}/{(pq_filename := engine.replace('/', '.'))}"
            parquet_files.append(pq_filename)
            df: 'dd' = self.__series[engine]
            df.to_parquet(engine_parquet_path)
        return {
            'name': self.__name,
            'initial_state': self.__initial_state,
            'block_structures': self.__block_structures,
            'column_index': self.__column_index,
            'parquet_files': parquet_files,
            'stats': self.__stats,
            'static': self.__static_data,
        }

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load an agent result from the specified path.'''
        import dask.dataframe as dd

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
            stats = meta['stats'] if 'stats' in meta else {}
            static_data = meta['static'] if 'static' in meta else {}
        engines = {}
        try:
            for engine in meta['parquet_files']:
                df = dd.read_parquet(f"{path}/data/{engine}")
                engines[engine.replace('.', '/')] = df
        except KeyError:
            for engine in get_parquets(f"{path}/data/"):
                df = dd.read_parquet(f"{path}/data/{engine}")
                engines[engine.replace('.', '/')] = df
        return cls(name, block_structures, engines, column_index, initial_state, stats, static_data=static_data)

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
        print('    ' + '-' * 91)
        print('    |' + 'id'.center(30) + 'type'.center(24) + 'name'.center(35) + '|')
        print('    ' + '-' * 91)
        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_structures[block_id].get('name', None)
                block_id_col = f"{block_id[:26]}"
                block_type = self.__block_structures[block_id].get('type', None)
                if block_name is not None:
                    name_id_col = f'{block_name[:25]}'
                else:
                    name_id_col = f'<Unnamed Block>'
                if block_type is not None:
                    type_id_col = f'{block_type[:30]}'
                else:
                    type_id_col = f'<Untyped Block>'
            else:
                block_id_col = f"root"
                name_id_col = ''
                type_id_col = ''
            print(f"    | {block_id_col:26s} | {type_id_col:30s} | {name_id_col:25s} |")
        print('    ' + '-' * 91)

        no_data_blocks = len(self.__block_structures) - len(self.__block_ids)
        if no_data_blocks > 0:
            print(f"\n    {no_data_blocks} block(s) with no associated data")

        hfill()
        print("❓ Query block results with .block(<ID>) or .block(<PARTIAL_ID>)")
        if self.__static_data:
            hfill()
            engines_as_text = ", ".join(get_static_data_engines(self.__static_data))
            print(f"📦 Static data is available for this agent in the following engine(s): {engines_as_text}.")
            print("📦 Query with .static_data('<ENGINE_NAME>') for that engine's static data on this agent,")
            print("   or .static_data() to get this agent's static data for all engines.")

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

    def static_data(self, engine=None):
        return get_static_data(self.__static_data, "Agent", engine=engine)
