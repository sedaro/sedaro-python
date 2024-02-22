import gzip
import json
from pathlib import Path
from typing import Generator, Union

from .series import SedaroSeries
from .utils import ENGINE_EXPANSION, HFILL, hfill
from .study_series import StudySeries


# What is the difference between StudyBlockResult and StudySeries?
# StudyBlockResult is a collection of SedaroBlockResults
class StudyBlockResult:

    def __init__(self, study_id, name, blocks):
        self._name = name
        self._study_id = study_id
        self._blocks   = blocks
        self._first_sim_id, self._first_block = next(iter(blocks.items()))

    def __getattr__(self, name: str) -> StudySeries:
        '''Get a particular variable by name.

        Typically invoked by calling .<VARIABLE_NAME> on an instance
        of SedaroBlockResult.
        '''
        series = { sim_id: block.__getattr__(name) for (sim_id,block) in self._blocks.items() }
        return StudySeries(self._study_id, name, series)

    def __contains__(self, variable: str) -> bool:
        '''Check if this block contains a variable by name.'''
        return variable in self._first_block.variables

    def __iter__(self) -> Generator:
        '''Iterate through variables on this block.'''
        return (self.__getattr__(variable) for variable in self._first_block.variables)

    def __repr__(self) -> str:
        return f'SedaroBlockResult({self._name})'        

    @property
    def name(self):
        return self._name

    @property
    def modules(self):
        return list(self._first_block.modules)

    @property
    def variables(self):
        return list(self._first_block.variables)

    def module_to_dataframe(self):
        raise NotImplementedError("")

    def variable(self, name: str) -> StudySeries:
        '''Query a particular variable by name.'''
        series = { sim_id: block.__getattr__(name) for (sim_id,block) in self._blocks.items() }
        return StudySeries(self._study_id, name, series)


    def to_file(self, filename_prefix: Union[str, Path], verbose=True) -> None:
        for (simjob_id,block) in self._blocks.items():
            filename = filename_prefix + '_' + simjob_id + "_block.json"
            block.to_file(filename, verbose)

    @classmethod
    def from_file(cls, filename: Union[str, Path]):
        pass

    def summarize(self) -> None:
        hfill()
        print(f"Study Simulation Block Result Summary".center(HFILL))
        print(f"'{self._name}'".center(HFILL))
        print(f"Study ID: '{self._study_id}'".center(HFILL))
        hfill()

        self._print_sim_ids()

        print("🧩 Simulated Modules")
        for module in self._first_block.modules:
            print(f'    • {ENGINE_EXPANSION[module]}')

        print("\n📋 Variables Available")
        for variable in self._first_block.variables:
            print(f'    • {variable}')
        hfill()

        print("❓ Query variables with .<VARIABLE_NAME> or .variable( VARIABLE_NAME )")
        print("⍆ The following commands have an optional variables argument which is a list of variable names prefixes to filter on.")
        print("Σ Display all block variables statistics for a study simulation with .sim_stats( sim_id, output_html=False, variables=None ) ")
        print("📊 Display all block variables histograms for a study simulation with .sim_histogram( sim_id, output_html=False, variables=None )")
        print("📈📉 Display block variables scatter matrix plot  ")
        print("📉📈      for a study simulation with .sim_scatter_matrix( sim_id, variables=None )") 
        hfill()
        print("📈📉 Display block scatter matrix plot from all sims in study ")
        print("📉📈      with .study_scatter_matrix(size=10, variables='attitudeError' )") 
        print("📊 Display block histograms from all study sims with .study_histogram(output_html= False, variables=None)")
        print("𝛴 Display Block statistics from all study sims with .study_stats() ")

    def value_at(self, mjd):
        return { sim_id: block.value_at(mjd) for (sim_id, block) in self._blocks.items()}

    def sim_scatter_matrix(self, sim_id, variables=None):
        if sim_id in self._blocks:
            self._blocks[sim_id].scatter_matrix(variables)
        else:
            print(f"Error: Study sim id {sim_id} not found.") 
            self._print_sim_ids()    

    def sim_stats(self, sim_id:str, variables=None):
        if sim_id in self._blocks:
            self._blocks[sim_id].stats(variables)
        else:
            print(f"Error: Study sim id {sim_id} not found.") 
            self._print_sim_ids()

    def sim_histogram(self, sim_id:str, output_html=False, variables=None):
        if sim_id in self._blocks:
            self._blocks[sim_id].histogram(output_html, variables)
        else:
            print(f"Error: Study sim id {sim_id} not found.") 
            self._print_sim_ids()

    def study_stats(self):
        for sim_id, block in self._blocks.items():
            block.stats()

    def study_histogram(self, output_html= False, variables=None):
        for sim_id, block in self._blocks.items():
            block.histogram(output_html, variables)

    def study_scatter_matrix(self, size=10, variables=None):
        for sim_id, block in self._blocks.items():
            block.scatter_matrix(size, variables)

    def _print_sim_ids(self):
        hfill()
        print(f"Study Simulation ID's".center(HFILL))
        print(f'\n {str( list(self._blocks.keys()) )}')
        hfill()


