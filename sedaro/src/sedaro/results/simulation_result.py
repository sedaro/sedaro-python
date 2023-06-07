
import datetime as dt
import gzip
import json
from pathlib import Path
from typing import List, Union

from .agent import SedaroAgentResult
from .utils import (HFILL, STATUS_ICON_MAP, _get_agent_id_name_map,
                    _restructure_data, hfill)


class SimulationResult:

    def __init__(self, simulation: dict, data: dict):
        '''Initialize a new Simulation Result.

        See the following class methods for alternate initialization:
            - from_file
        '''
        self.__simulation = {
            'id': simulation.get('id', None),
            'branch': simulation['branch'],
            'dateCreated': simulation['dateCreated'],
            'dateModified': simulation['dateModified'],
            'status': str(simulation['status']),
        }
        self.__branch = simulation['branch']
        self.__data = data
        self.__meta = data['meta']
        raw_series = data['series']
        agent_id_name_map = _get_agent_id_name_map(self.__meta)
        self.__simpleseries, self._agent_blocks = _restructure_data(raw_series, agent_id_name_map, self.__meta)

    def __repr__(self) -> str:
        return f'SedaroSimulationResult(branch={self.__branch}, status={self.status})'

    @property
    def id(self):
        return self.__simulation['id']

    @property
    def templated_agents(self) -> List[str]:
        return tuple([
            entry['name'] for _, entry
            in self.__meta['structure']['scenario']['blocks'].items()
            if entry['type'] == 'Agent' and not entry['peripheral']
        ])

    @property
    def peripheral_agents(self) -> List[str]:
        return tuple([
            entry['name'] for _, entry
            in self.__meta['structure']['scenario']['blocks'].items()
            if entry['type'] == 'Agent' and entry['peripheral']
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
            if entry['type'] == 'Agent' and name == entry['name']:
                return id_
        else:
            raise ValueError(f"Agent {name} not found in data set.")

    def agent(self, name: str) -> SedaroAgentResult:
        '''Query results for a particular agent by name.'''
        agent_id = self.__agent_id_from_name(name)
        initial_agent_models = self.__meta['structure']['agents']
        initial_state = initial_agent_models[agent_id] if agent_id in initial_agent_models else None
        return SedaroAgentResult(name, self._agent_blocks[agent_id], self.__simpleseries[name], initial_state=initial_state)

    def to_file(self, filename: Union[str, Path]) -> None:
        '''Save simulation result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'data': self.__data, 'simulation': self.__simulation}
            json.dump(contents, json_file)
            print(f"💾 Successfully saved to {filename}")

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

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load simulation result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return SimulationResult(contents['simulation'], contents['data'])
