from typing import TYPE_CHECKING
from urllib3.response import HTTPResponse
from pprint import pprint

from sedaro_old.custom import SedaroApiClient
from sedaro_old import ApiException
from sedaro_old.apis.tags import battery_cell_api
from sedaro_old.model.battery_cell import BatteryCell
from sedaro_old.model.battery_cell_create import BatteryCellCreate

if TYPE_CHECKING:
    from .sedaro_old.sedaro_old.custom import SedaroApiClient
    from .sedaro_old.sedaro_old import ApiException, ApiTypeError
    from .sedaro_old.sedaro_old.apis.tags import battery_cell_api
    from .sedaro_old.sedaro_old.model.battery_cell import BatteryCell
    from .sedaro_old.sedaro_old.model.battery_cell_create import BatteryCellCreate

API_KEY = '2.6YnJx9FECI0_tweCHBVoDw1NpkqXpX0g2SbivoWk1js8tIigEcAFo9ebQ2pzSqpO-fHqzVikT2njA6xXNRTslw'


def test_get():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch = sedaro_client.get_branch(14)
        print(f'\nres: {branch}\n')
        return


def test_create_block():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch = sedaro_client.get_branch(14)
        res = branch.BatteryCell.create({
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
        print(res)

        assert res == branch.BatteryCell.get(res.data['id'])


def test_update_block():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch = sedaro_client.get_branch(14)
        battery_cell = branch.BatteryCell.get(3604)

        res = battery_cell.update({'partNumber': 'Let\'s go!!!!!'})

        print(res)


def test_create_update_and_delete_block():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch = sedaro_client.get_branch(14)
        battery_cell = branch.BatteryCell.create({
            'partNumber': '987654321',
            'manufacturer': 'Oh Yeah!!!!!!!!!',
            'esr': 1.0,
            'maxChargeCurrent': 100,
            'maxDischargeCurrent': 100,
            'minSoc': 1,
            'capacity': 5000,
            'curve': [[0, 1], [3, 5]],
            'topology': '11',
        })

        battery_cell_id = battery_cell.data['id']

        assert battery_cell == branch.BatteryCell.get(battery_cell_id)

        new_part_number = "Let's gooo!!!!!!!!!!!!"

        print(battery_cell)

        battery_cell.update({'partNumber': new_part_number})

        assert branch.data['BatteryCell'][battery_cell_id]['partNumber'] == battery_cell.partNumber == new_part_number

        print(battery_cell)

        battery_cell.delete()

        try:
            print(battery_cell)
        except KeyError as e:
            assert str(e) == "'The referenced Sedaro Block no longer exists.'"


if __name__ == "__main__":
    # test_get()
    # test_create_block()
    # test_update_block()
    test_create_update_and_delete_block()


# ModuleNotFoundError -> AttributeError

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
