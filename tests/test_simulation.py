from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID

from sedaro import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _check_job_status(job):
    assert job['status'] == 'RUNNING'
    print('-', job['status'], '-', round(
        job['progress']['percentComplete'], 2), '%')


def test_run_simulation():
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation

    # Start simulation
    simulation_handle = sim.start()
    print('- Started simulation')

    # Get status (via default latest)
    _check_job_status(
        sim.status()
    )

    # Get status (via id)
    _check_job_status(
        sim.status(simulation_handle['id'])
    )

    # Terminate
    print('- Terminating...')
    terminated_handle = False
    simulation_handle = sim.terminate()
    try:
        simulation_handle['id']
    except Exception as e:
        assert 'No simulation is running' in str(e)
        terminated_handle = True
    assert terminated_handle

    # Test control from handle
    simulation_handle = sim.start()
    print('- Started simulation (via handle)')

    # Get status (via handle)
    _check_job_status(
        simulation_handle.status()
    )

    # Terminate
    print('- Terminating (via handle)...')
    simulation_handle.terminate()
    terminated_handle = False
    try:
        simulation_handle['id']
    except Exception as e:
        assert 'No simulation is running' in str(e)
        terminated_handle = True
    assert terminated_handle


def run_tests():
    test_run_simulation()
