import datetime as dt
from pathlib import Path
from typing import List

from sedaro.branches.scenario_branch.sim_client import Simulation
from sedaro.results.simulation_result import SimulationResult
from sedaro.results.utils import HFILL, STATUS_ICON_MAP, hfill


class StudyResult:

    def __init__(self, study, metadata: dict):
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

    def set_cache(self, cache: bool, cache_dir: str = None) -> None:
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

    def result(self, id_: str) -> SimulationResult:
        '''Query results for a particular simulation.'''
        result = None
        if self.__cache:
            if self.__cache_dir is None:
                if id_ in self.__cached_sim_results:
                    result = self.__cached_sim_results[id_]
            else:
                cache_file = self.__cache_dir / f'sim_{id_}.cache'
                if cache_file.exists():
                    result = SimulationResult.from_file(cache_file)

        if result is None:
            print(f'💾 Downloading simulation result id {id_}...', end='')
            result = Simulation(self.__study._sedaro, self.__study._branch).results(id_)
            print('done!')

        if self.__cache:
            if self.__cache_dir is None:
                self.__cached_sim_results[id_] = result
            else:
                if not cache_file.exists():
                    result.to_file(cache_file, verbose=False)

        return result

    def clear_cache(self) -> None:
        self.__cached_sim_results = {}
        if self.__cache_dir is not None:
            for file in self.__cache_dir.glob('sim_*.cache'):
                file.unlink()

    def refresh(self) -> None:
        '''Update metadata for this study.'''
        from sedaro.branches.scenario_branch.study_client import Study
        self.__metadata = self.__study.status(self.id)

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

        if self.__cache:
            if self.__cache_dir is None:
                print(f'\n❗ In-memory simulation result caching is ON')
            else:
                print(f'\n💾 Caching data to: {self.__cache_dir}')

        hfill()
        print("❓ Query individual simulation results with .result(<ID>)")
