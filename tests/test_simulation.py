import time

from sedaro import SedaroApiClient

from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%') # FIXME Can switch this back when percentage complete isn't NONE


def test_run_simulation():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro:
        # Instantiate job client
        sim_client = sedaro.get_sim_client(WILDFIRE_SCENARIO_ID)

        # Start simulation
        sim_client.start()
        print('- Started simulation')

        # Get status #1
        job = sim_client.get_latest()[0]
        _check_job_status(job)
        time.sleep(1)

        # Get status #2
        job = sim_client.get_latest()[0]
        _check_job_status(job)
        time.sleep(1)

        # Terminate
        print('- Terminating...')
        res = sim_client.terminate(job['id'])
        print('-', res['message'])
        assert res['message'] == 'Successfully terminated simulation.'


def run_tests():
    test_run_simulation()
