from random import randrange

from sedaro import SedaroApiClient
from sedaro.settings import BLOCKS

from config import API_KEY, HOST, SIMPLESAT_A_T_ID


def test_get_non_existant_branch():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        res = sedaro_client.send_request(
            f'/models/branches/999999999999999999999999',
            'GET'
        )

        assert res.get('error', {}).get(
            'message', None) == 'The requested endpoint does not exist or is not accessible with your current permissions.'


def test_raw_get_branch():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        res = sedaro_client.send_request(
            f'/models/branches/{SIMPLESAT_A_T_ID}',
            'GET'
        )
        keys = res.keys()
        for string in ['data', 'name', 'description', 'repository', 'tier2issues', 'workspace']:
            assert string in keys


def test_raw_request_CRUD_blocks():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        res = sedaro_client.send_request(
            f'/models/branches/{SIMPLESAT_A_T_ID}/template/',
            'PATCH',
            body={
                BLOCKS: [{
                    'name': 'Sun ' + str(randrange(1, 100000)),
                    'polynomialEphemerisBody': 'SUN',
                    'type': 'CelestialTarget'
                }]
            }
        )
        sun_id = res['crud'][BLOCKS][0]

        res = sedaro_client.send_request(
            f'/models/branches/{SIMPLESAT_A_T_ID}/template/',
            'PATCH',
            body={'delete': [sun_id]}
        )
        assert res['crud']['delete'][0] == sun_id


def run_tests():
    test_get_non_existant_branch()
    test_raw_get_branch()
    test_raw_request_CRUD_blocks()
