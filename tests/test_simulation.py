import time

from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID

from sedaro import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _job_status_is_pending(job):
    return job['status'] == 'PENDING' or job['status'] == 'PROVISIONING' or job['status'] == 'CONFIGURING' or job['status'] == 'BUILDING'


def _wait_until_passed_pending(simulation_handle):
    start_time = time.perf_counter()
    print('- Wait until no longer "PENDING"...')

    while _job_status_is_pending(simulation_handle.status()):
        max_seconds = 180
        if time.perf_counter() - start_time > max_seconds:
            raise TimeoutError(f'Simulation did not start within {max_seconds} seconds')
        time.sleep(2)


def _check_job_status_running(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def test_run_simulation():
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation

    # Start simulation
    simulation_handle = sim.start()
    print('- Started simulation')

    _wait_until_passed_pending(simulation_handle)

    # Get status (via default latest)
    _check_job_status_running(
        sim.status()
    )

    # Get status (via id)
    _check_job_status_running(
        sim.status(simulation_handle['id'])
    )

    # Terminate
    print('- Terminating...')
    sim.terminate()

    # Test control from handle
    simulation_handle = sim.start()
    print('- Started simulation (via handle)')

    _wait_until_passed_pending(simulation_handle)

    # Get status (via handle)
    _check_job_status_running(
        simulation_handle := simulation_handle.status()
    )
    # Assert idempotency
    _check_job_status_running(
        simulation_handle := simulation_handle.status()
    )

    # Terminate
    print('- Terminating (via handle)...')
    simulation_handle.terminate()

    # Test that handle is still useable
    assert simulation_handle.status()['status'] == 'TERMINATED'
    simulation_handle.results()


def run_tests():
    test_run_simulation()
