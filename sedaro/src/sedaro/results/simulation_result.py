import datetime as dt
import json
import os
import time
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, Union

from ..branches.scenario_branch.utils import _get_stats_for_sim_id
from ..settings import STATUS, SUCCEEDED
from .agent import SedaroAgentResult
from .utils import (HFILL, STATUS_ICON_MAP, SedaroResultBase, _block_type_in_supers, _get_agent_id_name_map,
                    _restructure_data, get_parquets, hfill)

if TYPE_CHECKING:
    import dask.dataframe as dd

    from ..sedaro_api_client import SedaroApiClient


class SimulationResult(SedaroResultBase):

    def __init__(self, simulation: dict, data: dict, _sedaro: 'SedaroApiClient' = None, stats_fetched: bool = False):
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
        self.__sedaro = _sedaro
        self.__branch = simulation['branch']
        self.__data = data
        self.__meta: dict = data['meta']
        self.__stats_fetched = ('stats_fetched' in data and data['meta']['stats_fetched']) or (
            'stats' in data and data['stats'])
        self.__stats = data['stats'] if 'stats' in data else {}
        self.__static_data: dict = data['static'] if 'static' in data else {}
        self.stats_to_plot = []
        raw_series = data['series']
        agent_id_name_map = _get_agent_id_name_map(self.__meta)
        self.__agent_ids, self.__block_structures, self.__column_index = _restructure_data(
            raw_series, agent_id_name_map, self.__meta)

    def __repr__(self) -> str:
        return f'SedaroSimulationResult(branch={self.__branch}, status={self.status})'

    def fetch_stats(self, wait=False):
        '''Fetch the stats for this SimulationResult.

        If `wait` is True, this method will block until the stats are ready.
        '''
        if self.__stats_fetched:
            print("Stats already fetched.")
            return
        if self.__sedaro is None:
            raise Exception("Fetching summary stats after loading from save is not currently supported.")
        result, success = _get_stats_for_sim_id(self.__sedaro, self.__meta['id'])
        if success:
            self.__stats = result
            self.__stats_fetched = True
        else:
            if wait:
                POLLING_INTERVAL = 2.0
                while not success:
                    time.sleep(POLLING_INTERVAL)
                    result, success = _get_stats_for_sim_id(self.__sedaro, self.__meta['id'])
                self.__stats = result
                self.__stats_fetched = True
            else:
                raise Exception("Failed to fetch summary stats for simulation. Stats are not yet ready.")
        print("Stats fetched.")

    @property
    def stats_fetched(self) -> bool:
        return self.__stats_fetched

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
                raise ValueError(
                    f"Agent with `id` or `name` '{id_or_name}' not found in data set. If an expected agent is missing, the simulation may have terminated early.")
        agent_dataframes = {}
        for stream_id in self.__data['series']:
            if stream_id.startswith(agent_id):
                agent_dataframes[stream_id] = self.__data['series'][stream_id]
        initial_agent_models = self.__meta['structure']['agents']
        initial_state = initial_agent_models[agent_id] if agent_id in initial_agent_models else None
        filtered_stats = {k: v for k, v in self.__stats.items() if k.startswith(agent_id)}
        filtered_static_data = {k: v for k, v in self.__static_data.items() if k.startswith(agent_id)}
        return SedaroAgentResult(
            name,
            self.__block_structures[agent_id],
            agent_dataframes,
            self.__column_index[agent_id],
            initial_state=initial_state,
            stats=filtered_stats,
            stats_to_plot=self.stats_to_plot,
            static_data=filtered_static_data,
        )

    def do_save(self, path: Union[str, Path]):
        '''Called by base class's `save` method. Saves the simulation result's series data, and returns associated metadata.'''
        parquet_files = self.save_parquets(self.__data['series'], path)
        return {
            'meta': self.__data['meta'],
            'simulation': self.__simulation,
            'stats': self.__stats,
            'static': self.__static_data,
            'parquet_files': parquet_files,
        }

    @classmethod
    def do_load(cls, path: Union[str, Path], metadata: dict) -> 'SimulationResult':
        '''Load a simulation result's data from the specified path and return a SimulationResult object.'''
        data = {}
        data['meta'] = metadata['meta']
        data['stats'] = metadata['stats'] if 'stats' in metadata else {}
        data['static'] = metadata['static'] if 'static' in metadata else {}
        data['series'] = {}
        simulation = metadata['simulation']

        import dask.dataframe as dd
        data_subdir_path = cls.data_subdir(path)
        try:
            for agent in metadata['parquet_files']:
                df = dd.read_parquet(f"{data_subdir_path}/{agent}")
                data['series'][agent.replace('.', '/')] = df
        except KeyError:
            for agent in get_parquets(f"{data_subdir_path}/"):
                df = dd.read_parquet(f"{data_subdir_path}/{agent}")
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
