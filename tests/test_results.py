import json
import os
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

import uuid6
from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID, SUPERDOVE_SCENARIO_ID

from sedaro import (SedaroAgentResult, SedaroApiClient, SedaroBlockResult,
                    SedaroSeries, SimulationResult)
from sedaro.branches.scenario_branch.download import StreamManager
from sedaro.exceptions import NoSimResultsError
from sedaro.settings import STATUS, SUCCEEDED

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def _make_sure_wildfire_terminated():
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation

    try:
        results = sim.results()
        assert results.status == 'TERMINATED'
    except (NoSimResultsError, AssertionError):
        sim.start(wait=True)
        sim.terminate()


def _make_sure_superdove_done():
    sim = sedaro.scenario(SUPERDOVE_SCENARIO_ID).simulation
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
    _make_sure_superdove_done()
    scenario = sedaro.scenario(SUPERDOVE_SCENARIO_ID)
    sim = scenario.simulation

    # Obtain handle
    simulation_handle = sim.status()

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

    agent_result = result.agent(result.templated_agents[0])
    block_result = agent_result.block('root')

    # Exercise iteration
    for _, elapsed_time, _ in block_result.position.eci:
        if elapsed_time > 10:
            break

    # Assert agent lookup by 'id` and `name`
    agent_result_by_name = result.agent(scenario.Agent.get_first().name)
    agent_result_by_id = result.agent(scenario.Agent.get_first().id)
    assert agent_result_by_name.name == scenario.Agent.get_first().name == agent_result_by_id.name


def test_save_load():
    '''Test save and load of simulation data.

    Requires that SimpleSat has run successfully on the host.
    '''
    _make_sure_superdove_done()
    result = sedaro.scenario(SUPERDOVE_SCENARIO_ID).simulation.results()
    assert result.success

    with TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "sim.bak"
        result.save(file_path)
        # test that .DS_STORE, etc. doesn't interfere with loading
        os.system(f"touch {file_path}/.DS_STORE")
        os.system(f"touch {file_path}/data/foobar.parquet")
        new_result = SimulationResult.load(file_path)

        file_path = Path(temp_dir) / "sim2.bak"
        result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        with open(f"{file_path}/meta.json", "r") as f:
            meta = json.load(f)
        del meta['parquet_files']
        with open(f"{file_path}/meta.json", "w") as f:
            json.dump(meta, f)
        new_result = SimulationResult.load(file_path)

        file_path = Path(temp_dir) / "agent.bak"
        agent_result = new_result.agent(new_result.templated_agents[0])
        agent_result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        os.system(f"touch {file_path}/data/foobar.parquet")
        new_agent_result = SedaroAgentResult.load(file_path)

        file_path = Path(temp_dir) / "agent2.bak"
        agent_result = new_result.agent(new_result.templated_agents[0])
        agent_result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        with open(f"{file_path}/meta.json", "r") as f:
            meta = json.load(f)
        del meta['parquet_files']
        with open(f"{file_path}/meta.json", "w") as f:
            json.dump(meta, f)
        new_agent_result = SedaroAgentResult.load(file_path)

        file_path = Path(temp_dir) / "block.bak"
        block_result = new_agent_result.block('root')
        block_result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        os.system(f"touch {file_path}/data/foobar.parquet")
        new_block_result = SedaroBlockResult.load(file_path)

        file_path = Path(temp_dir) / "block2.bak"
        block_result = new_agent_result.block('root')
        block_result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        with open(f"{file_path}/meta.json", "r") as f:
            meta = json.load(f)
        del meta['parquet_files']
        with open(f"{file_path}/meta.json", "w") as f:
            json.dump(meta, f)
        new_block_result = SedaroBlockResult.load(file_path)

        file_path = Path(temp_dir) / "series.bak"
        series_result = new_block_result.position.ecef
        series_result.save(file_path)
        os.system(f"touch {file_path}/.DS_STORE")
        new_series_result = SedaroSeries.load(file_path)

        ref_series_result = new_result.agent(
            result.templated_agents[0]).block('root').position.ecef
        assert ref_series_result.mjd == new_series_result.mjd
        assert ref_series_result.values == new_series_result.values


