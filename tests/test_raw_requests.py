from random import randrange

from sedaro import SedaroApiClient
from sedaro.utils import parse_urllib_response

from config import HOST, API_KEY, WILDFIRE_A_T_ID


def test_raw_get_branch():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        res = sedaro_client.send_request(
            f'/models/branches/{WILDFIRE_A_T_ID}',
            'GET'
        )
        keys = res.keys()
        for string in ['data', 'name', 'description', 'repository', 'user']:
            assert string in keys


def test_raw_request_CRUD_blocks():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        res = sedaro_client.send_request(
            f'/models/branches/{WILDFIRE_A_T_ID}/cdh/conops/celestial-targets/',
            'POST',
            body={
                'name': 'Sun ' + str(randrange(1, 100000)),
                'polynomialEphemerisBody': 'SUN',
                'conOps': 2
            }
        )
        assert res['action'] == 'CREATE'
        block_id = res['block']['id']

        res = sedaro_client.send_request(
            f'/models/branches/{WILDFIRE_A_T_ID}/cdh/conops/celestial-targets/{block_id}',
            'DELETE'
        )
        assert res['action'] == 'DELETE'


def run_tests():
    test_raw_get_branch()
    test_raw_request_CRUD_blocks()
