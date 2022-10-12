from typing import TYPE_CHECKING
from urllib3.response import HTTPResponse
from pprint import pprint

from sedaro.custom import SedaroApiClient
from sedaro import ApiException
from sedaro.apis.tags import battery_cell_api
from sedaro.model.battery_cell import BatteryCell
from sedaro.model.battery_cell_create import BatteryCellCreate

if TYPE_CHECKING:
    from .sedaro.sedaro.custom import SedaroApiClient
    from .sedaro.sedaro import ApiException, ApiTypeError
    from .sedaro.sedaro.apis.tags import battery_cell_api
    from .sedaro.sedaro.model.battery_cell import BatteryCell
    from .sedaro.sedaro.model.battery_cell_create import BatteryCellCreate

API_KEY = '2.6YnJx9FECI0_tweCHBVoDw1NpkqXpX0g2SbivoWk1js8tIigEcAFo9ebQ2pzSqpO-fHqzVikT2njA6xXNRTslw'


def test_get():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        # res = sedaro_client.call_api('/', 'GET')
        res: HTTPResponse = sedaro_client.call_api(
            '/models/branches/14', 'GET',)
        print(f'\nres: {res.data}\n')
        return


def test_create_block_1():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:

        api_instance = battery_cell_api.BatteryCellApi(sedaro_client)

        body = BatteryCellCreate(
            partNumber='1234',
            manufacturer='abcd',
            esr=1.0,
            maxChargeCurrent=100,
            maxDischargeCurrent=100,
            minSoc=0.01,
            capacity=5000,
            curve=[[0, 0.005, ], [3, 3.08]],
            topology='11',
        )

        res = api_instance.create_battery_cell(
            path_params={'branchId': 14},
            body=body,
        )
        pprint(res)


def test_create_block_2():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        block_client = sedaro_client.get_block_client(14, 'BatteryCell')

        res = block_client.create({
            'partNumber': '987654321',
            'manufacturer': 'Oh Yeah!',
            'esr': 1.0,
            'maxChargeCurrent': 100,
            'maxDischargeCurrent': 100,
            'minSoc': 0.01,
            'capacity': 5000,
            'curve': [[0, 0.005, ], [3, 3.08]],
            'topology': '11',
        })

        pprint(res)
        print(res.body['block']['id'])


def test_update_block():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        # import json
        # res = sedaro_client.call_api(
        #     '/models/branches/14/power/batteries/cells/3570',
        #     'PATCH',
        #     body=json.dumps({'partNumber': 'hello'}), headers={'Content-Type': 'application/json'}
        # )

        block_client = sedaro_client.get_block_client(14, 'BatteryCell')

        res = block_client.update('3572', {
            'partNumber': 'New Part Number',
            'manufacturer': 'Oh Yeah!',
            'esr': 1.0,
            'maxChargeCurrent': 100,
            'maxDischargeCurrent': 100,
            'minSoc': 0.01,
            'capacity': 5000,
            'curve': [[0, 0.005], [3, 3.08]],
            'topology': '11',
        })
        pprint(res)


if __name__ == "__main__":
    test_create_block_2()
    # test_update_block()


# class Block:

#     def create():
#         '''asdfasdf'''
#         pass

# class Branch:

#     def __getattr__(self, key) -> Block:
#         pass

# branch: Branch = sedaro_client.get_branch(14)

# block = branch.Block.create(**kwargs)
# block = branch.Block.get() # get from branch data already returned

# block.update(**kwargs)
# block.delete()

# batteryCell.partNumber # -> batteryCell['partNumber']


# Future:
# - Traversing: batteryCell.batteryPack.battery.satellite.update()
# - All references update togetehr: batteryCellCopy = copy(batteryCell)
# - Plotting methods on blocks
# - refresh method on a block


# import sedaro
# from sedaro import SedaroApiClient
# from sedaro_base_client import ApiClient
