
import dask.dataframe as dd
import datetime as dt
import json
import os
from pathlib import Path
import shutil
from typing import Dict, List, Union
import uuid6

from .agent import SedaroAgentResult
from .utils import (HFILL, STATUS_ICON_MAP, _block_type_in_supers,
                    _get_agent_id_name_map, _restructure_data, hfill, to_time_major)


class SimulationResult:

    def __init__(self, simulation: dict, data: dict):
        '''Initialize a new Simulation Result using methods on the `simulation` property of a `ScenarioBranch`.

        See the `from_file` class method on this class for alternate initialization.
        '''
        self.__simulation = {
            'id': simulation.get('id', None),
            'branch': simulation['branch'],
            'dateCreated': simulation['dateCreated'],
            'dateModified': simulation['dateModified'],
            'status': str(simulation['status']),
        }
        self.__branch = simulation['branch']
        self.___simulation = simulation
        self.___data = data
        self.__meta: Dict = data['meta']
        raw_series = data['series']
        agent_id_name_map = _get_agent_id_name_map(self.__meta)
        self.__dataframes, self.__agent_ids = _restructure_data(raw_series, agent_id_name_map)

    def __repr__(self) -> str:
        return f'SedaroSimulationResult(branch={self.__branch}, status={self.status})'

    @property
    def job_id(self):
        return self.__simulation['id']

    @property
    def data_array_id(self):
        return self.__meta.get('id', None)

    @property
    def templated_agents(self) -> List[str]:
        return tuple([
            entry['name'] for _, entry
            in self.__meta['structure']['scenario']['blocks'].items()
            if _block_type_in_supers(entry['type'], self.__meta['structure']['scenario']['_supers'], super_type='TemplatedAgent')
        ])

    @property
    def peripheral_agents(self) -> List[str]:
        return tuple([
            entry['name'] for id_, entry
            in self.__meta['structure']['scenario']['blocks'].items()
            if _block_type_in_supers(entry['type'], self.__meta['structure']['scenario']['_supers'], super_type='PeripheralAgent') and id_ in self.__agent_ids
        ])

    @property
    def status(self) -> str:
        return str(self.__simulation['status'])

    @property
    def start_time(self) -> dt.datetime:
        return dt.datetime.strptime(self.__simulation['dateCreated'], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def end_time(self) -> dt.datetime:
        return dt.datetime.strptime(self.__simulation['dateModified'], "%Y-%m-%dT%H:%M:%S.%fZ")

    @property
    def run_time(self) -> float:
        return (self.end_time - self.start_time).total_seconds()

    @property
    def success(self) -> bool:
        return str(self.__simulation['status']) == 'SUCCEEDED'

    def __assert_success(self) -> None:
        if not self.success:
            raise ValueError(
                'This operation cannot be completed because the simulation hasn\'t finished or failed early.')

    def __agent_id_from_name(self, name: str) -> str:
        for id_, entry in self.__meta['structure']['scenario']['blocks'].items():
            if name == entry.get('name') and _block_type_in_supers(entry['type'], self.__meta['structure']['scenario']['_supers']):
                if id_ in self.__agent_ids:
                    return id_
        else:
            raise ValueError(f"Agent {name} not found in data set.")

    def agent(self, name: str) -> SedaroAgentResult:
        '''Query results for a particular agent by name.'''
        agent_id = self.__agent_id_from_name(name)
        initial_agent_models = self.__meta['structure']['agents']
        initial_state = initial_agent_models[agent_id] if agent_id in initial_agent_models else None
        return SedaroAgentResult(name, self.__agent_ids[agent_id], self.__dataframes[name], initial_state=initial_state)

    # def to_file(self, filename: Union[str, Path]) -> None:
    #     '''Save simulation result to compressed JSON file.'''
    #     with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
    #         contents = {'data': self.__data, 'simulation': self.__simulation}
    #         json.dump(contents, json_file)
    #         print(f"💾 Successfully saved to {filename}")

    # @classmethod
    # def from_file(cls, filename: Union[str, Path]):
    #     '''Load simulation result from compressed JSON file.'''
    #     with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
    #         contents = json.load(json_file)
    #         return SimulationResult(contents['simulation'], contents['data'])

    def save(self, filename: Union[str, Path]):
        success = False
        try:
            tmpdir = f".{uuid6.uuid7()}"
            os.mkdir(tmpdir)
            with open(f"{tmpdir}/simulation.json", "w") as fp:
                json.dump(self.___simulation, fp)
            with open(f"{tmpdir}/meta.json", "w") as fp:
                json.dump(self.___data['meta'], fp)
            os.mkdir(f"{tmpdir}/data")
            for agent in self.___data['series']:
                path = f"{tmpdir}/data/{agent}"
                df : dd = self.___data['series'][agent]
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
            os.rename(f"{curr_zip_name}.zip", zip_new_path)
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
        NotImplemented

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print(f'Sedaro Simulation Result Summary'.center(HFILL))
        hfill()
        print(
            f'{STATUS_ICON_MAP[self.status]} Simulation {self.status.lower()} after {self.run_time:.1f}s')

        agents = self.templated_agents
        if len(agents) > 0:
            print('\n🛰️ Templated Agents ')
            for entry in agents:
                print(f'    • {entry}')

        agents = self.peripheral_agents
        if len(agents) > 0:
            print('\n📡 Peripheral Agents ')
            for entry in agents:
                print(f'    • {entry}')

        hfill()
        print("❓ Query agent results with .agent(<NAME>)")
