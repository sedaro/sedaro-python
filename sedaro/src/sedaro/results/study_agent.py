import gzip
import json
import glob
import os
import pandas as pd

from pathlib import Path
from typing import Generator, List, Union, Dict
from .study_block import StudyBlockResult

#from .block import SedaroBlockResult
from .utils import ENGINE_EXPANSION, ENGINE_MAP, HFILL, hfill, stats, histogram, scatter_matrix, compare_sims
from .agent import SedaroAgentResult
from .study_stats import StudyStats

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class StudyAgentResult(StudyStats):

    def __init__(self, study_id, name, simjob_to_agents):
        ''' Initialize study agent results
            Collection of SedaroAgentResults
        '''
        self._study_id = study_id
        self._name = name
        self._simjob_to_agents = simjob_to_agents
        self._simid_to_results = simjob_to_agents
        self._first_sim_id, self._first_agent = next(iter(simjob_to_agents.items()))

    def __iter__(self) -> Generator:
        '''Iterate through blocks on this studyagent.
           Assumes all studies simjobs have the same agents'''
        return (self.block(id_) for id_ in self._first_agent.blocks)

    def __contains__(self, id_: str) -> bool:
        '''Check if this studyagent result contains a certain block ID.'''
        return id_ in self._first_agent.blocks

    @property
    def name(self) -> str:
        return self._name

    @property
    def blockList(self) -> List[str]:
        ' Assumes all simjobs of a study have the same blocks'
        return self._first_agent.blocks

    @property
    def blockNameToID(self) -> Dict[str, str]:
        ' Assumes all simjobs of a study have the same blocks'
        return self._first_agent.blockNameToID

    @property
    def blockIdToName(self) -> Dict[str, str]:
        return self._first_agent.blockIdToName


    def blocks(self, id_: str) -> StudyBlockResult:
        blocks =  {simjob_id: agent.block(id_) for (simjob_id,agent) in self._simjob_to_agents.items()}
        return StudyBlockResult(self._study_id, id_, blocks)

    def block_names(self, name:str) -> StudyBlockResult:
        blocks =  {simjob_id: agent.block_name(name) for (simjob_id,agent) in self._simjob_to_agents.items()}
        return StudyBlockResult(self._study_id, name, blocks)


    @classmethod
    def load(cls, path: Union[str, Path]):
        # search directory for files with prefix
        simjobID_to_agents = {}

        for (dirpath, dirnames, filenames) in os.walk(path):
            for dir in dirnames:
                tokens = dir.split('_')
                name = tokens[-4]
                study_id = tokens[-3]
                simjob_id = tokens[-2]
                save_type = tokens[-1]
                if save_type == 'studyagent':
                    simjobID_to_agents[simjob_id] = SedaroAgentResult.load(os.path.join(dirpath, dir))
        return cls(study_id, name, simjobID_to_agents)


    def save(self, path: Union[str, Path]):
        for (simjob_id,agent) in self._simjob_to_agents.items():
            dirpath = f"{path}/{self._name}_{self._study_id}_{simjob_id}_studyagent"
            agent.save(dirpath)

    def summarize(self) -> dict:
        hfill()
        print(f"Study Agent Result Summary".center(HFILL))
        print(f"'{self._name}'".center(HFILL))
        print(f"Study ID: '{self._study_id}'".center(HFILL))

        self.print_sim_ids()

        print("🧩 Study Simulated Modules")
        print(self._first_agent.modules)

        print("\n📦 Available Blocks")
        print('    ' + '-' * 58)
        print('    |' + 'id'.center(38) + 'name'.center(30-12) + '|')
        print('    ' + '-' * 58)

        for block_id in self._first_agent._SedaroAgentResult__block_ids:
            if block_id != 'root':
                block_name = self._first_agent._SedaroAgentResult__block_structures[block_id].get('name', None)
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

        no_data_blocks = len(self._first_agent._SedaroAgentResult__block_structures) - len(self._first_agent._SedaroAgentResult__block_ids)
        if no_data_blocks > 0:
            print(f"\n    {no_data_blocks} block(s) with no associated data")

        hfill()
        print("❓ Query block results from all study simulations with .blocks(<ID>) or .blocks(<PARTIAL_ID>) or .block_names(<name>)")
        print("｛｝ Get a dict of block name to block_id with .blockNameToID")
        print("｛｝ Get a dict of block ID's to block name with .blockIdToName")
        print("［］ Get a list of block ID's  with .blockList()")
        hfill()
        print("⍆ The following commands have an optional variables argument which is a list of blockname.variable prefixes to filter on.")
        print("📊 Display a simulation agent module variables statistics with .sim_stats( module, sim_id,filter_string ) ")
        print(f"🧩   Where module must be one of the following: {  ENGINE_MAP.values() } ")
        print("📊 Display all agent block variables histograms for a study simulation with .sim_histogram( sim_id, output_html=False, filter_string=None )")
        print("📈📉 Display block variables scatter matrix plot  ")
        print("📉📈      for a study simulation with .sim_scatter_matrix( sim_id, filter_string=None )") 
        hfill()
        self.study_summarize()

    def sim_stats(self, module:str,  sim_id: str):
        if sim_id in self._simjob_to_agents:
            self._simjob_to_agents[sim_id].stats(module)  
        else:
            print(f"Error: Study sim id {sim_id} not found.")  
            self.print_sim_ids()

    def sim_histogram(self, module:str, sim_id: str, output_html= False, filter_string=None):
        if sim_id in self._simjob_to_agents:
            self._simjob_to_agents[sim_id].histogram(module,filter_string=filter_string, output_html=output_html)  
        else:
            print(f"Error: Study sim id {sim_id} not found.")  
            self.print_sim_ids()

    def sim_scatter_matrix(self, module:str, sim_id: str, filter_string=None):
        if sim_id in self._simjob_to_agents:
            self._simjob_to_agents[sim_id].scatter_matrix(module,filter_string=filter_string)  
        else:
            print(f"Error: Study sim id {sim_id} not found.")  
            self.print_sim_ids()

    def print_sim_ids(self):
            hfill()
            print(f"Study Simulation ID's".center(HFILL))
            print(f'\n {str( list(self._simjob_to_agents.keys()) )}')
            hfill()    

    def models_at(self, sim_id, mjd):
        if sim_id in self._simjob_to_agents:
            return { sim_id: agent.merge_at(mjd) for (sim_id, agent) in self._simjob_to_agents.items()}
        else:
            print(f"Error: Study sim id {sim_id} not found.")  
            self.print_sim_ids()



