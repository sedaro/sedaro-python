import time

from config import API_KEY, HOST, SIMPLESAT_SCENARIO_ID, WILDFIRE_SCENARIO_ID

from sedaro import SedaroApiClient
from sedaro.settings import PRE_RUN_STATUSES, RUNNING, STATUS, TERMINATED

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _job_status_is_pending(job):
    return job[STATUS] in PRE_RUN_STATUSES


def _wait_until_passed_pending(simulation_handle):
    start_time = time.perf_counter()
    print('- Wait until no longer "PENDING"...')

    while _job_status_is_pending(simulation_handle.status()):
        max_seconds = 180
        if time.perf_counter() - start_time > max_seconds:
            raise TimeoutError(f'Simulation did not start within {max_seconds} seconds')
        time.sleep(2)


def _check_job_status_running(job):
    assert job[STATUS] == RUNNING
    print('-', job[STATUS], '-', round(
        job['progress']['percentComplete'], 2), '%')


def test_run_simulation():
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation

    # Start simulation
    simulation_handle = sim.start()
    print('- Started simulation')

    try:
        _wait_until_passed_pending(simulation_handle)

        # Get status (via default latest)
        _check_job_status_running(
            sim.status()
        )

        # Get status (via id)
        _check_job_status_running(
            sim.status(simulation_handle['id'])
        )

    finally:
        # Terminate
        print('- Terminating...')
        sim.terminate()

    # Test control from handle
    simulation_handle = sim.start()
    print('- Started simulation (via handle)')

    try:
        _wait_until_passed_pending(simulation_handle)

        # Get status (via handle)
        _check_job_status_running(
            simulation_handle := simulation_handle.status()
        )
        # Assert idempotency
        _check_job_status_running(
            simulation_handle := simulation_handle.status()
        )

    finally:
        # Terminate
        print('- Terminating (via handle)...')
        simulation_handle.terminate()

    # Test that handle is still useable
    assert simulation_handle.status()[STATUS] == TERMINATED
    simulation_handle.results()

def test_start_as_contextmanager():
    sim = sedaro.scenario(SIMPLESAT_SCENARIO_ID).simulation

    try:
        with sim.start(wait=True, verbose=True, timeout=600) as simulation_handle:
            sim_id = simulation_handle['id']
            assert simulation_handle.status()[STATUS] == RUNNING
            raise ValueError('Intentional error')  # intentionally raise error
    except ValueError as e:
        if str(e) != 'Intentional error':
            raise

    assert sim.status(job_id=sim_id)[STATUS] == TERMINATED


def run_tests():
    test_run_simulation()
    test_start_as_contextmanager()
