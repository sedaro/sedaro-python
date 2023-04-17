import time
from pathlib import Path
from tempfile import TemporaryDirectory

from sedaro import (SedaroAgentResult, SedaroApiClient, SedaroBlockResult,
                    SedaroSeries, SedaroSimulationResult)

from config import API_KEY, HOST, SIMPLESAT_SCENARIO_ID, WILDFIRE_SCENARIO_ID


def _make_sure_wildfire_terminated():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro:
        sim_client = sedaro.get_sim_client(WILDFIRE_SCENARIO_ID)
        job = sim_client.get_latest()[0]

        if job['status'] != 'TERMINATED':
            sim_client.start()
            job = sim_client.get_latest()[0]
            sim_client.terminate(job['id'])

def _make_sure_simplesat_done():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro:
        sim_client = sedaro.get_sim_client(SIMPLESAT_SCENARIO_ID)
        job = sim_client.get_latest()[0]

        if job['status'] != 'SUCCEEDED':

            sim_client = sedaro.get_sim_client(SIMPLESAT_SCENARIO_ID)
            sim_client.start()
            job = sim_client.get_latest()[0]

            while job['status'] != 'SUCCEEDED':
                job = sim_client.get_latest()[0]
                time.sleep(1)

def test_query_terminated():
    '''Test querying of a terminated scenario.'''
    _make_sure_wildfire_terminated()
    result = SedaroSimulationResult.get_scenario_latest(API_KEY, WILDFIRE_SCENARIO_ID, host=HOST)
    assert not result.success


def test_query():
    '''Test querying of a successful scenario.

    Requires that SimpleSat has run successfully on the host.
    '''
    _make_sure_simplesat_done()
    result = SedaroSimulationResult.get_scenario_latest(API_KEY, SIMPLESAT_SCENARIO_ID, host=HOST)
    assert result.success

    agent_result = result.agent(result.templated_agents[0])
    block_result = agent_result.block('root')

    # Exercise iteration
    for elapsed_time, _ in block_result.position.eci:
        if elapsed_time > 10:
            break


def test_save_load():
    '''Test save and load of simulation data.

    Requires that SimpleSat has run successfully on the host.
    '''
    _make_sure_simplesat_done()
    result = SedaroSimulationResult.get_scenario_latest(API_KEY, SIMPLESAT_SCENARIO_ID, host=HOST)
    assert result.success

    with TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "sim.bak"
        result.to_file(file_path)
        new_result = SedaroSimulationResult.from_file(file_path)

        file_path = Path(temp_dir) / "agent.bak"
        agent_result = new_result.agent(new_result.templated_agents[0])
        agent_result.to_file(file_path)
        new_agent_result = SedaroAgentResult.from_file(file_path)

        file_path = Path(temp_dir) / "block.bak"
        block_result = new_agent_result.block('root')
        block_result.to_file(file_path)
        new_block_result = SedaroBlockResult.from_file(file_path)

        file_path = Path(temp_dir) / "series.bak"
        series_result = new_block_result.position.ecef
        series_result.to_file(file_path)
        new_series_result = SedaroSeries.from_file(file_path)

        ref_series_result = new_result.agent(result.templated_agents[0]).block('root').position.ecef
        assert ref_series_result.mjd == new_series_result.mjd
        assert ref_series_result.values == new_series_result.values


def run_tests():
    test_query_terminated()
    test_query()
    test_save_load()
