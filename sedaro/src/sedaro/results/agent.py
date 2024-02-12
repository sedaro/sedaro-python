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
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, hfill


class SedaroAgentResult:

    def __initialize_block_structure(self):
        '''Initialize the block structure for this agent.'''
        columns = {}
        for module in self.__series:
            columns[module] = self.__series[module].columns.tolist()
        column_mapping = {}
        for module in columns:
            for column in columns[module]:
                if column != 'time':
                    assert column not in column_mapping
                    column_mapping[column] = module
        return column_mapping

    def __init__(self, name: str, block_structures: dict, series: dict, structure: dict, initial_state: dict = None):
        '''Initialize a new agent result.

        Agent results are typically created through the .agent method of
        SedaroSimulationResult or the .from_file method of this class.
        '''
        self.__name = name
        for k in series:
            self.__agent_uuid = k.split('/')[0]
            break
        self.__structure = structure
        self.__block_structures = block_structures
        self.__series = series
        self.__block_uuids = {}
        for block_uuid in self.__structure['agents'][self.__agent_uuid]['blocks']:
            if 'name' in self.__structure['agents'][self.__agent_uuid]['blocks'][block_uuid]:
                self.__block_uuids[block_uuid] = self.__structure['agents'][self.__agent_uuid]['blocks'][block_uuid]['name']
            else:
                self.__block_uuids[block_uuid] = None
        self.__block_ids = sorted(set(
            block_id.split('.')[0] if block_id.split('.')[0] in self.__block_uuids else 'root'
            for module in self.__series
            for block_id in self.__series[module].columns.tolist()
        ),
            reverse=True
        )
        self.__initial_state = initial_state
        self.__column_mapping = self.__initialize_block_structure()

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

        column_block_lists = {}
        for column in self.__column_mapping:
            if (id_ != 'root' and column.split('.')[0] == id_) or (id_ == 'root' and column.split('.')[0] not in self.__block_uuids):
                column_dataframe = self.__column_mapping[column]
                if column_dataframe not in column_block_lists:
                    column_block_lists[column_dataframe] = []
                column_block_lists[column_dataframe].append(column)

        block_data = {}
        for module in self.__series:
            if module in column_block_lists:
                block_data[module] = self.__series[module][column_block_lists[module]]
                if id_ != 'root':
                    # rename columns, removing first part of the column name
                    block_data[module] = block_data[module].rename(columns={column: '.'.join(column.split('.')[1:]) for column in column_block_lists[module]})
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
                    'structure': self.__structure,
                    'initial_state': self.__initial_state,
                    'block_structures': self.__block_structures,
                }, fp)
            os.mkdir(f"{tmpdir}/data")
            for engine in self.__series:
                path = f"{tmpdir}/data/{engine.replace('/', ' ')}"
                df : dd = self.__series[engine]
                df.to_parquet(path)
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
            shutil.move(f"{curr_zip_name}.zip", zip_new_path)
            # remove tmpdir
            shutil.rmtree(tmpdir, ignore_errors=True)
            success = True
            print(f"Successfully archived at {zip_new_path}")
        except Exception as e:
            raise e
        finally:
            if not success:
                shutil.rmtree(tmpdir, ignore_errors=True)

    @classmethod
    def load(cls, filename: Union[str, Path]):
        success = False
        try:
            tmpdir = f".{uuid6.uuid7()}"
            shutil.unpack_archive(filename, tmpdir, 'zip')
            with open(f"{tmpdir}/meta.json", "r") as fp:
                meta = json.load(fp)
                name = meta['name']
                structure = meta['structure']
                block_structures = meta['block_structures']
                initial_state = meta['initial_state']
            engines = {}
            parquets = os.listdir(f"{tmpdir}/data/")
            for agent in parquets:
                df = dd.read_parquet(f"{tmpdir}/data/{agent}")
                engines[agent.replace(' ', '/')] = df
            # remove tmpdir
            shutil.rmtree(tmpdir, ignore_errors=True)
            success = True
        except Exception as e:
            raise e
        finally:
            if not success:
                shutil.rmtree(tmpdir, ignore_errors=True)
        return SedaroAgentResult(name, block_structures, engines, structure, initial_state)

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
        print('    ' + '-' * 58)
        print('    |' + 'id'.center(38) + 'name'.center(30-12) + '|')
        print('    ' + '-' * 58)
        for block_id in self.__block_ids:
            if block_id != 'root':
                block_name = self.__block_uuids[block_id]
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
