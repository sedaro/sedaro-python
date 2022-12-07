import time
from sedaro import SedaroApiClient

from config import HOST, API_KEY, WILDFIRE_SCENARIO_ID


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def _test_run_simulation():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        # Instantiate job client
        sim_client = sedaro_client.get_sim_client(WILDFIRE_SCENARIO_ID)

        # Start simulation
        sim_client.start()
        print('- Started simulation')

        # Get status #1
        response = sim_client.get_latest()
        _check_job_status(response.body[0])
        time.sleep(1)

        # Get status #2
        response = sim_client.get_latest()
        job = response.body[0]
        _check_job_status(job)
        time.sleep(1)

        # Terminate
        print('- Terminating...')
        response = sim_client.terminate(job['id'])
        print('-', response.body['message'])
        assert response.body['message'] == 'Successfully terminated simulation.'


def run_tests():
    _test_run_simulation()