def sample_model_and_data():
    import dask.dataframe as dd

    df1 = dd.from_dict({
        'b.value': ['0first', '0second'],
        'value': ['0rfirst', '0rsecond'],
        'index': [1, 4],
    }, npartitions=1)
    df1 = df1.set_index('index')

    df2 = dd.from_dict({
        'b.otherValue': ['1first', '1second', '1third', '1fourth'],
        'otherValue': ['1rfirst', '1rsecond', '1rthird', '1rfourth'],
        'index': [1, 2, 3, 4],
    }, npartitions=1)
    df2 = df2.set_index('index')

    return {
        'meta': {
            'structure': {
                'scenario': {
                    '_supers': {
                        'BlockWithQuantityKind': [],
                        'Agent': ['BlockWithQuantityKind'],
                    },
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
                        '_supers': {},
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
            },
        },
        'series': {
            'a/0': df1,
            'a/1': df2,
        },
    }

def test_query_model():
    simulation_job = {
        'branch': 'test_id',
        'dateCreated': '2021-08-05T18:00:00.000Z',
        'dateModified': '2021-08-05T18:00:00.000Z',
        STATUS: SUCCEEDED,
    }

    data = sample_model_and_data()

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
    assert model['value'] == '0rsecond'
    assert model['otherValue'] == '1rfourth'
    assert model['name'] == 'Root'
    assert model['blocks']['b']['value'] == '0second'
    assert model['blocks']['b']['otherValue'] == '1fourth'
    assert model['blocks']['b']['name'] == 'Block'


class MockDownloadBar:
    def __init__(self):
        pass

    def update(self, *args, **kwargs):
        pass


def compare_with_nans(a, b):
    import numpy as np

    assert len(a) == len(b)
    for i in range(len(a)):
        if np.isnan(a[i]):
            assert np.isnan(b[i])
        else:
            assert a[i] == b[i]


def test_download():
    # test download internals
    download_worker = StreamManager(None)
    download_worker.keys = set(['position', 'position.x', 'positionx', 'time', 'timeStep', 'timeStep.s'])
    to_remove = download_worker.select_columns_to_remove()
    assert set(to_remove) == set(['position', 'timeStep'])

    # test some insertions
    download_worker = StreamManager(MockDownloadBar())
    dict_1 = {'a': [1, 2, 3], 'b': [1, 2, 3], 'time': [1, 2, 3]}
    download_worker.ingest_core_data('foo', dict_1)
    assert download_worker.keys == set(['a', 'b', 'time'])
    assert set(download_worker.dataframe.columns) == set(['a', 'b', 'time'])
    c = download_worker.dataframe.compute()
    assert list(c['a']) == [1, 2, 3]
    assert list(c['b']) == [1, 2, 3]
    assert list(c['time']) == [1, 2, 3]

    dict_2 = {'a': [4, 5, 6], 'c': [4, 5, 6], 'time': [4, 5, 6]}
    download_worker.ingest_core_data('foo', dict_2)
    assert download_worker.keys == set(['a', 'b', 'c', 'time'])
    assert set(download_worker.dataframe.columns) == set(['a', 'b', 'c', 'time'])
    download_worker.dataframe = download_worker.dataframe.repartition(npartitions=1)
    download_worker.dataframe = download_worker.dataframe.reset_index(drop=True)
    c = download_worker.dataframe.compute()
    assert list(c['a']) == [1, 2, 3, 4, 5, 6]
    compare_with_nans(list(c['b']), [1.0, 2.0, 3.0, float('nan'), float('nan'), float('nan')])
    compare_with_nans(list(c['c']), [float('nan'), float('nan'), float('nan'), 4.0, 5.0, 6.0])
    assert list(c['time']) == [1, 2, 3, 4, 5, 6]

    # test that download succeeds
    sim = sedaro.scenario(WILDFIRE_SCENARIO_ID).simulation
    results = sim.results()
    root = uuid6.uuid7()
    path = f"{root}/to/some/directory"
    results.save(path)
    try:
        assert os.path.exists(path)
    finally:
        shutil.rmtree(path)


def test_series_values():
    import dask.dataframe as dd

    df = dd.from_dict({
        'time': [0, 1, 2, 3, 4, 5],
        'pref.a.0': [0, 1, 2, 3, 4, 5],
        'pref.a.1': [0, 5, 10, 15, 20, 25],
        'pref.b': [0, 2, 4, 6, 8, 10],
        'pref.c.foo': [0, 3, 6, 9, 12, 15],
        'pref.c.bar': [0, 4, 8, 12, 16, 20],
        'pref.c.baz.0.0': [0, 6, 12, 18, 24, 30],
        'pref.c.baz.0.1': [0, 7, 14, 21, 28, 35],
        'pref.c.baz.1.0': [0, 8, 16, 24, 32, 40],
        'pref.c.baz.1.1': [0, 9, 18, 27, 36, 45],
        'pref.d.a': [0, 10, 20, 30, 40, 50],
        'pref.visibleEarthArea': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],
    }, npartitions=1)
    df = df.set_index('time')

    col_ind = {
        'a': {'0': {}, '1': {}},
        'b': {},
        'c': {'foo': {}, 'bar': {}, 'baz': {'0': {'0': {}, '1': {}}, '1': {'0': {}, '1': {}}}},
        'd': {'a': {}},
        'visibleEarthArea': {},
    }

    ser = SedaroSeries('pref', df, {}, col_ind, 'pref')

    assert ser.values == {
        'a': [[0, 0], [1, 5], [2, 10], [3, 15], [4, 20], [5, 25]],
        'b': [0, 2, 4, 6, 8, 10],
        'c': {
            'foo': [0, 3, 6, 9, 12, 15],
            'bar': [0, 4, 8, 12, 16, 20],
            'baz': [[[0, 0], [0, 0]], [[6, 7], [8, 9]], [[12, 14], [16, 18]], [[18, 21], [24, 27]], [[24, 28], [32, 36]], [[30, 35], [40, 45]]],
        },
        'd': {'a': [0, 10, 20, 30, 40, 50]},
        'visibleEarthArea': [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]],
    }

    df2 = df[['pref.c.baz.0.0', 'pref.c.baz.0.1', 'pref.c.baz.1.0', 'pref.c.baz.1.1']]

    col_ind2 = col_ind['c']['baz']
    ser2 = SedaroSeries('pref.c.baz', df2, {}, col_ind2, 'pref.c.baz')
    assert ser2.values == [
        [[0, 0], [0, 0]],
        [[6, 7], [8, 9]],
        [[12, 14], [16, 18]],
        [[18, 21], [24, 27]],
        [[24, 28], [32, 36]],
        [[30, 35], [40, 45]],
    ]


