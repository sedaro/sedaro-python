import json

import numpy as np
from config import API_KEY, HOST, SIMPLESAT_SCENARIO_ID

from sedaro import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def __do_test(simulation_handle):
    agent_id = 'NSghFfVT8ieam0ydeZGX-'
    block_id = 'NZ2SHUkS95z1GtmMZ0CTk'

    assert tuple() == simulation_handle.produce(
        agent_id, block_id, ([1, 2, 3],))
    assert tuple() == simulation_handle.produce(
        agent_id, block_id, ([4, 5, 6],), timestamp=59911*2)

    result = simulation_handle.consume(agent_id, block_id)
    assert type(result) is tuple
    assert len(result) == 1
    assert type(result[0]) is np.ndarray
    assert result[0].shape == (3,)

    result = simulation_handle.consume(agent_id, block_id, time=59911)
    assert type(result) is tuple
    assert len(result) == 1
    assert type(result[0]) is np.ndarray
    assert result[0].shape == (3,)
    assert json.dumps(result[0].tolist()) == json.dumps([6800.,    0.,    0.])

    result = simulation_handle.consume(agent_id, block_id, time=59911.001)
    assert type(result) is tuple
    assert len(result) == 1
    assert type(result[0]) is np.ndarray
    assert result[0].shape == (3,)
    assert json.dumps(result[0].tolist()) == json.dumps(
        [6774.087229886119, 419.06940018131314, 419.06776101443677])


def test_run_externals():
    sim = sedaro.scenario(SIMPLESAT_SCENARIO_ID).simulation

    # Start simulation
    simulation_handle = sim.start()
    print('- Started simulation')

    __do_test(simulation_handle)

    # Test that can communicate after handle refresh
    simulation_handle.status()
    __do_test(simulation_handle)

    simulation_handle = sim.status()
    __do_test(simulation_handle)

    # Terminate
    print('- Terminating...')
    sim.terminate()


def run_tests():
    test_run_externals()
