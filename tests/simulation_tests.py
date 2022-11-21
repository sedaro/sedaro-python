import time
from sedaro import SedaroApiClient

from config import HOST, API_KEY, WILDFIRE_SCENARIO_ID


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def _test_run_simulation():
    from sedaro_base_client.apis.tags import jobs_api

    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        # Instantiate jobs client
        jobs_api_client = jobs_api.JobsApi(sedaro_client)

        # Start simulation
        jobs_api_client.start_simulation(
            path_params={'branchId': WILDFIRE_SCENARIO_ID})
        print('- Started simulation')

        # Get status #1
        response = jobs_api_client.get_simulations(
            path_params={'branchId': WILDFIRE_SCENARIO_ID}, query_params={'latest': ''}
        )
        _check_job_status(response.body[0])
        time.sleep(3)

        # Get status #2
        response = jobs_api_client.get_simulations(
            path_params={'branchId': WILDFIRE_SCENARIO_ID}, query_params={'latest': ''}
        )
        _check_job_status(response.body[0])
        time.sleep(3)

        # Terminate
        print('- Terminating...')
        response = jobs_api_client.terminate_simulation(
            path_params={
                'branchId': WILDFIRE_SCENARIO_ID,
                'jobId': response.body[0]['id']
            }
        )
        print('-', response.body['message'])
        assert response.body['message'] == 'Successfully terminated simulation.'


def run_tests():
    _test_run_simulation()