def fake_stats(factor):
    return {
        'min': -1 * factor,
        'max': 5 * factor,
        'average': 2 * factor,
        'integral': 10 * factor,
        'absAvg': 3 * factor,
        'negativeMax': None,
        'positiveMax': 5 * factor,
    }


def test_stats():
    # test propagation of stats down to Series level, as well as certain functions at Block and Series level
    simulation_job = {
        'branch': 'test_id',
        'dateCreated': '2021-08-05T18:00:00.000Z',
        'dateModified': '2021-08-05T18:00:00.000Z',
        STATUS: SUCCEEDED,
    }

    data = sample_model_and_data()
    all_stats = data['stats'] = {
        'a/0': {
            'b.value': fake_stats(1),
            'value': fake_stats(10),
        },
        'a/1': {
            'b.otherValue': fake_stats(100),
            'otherValue': fake_stats(1000),
        },
    }

    results = SimulationResult(simulation_job, data)
    agent = results.agent('Agent')
    assert agent._SedaroAgentResult__stats == all_stats
    block = agent.block('b')
    assert block._SedaroBlockResult__stats == {
        'a/0': { 'b.value': fake_stats(1), },
        'a/1': { 'b.otherValue': fake_stats(100), },
    }
    assert block.stats() == {
        'Block.value': fake_stats(1),
        'Block.otherValue': fake_stats(100),
    }
    assert block.stats('min') == {
        'Block.value': -1,
        'Block.otherValue': -100,
    }
    assert block.stats('min', 'max') == ({
        'Block.value': -1,
        'Block.otherValue': -100,
    }, {
        'Block.value': 5,
        'Block.otherValue': 500,
    })
    series = block.value
    assert series.stats() == fake_stats(1)
    assert series.stats('min') == -1
    assert series.stats('min', 'max') == (-1, 5)

    # test waiting on stats from results_poll
    scenario = sedaro.scenario(SUPERDOVE_SCENARIO_ID)
    sim = scenario.simulation
    _make_sure_superdove_done()
    res = sim.results_poll(wait_on_stats=True)
    empty = ['NT-KoZFSELKK8eomP3lkV/0', 'NT-KoZFSELKK8eomP3lkV/1']
    has_rain_stats = ['NT-LKoFSJLenjoFP9FXAV/0', 'NT-LuTrRCydjLgnmceboV/0', 'NT-LgloSzu8F-V4MtzkHV/0', 'NT-L_VwTrXTMQUapcAoJk/0', 'NT-M0sqRR5WTIHKtB4ylF/0', 'NT-LoCYRnPamzh3QTTedF/0']
    assert res._SimulationResult__stats_fetched
    assert len(res._SimulationResult__stats) == len(empty) + len(has_rain_stats)
    for agent_id in empty:
        assert res._SimulationResult__stats[agent_id] == {}
    for agent_id in has_rain_stats:
        assert list(res._SimulationResult__stats[agent_id].keys()) == ['rainData.rainProbability']
    stats_from_endpoint = sim.stats()
    assert stats_from_endpoint == res._SimulationResult__stats

