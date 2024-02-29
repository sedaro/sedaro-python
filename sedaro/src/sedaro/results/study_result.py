import datetime as dt
import numpy as np
import pandas as pd
import os
from pathlib import Path
from typing import List, Optional, Tuple, Union

from sedaro.branches.scenario_branch.sim_client import Simulation
from sedaro.results.simulation_result import SimulationResult
from sedaro.results.utils import HFILL, STATUS_ICON_MAP, hfill

from .study_agent import StudyAgentResult


class StudyResult:

    def __init__(self, study, metadata):
        '''Initialize a new Study Result.

        By default, this class will lazily load simulation results as requested
        and cache them in-memory. Different caching options can be enabled with
        the .set_cache method.
        '''
        self.__study = study
        self.__metadata = metadata
        self.__cache = True
        self.__cache_dir = None
        self.__cached_sim_results = {}
        

    def __repr__(self) -> str:
        return f'SedaroStudyResult(branch={self.branch}, status={self.status}, iterations={self.iterations})'

    def __iter__(self):
        '''Iterate through simulation results.'''
        return (self.result(id_) for id_ in self.job_ids)

    def __contains__(self, id_):
        '''Check if this study contains a certain simulation ID.'''
        return id_ in self.job_ids

    @property
    def id(self) -> int:
        return self.__metadata['id']

    @property
    def branch(self) -> str:
        return self.__metadata['branch']

    @property
    def scenario_hash(self) -> str:
        return self.__metadata['scenarioHash']

    @property
    def status(self) -> str:
        return self.__metadata['status']

    @property
    def date_created(self) -> dt.datetime:
        return dt.datetime.fromisoformat(str(self.__metadata['dateCreated'])[:-1])

    @property
    def date_modified(self) -> dt.datetime:
        return dt.datetime.fromisoformat(str(self.__metadata['dateModified'])[:-1])

    @property
    def job_ids(self) -> List[int]:
        return [entry for entry in self.__metadata['jobs']]

    @property
    def iterations(self) -> int:
        return len(self.__metadata['jobs'])

    def set_cache(self, cache: bool = True, cache_dir: str = None) -> None:
        '''Set caching options for this study result.

        Args:
            cache: Boolean option to turn caching on or off.
            cache_dir: Path to a directory for on-disk caching.
        '''
        self.__cache = cache
        self.__cache_dir = cache_dir
        if self.__cache:
            if cache_dir is not None:
                self.__cache_dir = Path(cache_dir)
                if not self.__cache_dir.is_dir():
                    raise ValueError(f'Cache directory not found: {cache_dir}')
        else:
            if self.__cache_dir is not None:
                raise ValueError(f'Cache directory is defined but caching is off.')
        self.__cached_sim_results = {}

    def sim_result(self, id_: str, streams: Optional[List[Tuple[str, ...]]] = None) -> SimulationResult:
        '''Query results for a particular simulation.'''
        result = None
        engines_selected = ""
        if streams:
            engines_selected = ".".join([ f"{agent_id}_{engine_name}" for agent_id, engine_name in streams])

        cache_string = f"{id_}_{engines_selected}"

        if self.__cache:
            if self.__cache_dir is None:
                if cache_string in self.__cached_sim_results:
                    result = self.__cached_sim_results[cache_string]
            else:
                cache_file = self.__cache_dir / f'sim_{cache_string}.cache'
                if cache_file.exists():
                    result = SimulationResult.from_file(cache_file)

        if result is None:
            print(f'💾 Downloading simulation result id {id_}...', end='')
            result = Simulation(self.__study._sedaro, self.__study._branch).results(id_, streams)
            print('done!')

        if self.__cache:
            if self.__cache_dir is None:
                self.__cached_sim_results[cache_string] = result
            else:
                if not cache_file.exists():
                    result.to_file(cache_file)

        return result  

    @property
    def study_results_dict(self):
        return { job_id: self.sim_result(job_id) for job_id in self.job_ids }

    def compare_agent_block(self, agent, block):
        return


    def clear_cache(self) -> None:
        self.__cached_sim_results = {}
        if self.__cache_dir is not None:
            for file in self.__cache_dir.glob('sim_*.cache'):
                file.unlink()

    def refresh(self) -> None:
        '''Update metadata for this study.'''
        from sedaro.branches.scenario_branch.study_client import Study
        self.__metadata = self.__study.status(self.id)

    def summarize_agents(self):
        for (sim_id, results) in self.study_results_dict.items():
            print(
                f'{sim_id}:{STATUS_ICON_MAP[results.status]} Simulation {results.status.lower()} after {results.run_time:.1f}s')

        first_results = next(iter(self.study_results_dict.values()))

        agents = first_results.templated_agents
        if len(agents) > 0:
            print('\n🛰️ Templated Agents ')
            for entry in agents:
                print(f'    • {entry}')

        agents = first_results.peripheral_agents
        if len(agents) > 0:
            print('\n📡 Peripheral Agents ')
            for entry in agents:
                print(f'    • {entry}')

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print(f'Sedaro Study Result Summary'.center(HFILL))
        print(f'Job ID {self.id}'.center(HFILL))
        hfill()
        print(f'{STATUS_ICON_MAP[self.status]} Study {self.status.lower()}')

        # print(f'\n📇 Scenario identification hash: {self.scenario_hash[:12]}')

        if self.iterations == 1:
            print('\n📋 Study contains 1 simulation')
        else:
            print(f'\n📋 Study contains {self.iterations} simulations')
        print(f'\n {str(self.job_ids)}')

        if self.__cache:
            if self.__cache_dir is None:
                print(f'\n❗ In-memory simulation result caching is ON')
            else:
                print(f'\n💾 Caching data to: {self.__cache_dir}')

        hfill()
        
        if len(self.__cached_sim_results) > 0:
            self.summarize_agents()
        else:
            print("❓ Agent data not yet loaded. Load with .summarize_agents()")

        hfill()
        print("❓ First set desired results downsampling with:")
        # print("       .set_result_limit(<# of points>) ")
        # print("       .set_result_binWidth( <fraction of overall points> )   ")
        hfill()
        print("❓ Query individual simulation results with .sim_result(<ID>)")
        print("❓ Load all Study result data and list Study Agent information with .summarize_agents()")
        print("❓ Return sim_id to sim_results dict with .study_results_dict()")
        print("❓ Query study agents with .agents(<NAME>)")
        # print("❓ return Study Dataframe with .study_dataframe(agent_id, engine_name, agent_name) ")
        # print(".       where engine_name is []")
        hfill()
        

    def agents(self, name:str) -> StudyAgentResult:
        simjob_to_agents =  { simjob_id:simresults.agent(name)   for (simjob_id, simresults) in self.study_results_dict.items() }
        return StudyAgentResult(self.id, name, simjob_to_agents)

    def study_dataframe(self, agent_id, engine_name, agent_name) -> pd.DataFrame:
        agent_engine_sim_results = {}
        
        agent_engine_df = {}
        
        for job_id in self.job_ids:
            var_dfs = []
            print(f'Processing {job_id}')
            agent_engine_sim_results[job_id] = self.sim_result(job_id) #,[(agent_id,engine_name)])
            for block_id in agent_engine_sim_results[job_id].agent(agent_name).blocks:
                block_results = agent_engine_sim_results[job_id].agent(agent_name).block(block_id)
                block_name = block_results.name
                for variable_name in block_results.variables:
                    variable_data = block_results.variable(variable_name)
                    
                    column_name = f'{block_name}.{variable_name}'
                    if variable_data.has_subseries:
                        for key, subtype in variable_data.subtypes:
                            #print(f"{block_name} {variable_name} {key} {subtype}")
                            first_value = variable_data[key].values[0]
                            data = variable_data[key].values
                        column_name += f'.{key}'
                    else:
                        first_value = variable_data.values[0]
                        data = variable_data.values
                    
                    if type(first_value) is list:
                        list_len = len(first_value)
                        columns = [f'{column_name}_X', f'{column_name}_Y', f'{column_name}_Z']
                        if list_len == 4:
                            columns.append(f'{column_name}_Q')

                        var_dfs.append( pd.DataFrame(data, columns=columns ) )
                    else:
                        var_dfs.append( pd.DataFrame(data, columns=[column_name]) )
            print('Combining')
            agent_engine_df[job_id] = pd.concat( var_dfs, index=1 )
                                      
        return agent_engine_df

    def save(self, path: Union[str, Path]):
        for cache_string, results in self.__cached_sim_results.items():
            dirpath = f"{path}/{self.__study.name}_{self.__study.id}_{cache_string}_studyresults"
            results.save(dirpath)
        with open(f"{Path}/study_metadata.txt", "w") as file:
            file.write(f"{self.__metadata}")
        with open(f"{Path}/study_info.txt", "w") as file:
            file.write(f"{self.__study}")

    @classmethod
    def load(cls, path: Union[str, Path]):
        series_results = {}
        for (dirpath, dirnames, filenames) in os.walk(path):
            for dir in dirnames:
                tokens = dir.split('_')
                name = tokens[-4]
                study_id = tokens[-3]
                cache_string = tokens[-2]
                save_type = tokens[-1]
                if save_type == 'studyresults':
                    series_results[cache_string] = SimulationResult.load(os.path.join(dirpath, dir))
            for file in filenames:
                if file == 'study_metadata.txt':
                    with open(os.path.join(dirpath, file), "r") as file:
                        metadata = file.read()
                if file == 'study_info.txt':
                    with open(os.path.join(dirpath, file), "r") as file:
                        study = file.read()

        new_study_result = cls(study, metadata)
        new_study_result.__cached_sim_results = series_results
        new_study_result.__cache = True
        new_study_result.__cache_dir = None

        return new_study_result