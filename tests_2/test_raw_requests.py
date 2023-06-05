from random import randrange

from config import API_KEY, HOST, SIMPLESAT_A_T_ID
from sedaro_2 import SedaroApiClient

from sedaro.settings import BLOCKS, CRUD

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def test_get_non_existant_branch():
    res = sedaro.request.get(
        f'/models/branches/999999999999999999999999',
    )

    assert res.get('error', {}).get(
        'message', None) == 'The requested endpoint does not exist or is not accessible with your current permissions.'


def test_raw_get_branch():
    res = sedaro.request.get(
        f'/models/branches/{SIMPLESAT_A_T_ID}',
    )
    keys = res.keys()
    for string in ['data', 'name', 'description', 'repository', 'tier2issues', 'workspace']:
        assert string in keys


def test_raw_request_CRUD_blocks():
    res = sedaro.request.patch(
        f'/models/branches/{SIMPLESAT_A_T_ID}/template/',
        body={
            BLOCKS: [{
                'name': 'Sun ' + str(randrange(1, 100000)),
                'type': 'CelestialTarget'
            }]
        }
    )
    sun_id = res[CRUD][BLOCKS][0]

    res = sedaro.request.patch(
        f'/models/branches/{SIMPLESAT_A_T_ID}/template/',
        body={'delete': [sun_id]}
    )
    assert res[CRUD]['delete'][0] == sun_id


def run_tests():
    test_get_non_existant_branch()
    test_raw_get_branch()
    test_raw_request_CRUD_blocks()