def test_utils():
    from sedaro.results.utils import get_static_data

    test_static_data = {
        'foobar/0': {
            'foo': 'bar',
        },
        'foobar/1': {
            'qux': 'baz',
        },
    }

    assert get_static_data(test_static_data, 'Block') == test_static_data
    assert get_static_data(test_static_data, 'Block', 'GNC') == {'foo': 'bar'}
    assert get_static_data(test_static_data, 'Block', 'CDH') == {'qux': 'baz'}
    assert get_static_data(test_static_data, 'Agent', 'CDH') == {'qux': 'baz'}
    assert get_static_data(test_static_data, 'slikertuhmdrtybdetvime5vt', 'CDH') == {'qux': 'baz'}
    try:
        get_static_data(test_static_data, 'Block', 'Power')
    except KeyError as e:
        assert e.args[0] == "No static data available for the specified engine for this Block."
    try:
        get_static_data(test_static_data, 'Agent', 'Power')
    except KeyError as e:
        assert e.args[0] == "No static data available for the specified engine for this Agent."
    try:
        get_static_data(test_static_data, 'Agent', 'NotAnEngine')
    except ValueError as e:
        assert e.args[0] == "NotAnEngine is not a valid engine identifier."
    try:
        get_static_data({}, 'Agent')
    except ValueError as e:
        assert e.args[0] == "No static data available for this Agent."


def run_tests():
    test_query_terminated()
    test_query()
    test_save_load()
    test_query_model()
    test_download()
    test_series_values()
    test_stats()
    test_utils()
