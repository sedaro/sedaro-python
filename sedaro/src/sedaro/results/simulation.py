
import datetime as dt
import gzip
import json
import time
from pathlib import Path
from typing import List, Optional, Tuple, Union

from sedaro import SedaroApiClient
from sedaro.results.agent import SedaroAgentResult
from sedaro.results.utils import (HFILL, STATUS_ICON_MAP,
                                  _get_agent_id_name_map, _restructure_data,
                                  hfill, progress_bar)


class SedaroSimulationResult:

    def __init__(self, simulation: dict, data: dict):
        '''Initialize a new Simulation Result.

        See the following class methods for simple initialization:
            - get_scenario_latest
            - poll_scenario_latest
            - from_file
        '''
        self.__simulation = {
            'branch': simulation['branch'],
            'dateCreated': simulation['dateCreated'],
            'dateModified': simulation['dateModified'],
            'status': str(simulation['status']),
        }
        self.__data = data
        self.__branch = simulation['branch']
        if self.success:
            self.__meta = data['meta']
            raw_series = data['series']
            agent_id_name_map = _get_agent_id_name_map(self.__meta)
            self.__simpleseries, self._agent_blocks = _restructure_data(raw_series, agent_id_name_map, self.__meta)
        else:
            self.__meta = None
            self.__simpleseries = None
            self._agent_blocks = None

    def __repr__(self) -> str:
        return f'SedaroSimulationResult(branch={self.__branch}, status={self.status})'

    @classmethod
    def get_scenario_latest(
        cls,
        api_key: str,
        scenario_id: int,
        host: str = 'https://api.sedaro.com',
        streams: Optional[List[Tuple[str, ...]]] = None
    ):
        '''Query latest scenario result.'''
        streams = streams or []
        with SedaroApiClient(api_key=api_key, host=host) as sedaro_client:
            simulation = cls.__get_simulation(sedaro_client, scenario_id)
            if simulation['status'] == 'SUCCEEDED':
                data = sedaro_client.get_data(simulation['dataArray'], streams=streams)
            else:
                data = None
            return cls(simulation, data)

    @classmethod
    def poll_scenario_latest(
        cls,
        api_key: str,
        scenario_id: int,
        host: str = 'https://api.sedaro.com',
        streams: Optional[List[Tuple[str, ...]]] = None,
        retry_interval: int = 2
    ):
        '''Query latest scenario result and wait for sim if it is running.'''
        streams = streams or []
        with SedaroApiClient(api_key=api_key, host=host) as sedaro_client:
            simulation = cls.__get_simulation(sedaro_client, scenario_id)

            while simulation['status'] in ('PENDING', 'RUNNING'):
                simulation = cls.__get_simulation(sedaro_client, scenario_id)
                progress_bar(simulation['progress']['percentComplete'])
                time.sleep(retry_interval)

            return cls.get_scenario_latest(api_key, scenario_id, host=host, streams=streams)

    @staticmethod
    def __get_simulation(client, scenario_id: int) -> dict:
        try:
            sim = client.get_sim_client(scenario_id)
            return sim.get_latest()[0]
        except IndexError:
            raise IndexError(
                f'Could not find any simulation results for scenario: {scenario_id}')

    @property
    def templated_agents(self) -> List[str]:
        self.__assert_success()
        return tuple([
            entry['name'] for _, entry
            in self.__meta['structure']['scenario']['blocks'].items()
            if entry['type'] == 'Agent' and not entry['peripheral']
        ])

    @property
    def peripheral_agents(self) -> List[str]:
        self.__assert_success()
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
                'This operation cannot be completed because the simulation failed.')

    def __agent_id_from_name(self, name: str) -> str:
        for id_, entry in self.__meta['structure']['scenario']['blocks'].items():
            if entry['type'] == 'Agent' and name == entry['name']:
                return id_
        else:
            raise ValueError(f"Agent {name} not found in data set.")

    def agent(self, name: str) -> SedaroAgentResult:
        '''Query results for a particular agent by name.'''
        self.__assert_success()
        agent_id = self.__agent_id_from_name(name)
        return SedaroAgentResult(name, self._agent_blocks[agent_id], self.__simpleseries[name])

    def to_file(self, filename: Union[str, Path]) -> None:
        '''Save simulation result to compressed JSON file.'''
        with gzip.open(filename, 'xt', encoding='UTF-8') as json_file:
            contents = {'data': self.__data, 'simulation': self.__simulation}
            json.dump(contents, json_file)
            print(f"💾 Successfully saved to {filename}")

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        '''Load simulation result from compressed JSON file.'''
        with gzip.open(filename, 'rt', encoding='UTF-8') as json_file:
            contents = json.load(json_file)
            return cls(contents['simulation'], contents['data'])

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
