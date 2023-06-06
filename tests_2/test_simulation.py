import time

from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID
from sedaro_2 import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def test_run_simulation():
    sim = sedaro.scenario_branch(WILDFIRE_SCENARIO_ID).simulation

    # Start simulation
    sim.start()
    print('- Started simulation')

    # Get status #1
    job = sim.latest_raw()
    _check_job_status(job)
    time.sleep(1)

    # Get status #2
    job = sim.latest_raw()
    _check_job_status(job)
    time.sleep(1)

    # Terminate
    print('- Terminating...')
    res = sim.terminate(job['id'])
    print('-', res['message'])
    assert res['message'] == 'Successfully terminated simulation.'


def run_tests():
    test_run_simulation()
