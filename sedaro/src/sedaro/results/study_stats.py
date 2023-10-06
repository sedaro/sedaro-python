import datetime as dt
from pathlib import Path
from typing import List

from sedaro.branches.scenario_branch.sim_client import Simulation
from sedaro.results.simulation_result import SimulationResult

try:
    import matplotlib.pyplot as plt
except ImportError:
    PLOTTING_ENABLED = False
else:
    PLOTTING_ENABLED = True

try:
    import pandas as pd
    from ydata_profiling import ProfileReport, compare 
except ImportError:
    PANDAS_ENABLED = False
else:
    PANDAS_ENABLED = True



class StudyStatsResult:

    def __init__(self, study):
        '''Initialize a new Study Stats Result.

        By default, this class will lazily load simulation results as requested
        and cache them in-memory. Different caching options can be enabled with
        the .set_cache method.
        '''
        self.__study = study
        self.study_sim_results = {}
        self.job_ids = study.job_ids


    def __repr__(self) -> str:
        return f'SedaroStudyStatsResult(branch={self.__study.branch}, status={self.__study.status}, simulations={self.__study.iterations})'

    def __iter__(self):
        '''Iterate through simulation results.'''
        return (self.self.__study.result(id_) for id_ in self.job_ids)

    def __contains__(self, id_):
        '''Check if this study contains a certain simulation ID.'''
        return id_ in self.job_ids

    @property
    def id(self) -> int:
        return self.__study.id

    @property
    def branch(self) -> str:
        return self.__study.branch

    @property
    def scenario_hash(self) -> str:
        return self.__study.scenarioHash

    @property
    def status(self) -> str:
        return self.__study.status

    @property
    def date_created(self) -> dt.datetime:
        return dt.datetime.fromisoformat(str(self.__study.dateCreated)[:-1])

    @property
    def date_modified(self) -> dt.datetime:
        return dt.datetime.fromisoformat(str(self.__study.dateModified)[:-1])

    @property
    def job_ids(self) -> List[int]:
        return [entry for entry in self.__study.jobs]

    @property
    def iterations(self) -> int:
        return len(self.__study.jobs)

    def summarize(self) -> None:
        '''Summarize these results in the console.'''
        hfill()
        print(f'Sedaro Study Stat Result Summary'.center(HFILL))
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
        print("❓ Query individual simulation results with .result(<ID>)")
        print("❓ Query individual simulation statistics results with .stats_results(<ID>)")
        print("❓ Query Study Summary statistics results with .study_stats_results( [<ID>]) (defaults to all)")

    def stats_results(self, _id):
        return study_stats_results([_id])

    wildfire_agent_id = 'NT06aqHUT5djI1_JPAsck'

    #self = studyjob
    def study_stats_results(_ids=None, agent_name='Wildfire', wildfire_agent_id=wildfire_agent_id, engine='GNC' ):
        agent_engine_sim_results = {}
        
        agent_engine_df = {}
        
        if not _ids:
            _ids = self.job_ids 
        for jid in _ids:
            var_dfs = []
            print(f'Processing {jid}')
            agent_engine_sim_results[jid] = wildfire_branch.simulation.results(jid,[(wildfire_agent_id,engine)])
            for block_id in agent_engine_sim_results[jid].agent(agent_name).blocks:
                block_results = agent_engine_sim_results[jid].agent(agent_name).block(block_id)
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
            agent_engine_df[jid] = pd.concat( var_dfs, index=1 )
                                      
        return agent_engine_df



        




