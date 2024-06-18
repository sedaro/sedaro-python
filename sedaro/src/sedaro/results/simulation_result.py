import datetime as dt
import json
import os
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Union

from ..settings import STATUS, SUCCEEDED
from ..stats.stats import SimulationStats
from .agent import SedaroAgentResult
from .utils import (HFILL, STATUS_ICON_MAP, FromFileAndToFileAreDeprecated,
                    _block_type_in_supers, _get_agent_id_name_map,
                    _restructure_data, get_parquets, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd


class SimulationResult(FromFileAndToFileAreDeprecated):

    def __init__(self, simulation: dict, data: dict):
        '''Initialize a new Simulation Result using methods on the `simulation` property of a `ScenarioBranch`.

        See the `from_file` class method on this class for alternate initialization.
        '''
        self.__simulation = {
            'id': simulation.get('id', None),
            'branch': simulation['branch'],
            'dateCreated': simulation['dateCreated'],
            'dateModified': simulation['dateModified'],
            STATUS: str(simulation[STATUS]),
        }
        self.__branch = simulation['branch']
        self.__data = data
        self.__meta: dict = data['meta']
        self.stats: SimulationStats = SimulationStats(data['stats'])
        raw_series = data['series']
        agent_id_name_map = _get_agent_id_name_map(self.__meta)
        self.__agent_ids, self.__block_structures, self.__column_index = _restructure_data(
            raw_series, agent_id_name_map, self.__meta)

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
    def dataframe(self) -> 'Dict[str, dd.DataFrame]':
        '''Get the raw Dask DataFrames for this SimulationResult.'''
        return self.__data['series']

    @property
    def status(self) -> str:
        return str(self.__simulation[STATUS])

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
        return str(self.__simulation[STATUS]) == SUCCEEDED

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

    def agent(self, id_or_name: str) -> SedaroAgentResult:
        '''Query results for a particular agent by name or ID. In the event that an agent's name is the same as another agent's ID, the agent with the ID that matches the given string will be used.'''
        if id_or_name in self.__agent_ids:
            agent_id, name = id_or_name, self.__agent_ids[id_or_name]
        else:
            try:
                agent_id, name = self.__agent_id_from_name(id_or_name), id_or_name
            except ValueError:
                raise ValueError(f"Agent with `id` or `name` '{id_or_name}' not found in data set.")
        agent_dataframes = {}
        for stream_id in self.__data['series']:
            if stream_id.startswith(agent_id):
                agent_dataframes[stream_id] = self.__data['series'][stream_id]
        initial_agent_models = self.__meta['structure']['agents']
        initial_state = initial_agent_models[agent_id] if agent_id in initial_agent_models else None
        return SedaroAgentResult(name, self.__block_structures[agent_id], agent_dataframes, self.__column_index[agent_id], initial_state=initial_state)

    def save(self, path: Union[str, Path]):
        '''Save the simulation result to a directory with the specified path.'''
        try:
            os.makedirs(path)
        except FileExistsError:
            if not (os.path.isdir(path) and any(os.scandir(path))):
                raise FileExistsError(
                    f"A file or non-empty directory already exists at {path}. Please specify a different path.")
        with open(f"{path}/class.json", "w") as fp:
            json.dump({'class': 'SimulationResult'}, fp)
        os.mkdir(f"{path}/data")
        parquet_files = []
        for agent in self.__data['series']:
            agent_parquet_path = f"{path}/data/{(pname := agent.replace('/', '.'))}"
            parquet_files.append(pname)
            df: 'dd' = self.__data['series'][agent]
            df.to_parquet(agent_parquet_path)
        with open(f"{path}/meta.json", "w") as fp:
            json.dump({'meta': self.__data['meta'], 'simulation': self.__simulation,
                      'parquet_files': parquet_files}, fp)
        print(f"Simulation result saved to {path}.")

    @classmethod
    def load(cls, path: Union[str, Path]):
        '''Load a simulation result from the specified path.'''
        import dask.dataframe as dd
        with open(f"{path}/class.json", "r") as fp:
            archive_type = json.load(fp)['class']
            if archive_type != 'SimulationResult':
                raise ValueError(f"Archive at {path} is a {archive_type}. Please use {archive_type}.load instead.")
        data = {}
        with open(f"{path}/meta.json", "r") as fp:
            contents = json.load(fp)
            simulation = contents['simulation']
            data['meta'] = contents['meta']
        data['series'] = {}
        try:
            for agent in contents['parquet_files']:
                df = dd.read_parquet(f"{path}/data/{agent}")
                data['series'][agent.replace('.', '/')] = df
        except KeyError:
            for agent in get_parquets(f"{path}/data/"):
                df = dd.read_parquet(f"{path}/data/{agent}")
                data['series'][agent.replace('.', '/')] = df
        return cls(simulation, data)

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
