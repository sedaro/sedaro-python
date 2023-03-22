import time

import datetime as dt

from typing import List
from pathlib import Path
from sedaro import SedaroApiClient
from sedaro_base_client.apis.tags import jobs_api
from sedaro.results import SedaroSimulationResult
from sedaro.results.utils import hfill, HFILL, DEFAULT_HOST, STATUS_ICON_MAP


class SedaroStudyResult:

    def __init__(self, host, scenario_id, api_key: str, metadata, cache: bool = True, cache_dir = None):
        '''Initialize a new Study Result.

        See the following class methods for simple initialization:
            - get
            - poll
            - get_scenario_latest
            - poll_scenario_latest

        By default, this class will lazily load simulation results as requested
        and cache them in-memory. All constructors support the following
        optional arguments for caching:
            - cache: Boolean option to turn caching on or off.
            - cache_dir: Path to a directory for on-disk caching.
        '''
        self.__api_key = api_key
        self.__scenario = scenario_id
        self.__host = host

        self.__metadata = metadata

        self.__cache = cache
        self.__cache_dir = None
        self.__cached_sim_results = {}
        if self.__cache:
            if cache_dir is not None:
                self.__cache_dir = Path(cache_dir)
                if not self.__cache_dir.is_dir():
                    raise ValueError(f'Cache directory not found: {cache_dir}')
        else:
            if self.__cache_dir is not None:
                raise ValueError(f'Cache directory is defined but caching is off.')

    def __repr__(self) -> str:
        return f'SedaroStudyResult(branch={self.__scenario}, status={self.status}, iterations={self.iterations})'

    def __iter__(self):
        '''Iterate through simulation results.'''
        return (self.result(id_) for id_ in self.job_ids)

    def __contains__(self, id_):
        '''Check if this study contains a certain simulation ID.'''
        try:
            id_ = int(id_)
        except Exception:
            raise ValueError(f'Unrecognized ID type (expected int): {type(id_)}')
        return id_ in self.job_ids

    @property
    def id(self) -> int:
        return self.__metadata['id']

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
        return [int(entry) for entry in self.__metadata['jobs']]

    @property
    def iterations(self) -> int:
        return len(self.__metadata['jobs'])

    @classmethod
    def __get(
        cls,
        api_key: str,
        scenario_id: int,
        job_id: int = None,
        poll: bool = False,
        retry_interval: int = 2,
        host: str = DEFAULT_HOST,
        cache: bool = False,
        cache_dir = None,
    ):
        with SedaroApiClient(api_key=api_key, host=host) as sedaro_client:
            api_instance = jobs_api.JobsApi(sedaro_client)
            if job_id is None:
                try:
                    job_id = api_instance.get_studies(
                        path_params={'branchId': scenario_id},
                        query_params={'latest': ''}
                    ).body[0]['id']
                except IndexError:
                    raise IndexError(f'Could not find any simulation results for scenario: {scenario_id}')
            study = cls.__get_study(api_instance, scenario_id, job_id)

            if poll:
                while study['status'] in ('PENDING', 'RUNNING'):
                    study = cls.__get_study(api_instance, scenario_id, job_id)
                    time.sleep(retry_interval)

            return cls(host, scenario_id, api_key, study, cache=cache, cache_dir=cache_dir)

    @staticmethod
    def __get_study(api_instance: jobs_api.JobsApi, scenario_id: int, job_id: int) -> dict:
        try:
            return api_instance.get_study(path_params={'branchId': scenario_id, 'jobId': job_id}).body
        except Exception:
            raise IndexError(f'Could not find any study results for job: {job_id}')

    @classmethod
    def get(cls, api_key: str, scenario_id: int, job_id: int = None, **kwargs):
        '''Query a specific study result.'''
        return cls.__get(api_key, scenario_id, job_id, **kwargs)

    @classmethod
    def poll( cls, api_key: str, scenario_id: int, job_id: int = None, retry_interval: int = 2, **kwargs):
        '''Query a specific study result and wait for it to finish if it is running.'''
        return cls.__get(api_key, scenario_id, job_id, poll=True, retry_interval=retry_interval, **kwargs)

    def result(self, id_: str) -> SedaroSimulationResult:
        '''Query results for a particular simulation.'''
        try:
            id_ = int(id_)
        except Exception:
            raise ValueError(f'Unrecognized ID type (expected int): {type(id_)}')

        result = None
        if self.__cache:
            if self.__cache_dir is None:
                if id_ in self.__cached_sim_results:
                    result = self.__cached_sim_results[id_]
            else:
                cache_file = self.__cache_dir / f'sim_{id_}.cache'
                if cache_file.exists():
                    result = SedaroSimulationResult.from_file(cache_file)

        if result is None:
            print(f'💾 Downloading simulation result id {id_}...', end='')
            result = SedaroSimulationResult.get(self.__api_key, self.__scenario, id_, self.__host)
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
        with SedaroApiClient(api_key=self.__api_key, host=self.__host) as sedaro_client:
            api_instance = jobs_api.JobsApi(sedaro_client)
            self.__metadata = SedaroStudyResult.__get_study(api_instance, self.__scenario, self.id)

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
