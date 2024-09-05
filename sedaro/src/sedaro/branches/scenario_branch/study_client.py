import time
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Generator, Union

from sedaro_base_client.apis.tags import jobs_api

from ...exceptions import NoSimResultsError
from ...results import StudyResult
from ...settings import COMMON_API_KWARGS, PENDING, RUNNING, STATUS
from ...utils import body_from_res

if TYPE_CHECKING:
    from ...branches import ScenarioBranch
    from ...sedaro_api_client import SedaroApiClient


class Study:
    """A client to interact with the Sedaro API study (jobs) routes"""

    def __init__(self, sedaro: 'SedaroApiClient', branch: 'ScenarioBranch'):
        """Instantiate a Sedaro `Study` instance

        Args:
            sedaro (`SedaroApiClient`): the `SedaroApiClient`
            branch_id (`int`): id of the desired Sedaro Scenario Branch to interact with its simulations (jobs).
        """
        self._branch = branch
        self._sedaro = sedaro

    @contextmanager
    def __jobs_client(self) -> Generator['jobs_api.JobsApi', Any, None]:
        with self._sedaro.api_client() as api:
            yield jobs_api.JobsApi(api)

    def start(self, iterations: int) -> 'StudyHandle':
        """Starts study corresponding to the respective Sedaro Scenario Branch id.

        Returns:
            StudyHandle
        """
        with self.__jobs_client() as jobs:
            res = jobs.start_study(
                path_params={'branchId': self._branch.id},
                query_params={'iterations': iterations},
                **COMMON_API_KWARGS
            )
        return StudyHandle(body_from_res(res), self)

    def status(self, job_id: str = None) -> 'StudyHandle':
        """Gets the latest study corresponding to the respective Sedaro Scenario Branch id. This can return a
        response even before the study is done.

        Args:
            job_id (str, optional): triggers getting the study job assocciated with the `id` rather than the\
                default latest.

        Raises:
            NoSimResultsError: if no study has been started and `err_if_empty` set to `True`

        Returns:
            StudyHandle
        """
        if job_id is None:
            with self.__jobs_client() as jobs:
                res = jobs.get_studies(
                    path_params={'branchId': self._branch.id},
                    query_params={'latest': ''},
                    **COMMON_API_KWARGS
                )
            if len(body := body_from_res(res)):
                return StudyHandle(body[0], self)

            raise NoSimResultsError(
                status=404,
                reason=f'Could not find any studies for scenario: {self._branch.id}'
            )

        else:
            with self.__jobs_client() as jobs:
                res = jobs.get_study(
                    path_params={
                        'branchId': self._branch.id,
                        'jobId': job_id
                    },
                    **COMMON_API_KWARGS
                )
                return StudyHandle(body_from_res(res), self)

    def terminate(self, job_id: int = None) -> 'StudyHandle':
        """Terminate latest running simulation job corresponding to the respective Sedaro Scenario Branch id. If a
        `job_id` is provided, that simulation job will be terminated rather than the latest.

        Args:
            job_id (`int`, optional): id of the simulation (job) to terminate.

        Raises:
            NoSimResultsError: if no study has been started.

        Returns:
            StudyHandle
        """
        if job_id is None:
            job_id = self.status()['id']

        with self.__jobs_client() as jobs:

            jobs.terminate_study(
                path_params={
                    'branchId': self._branch.id,
                    'jobId': job_id
                },
                **COMMON_API_KWARGS
            )
        return StudyHandle(None, self)

    def results(self, job_id: str = None) -> StudyResult:
        """Query latest scenario study result. If a `job_id` is passed, query for corresponding sim results rather than
        latest.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.

        Raises:
            NoSimResultsError: if no study has been started.
            SedaroApiException: if no study has completed.

        Returns:
            SimulationResult: a `SimulationResult` instance to interact with the results of the sim.
        """
        job = self.status(job_id)
        return StudyResult(self, job)

    def results_poll(self, job_id: str = None, retry_interval: int = 2, timeout: int = None) -> StudyResult:
        """Query latest scenario study result and wait for sim to finish if it's running. If a `job_id` is passed, query for
        corresponding study results rather than latest. See `results` method for details on using the `streams` kwarg.

        Args:
            job_id (str, optional): `id` of the data array from which to fetch results. Defaults to `None`.
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the study to finish. Defaults to `None`.

        Raises:
            NoSimResultsError: if no study has been started.

        Returns:
            StudyResult: a `StudyResult` instance to interact with the results of the sim.
        """
        job = self.status(job_id)
        options = {PENDING, RUNNING}
        start_time = time.time()

        while job[STATUS] in options and (not timeout or time.time() - start_time < timeout):
            job = self.status()
            time.sleep(retry_interval)

        return self.results(job_id=job_id)


class StudyJob:
    def __init__(self, job: Union[dict, None]): self.__job = job
    def get(self, key, default=None): return self.__job.get(key, default)

    def __getitem__(self, key):
        if self.__job:
            if key in self.__job:
                return self.__job[key]
            else:
                raise KeyError(
                    f'Key {key} not found in StudyJob object. Available values are: {self.__job.keys()}')
        else:
            raise Exception(
                'No study is running. It was either terminated or one was never started.')


class StudyHandle:

    def __init__(self, job: Union[dict, None], study_client: Study):
        self.__job = StudyJob(job)
        self.__study_client = study_client

    def __getitem__(self, key): return self.__job[key]
    def get(self, key, default=None): return self.__job.get(key, default)

    def status(self, err_if_empty: bool = True):
        """Refreshes the local study status.

        Args:
            err_if_empty (bool, optional): Triggers raising an error if no study results and `err_if_empty`.\
                Defaults to `True`.

        Raises:
            NoSimResultsError: if no study has been started and `err_if_empty` set to `True`

        Returns:
            StudyHandle (self)
        """
        # FIXME: This is broken, but matches SimulationHandle (also broken)
        self.__job = self.__study_client.status(self.__job['id'], err_if_empty=err_if_empty)
        return self

    def terminate(self):
        """Terminate the running study.

        Returns:
            StudyHandle (self)
        """
        self.__study_client.terminate(self.__job['id'])
        self.__job = StudyJob(None)
        return self

    def results(self) -> StudyResult:
        """Query study results.

        Args:
            None

        Raises:
            NoSimResultsError: if no study has been started.
            SedaroApiException: if no study has completed.

        Returns:
            StudyResult: a `StudyResult` instance to interact with the results of the sim.
        """
        return self.__study_client.results(job_id=self.__job['id'])

    def results_poll(self, retry_interval: int = 2, timeout: int = None) -> StudyResult:
        """Query study results but wait for sim to finish if it's running. See `results` method for details on using the `streams` kwarg.

        Args:
            retry_interval (int, optional): Seconds between retries. Defaults to `2`.
            timeout (int, optional): Maximum time to wait for the study to finish. Defaults to `None`.

        Raises:
            NoSimResultsError: if no study has been started.

        Returns:
            StudyResult: a `StudyResult` instance to interact with the results of the sim.
        """
        return self.__study_client.results_poll(job_id=self.__job['id'], retry_interval=retry_interval, timeout=timeout)
