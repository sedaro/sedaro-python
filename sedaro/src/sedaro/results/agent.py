import dask.dataframe as dd
import gzip
import json
import os
from pathlib import Path
import shutil
from typing import Generator, List, Union
import uuid6

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

    def save(self, filename: Union[str, Path]):
        success = False
        try:
            tmpdir = f".{uuid6.uuid7()}"
            os.mkdir(tmpdir)
            with open(f"{tmpdir}/meta.json", "w") as fp:
                json.dump({
                    'name': self.__name,
                    'initial_state': self.__initial_state,
                    'block_structures': self.__block_structures,
                }, fp)
            os.mkdir(f"{tmpdir}/data")
            for engine in self.__series:
                path = f"{tmpdir}/data/{engine}"
                df : dd = self.__series[engine]
                df.to_parquet(path.replace('/', ' '))
            shutil.make_archive(tmpzip := f".{uuid6.uuid7()}", 'zip', tmpdir)
            curr_zip_base = ''
            # if the path is to another directory, make that directory if nonexistent, and move the zip there
            if len(path_split := filename.split('/')) > 1:
                path_dirs = '/'.join(path_split[:-1])
                Path(path_dirs).mkdir(parents=True, exist_ok=True)
                shutil.move(f"{tmpzip}.zip", f"{(curr_zip_base := path_dirs)}/{tmpzip}.zip")
                zip_desired_name = path_split[-1]
            else:
                zip_desired_name = filename
            # rename zip to specified name
            if len(curr_zip_base) > 0:
                zip_new_path = f"{curr_zip_base}/{zip_desired_name}"
                curr_zip_name = f"{curr_zip_base}/{tmpzip}"
            else:
                zip_new_path = zip_desired_name
                curr_zip_name = tmpzip
            shutil.move(f"{curr_zip_name}.zip", f"{zip_new_path}.zip")
            # remove tmpdir
            os.system(f"rm -r {tmpdir}")
            success = True
            print(f"Successfully archived at {zip_new_path}")
        except Exception as e:
            raise e
        finally:
            if not success:
                os.system(f"rm -r {tmpdir}")

    @classmethod
    def load(cls, filename: Union[str, Path]):
        try:
            tmpdir = f".{uuid6.uuid7()}"
            shutil.unpack_archive(filename, tmpdir, 'zip')
            with open(f"{tmpdir}/meta.json", "r") as fp:
                meta = json.load(fp)
                name = meta['name']
                block_structures = meta['block_structures']
                initial_state = meta['initial_state']
            engines = {}
            parquets = os.listdir(f"{tmpdir}/data/")
            for agent in parquets:
                df = dd.read_parquet(f"{tmpdir}/data/{agent}")
                engines[agent.replace(' ', '/')] = df
        except Exception as e:
            raise e
        return SedaroAgentResult(name, block_structures, engines, initial_state)

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
