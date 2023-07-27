from pathlib import Path
from tempfile import TemporaryDirectory

from config import API_KEY, HOST, SIMPLESAT_SCENARIO_ID, WILDFIRE_SCENARIO_ID

from sedaro import (SedaroAgentResult, SedaroApiClient, SedaroBlockResult,
                    SedaroSeries, SimulationResult)
from sedaro.exceptions import NoSimResultsError

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _make_sure_wildfire_terminated():
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation

    try:
        results = sim.results()
        assert results.status == 'TERMINATED'
    except (NoSimResultsError, AssertionError):
        sim.start()
        sim.terminate()


def _make_sure_simplesat_done():
    sim = sedaro.scenario(SIMPLESAT_SCENARIO_ID).simulation
    try:
        results = sim.results()
        assert results.success
    except (NoSimResultsError, AssertionError):
        sim.start()
        sim.results_poll()


def test_query_terminated():
    '''Test querying of a terminated scenario.'''
    _make_sure_wildfire_terminated()
    assert not sedaro.scenario(
        WILDFIRE_SCENARIO_ID).simulation.results().success


def test_query():
    '''Test querying of a successful scenario.

    Requires that SimpleSat has run successfully on the host.
    '''
    _make_sure_simplesat_done()
    sim = sedaro.scenario(SIMPLESAT_SCENARIO_ID).simulation

    # Obtain handle
    simulation_handle = sim.status()

    # make sure results_plain returns dictionary (testing latest and with id)
    plain = sim.results_plain()
    assert isinstance(plain, dict)
    assert plain == simulation_handle.results_plain()
    data_array_id = plain['meta']['id']
    assert plain == sim.results_plain(id=data_array_id)

    # test results method (default latest)
    result = sim.results()
    assert result.success
    result = simulation_handle.results()
    assert result.success

    # test results method (with id)
    job = sim.status()
    job_id = job['id']
    result_from_id = sim.results(job_id)
    assert result_from_id.success

    # make sure results have same ids
    assert result.job_id == result_from_id.job_id == job_id
    assert result.data_array_id == result_from_id.data_array_id == data_array_id

    agent_result = result.agent(result.templated_agents[0])
    block_result = agent_result.block('root')

    # Exercise iteration
    for _, elapsed_time, _ in block_result.position.eci:
        if elapsed_time > 10:
            break


def test_save_load():
    '''Test save and load of simulation data.

    Requires that SimpleSat has run successfully on the host.
    '''
    _make_sure_simplesat_done()
    result = sedaro.scenario(SIMPLESAT_SCENARIO_ID).simulation.results()
    assert result.success

    with TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "sim.bak"
        result.to_file(file_path)
        new_result = SimulationResult.from_file(file_path)

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

        ref_series_result = new_result.agent(
            result.templated_agents[0]).block('root').position.ecef
        assert ref_series_result.mjd == new_series_result.mjd
        assert ref_series_result.values == new_series_result.values


def test_query_model():
    simulation_job = {
        'branch': 'test_id',
        'dateCreated': '2021-08-05T18:00:00.000Z',
        'dateModified': '2021-08-05T18:00:00.000Z',
        'status': 'SUCCEEDED',
    }

    data = {
        'meta': {
            'structure': {
                'scenario': {
                    'blocks': {
                        'a': {
                            'type': 'Agent',
                            'name': 'Agent',
                            'id': 'a',
                        }
                    }
                },
                'agents': {
                    'a': {
                        'blocks': {
                            'b': {
                                'id': 'b',
                                'name': 'Block',
                                'value': '0zero',
                                'otherValue': '0otherZero',
                            },
                        },
                        'name': 'Root',
                        'value': '0rzero',
                        'otherValue': '0rotherZero',
                    }
                }
            }
        },
        'series': {
            'a/0': [
                [1, 4],
                {
                    'a': {
                        'b': {
                            'value': ['0first', '0second'],
                        },
                        'value': ['0rfirst', {'edge': 12}],
                    }
                }
            ],
            'a/1': [
                [1, 2, 3, 4],
                {
                    'a': {
                        'b': {
                            'otherValue': ['1first', '1second', '1third', '1fourth'],
                        },
                        'otherValue': ['1rfirst', '1rsecond', '1rthird', '1rfourth'],
                    }
                }
            ],
        }
    }

    results = SimulationResult(simulation_job, data)
    agent = results.agent('Agent')

    model = agent.model_at(1)
    assert model['value'] == '0rfirst'
    assert model['otherValue'] == '1rfirst'
    assert model['name'] == 'Root'
    assert model['blocks']['b']['value'] == '0first'
    assert model['blocks']['b']['otherValue'] == '1first'
    assert model['blocks']['b']['name'] == 'Block'

    for t in [2, 2.1, 2.9999]:
        model = agent.model_at(t)
        assert model['value'] == '0rfirst'
        assert model['otherValue'] == '1rsecond'
        assert model['name'] == 'Root'
        assert model['blocks']['b']['value'] == '0first'
        assert model['blocks']['b']['otherValue'] == '1second'
        assert model['blocks']['b']['name'] == 'Block'

    model = agent.model_at(4)
    assert model['value']['edge'] == 12
    assert model['otherValue'] == '1rfourth'
    assert model['name'] == 'Root'
    assert model['blocks']['b']['value'] == '0second'
    assert model['blocks']['b']['otherValue'] == '1fourth'
    assert model['blocks']['b']['name'] == 'Block'


def run_tests():
    test_query_terminated()
    test_query()
    test_save_load()
    test_query_model()
