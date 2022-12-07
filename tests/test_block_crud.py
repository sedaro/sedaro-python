from random import randrange

from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError
from sedaro.block_client import BlockClient
from sedaro.branch_client import BranchClient

from config import HOST, API_KEY, WILDFIRE_A_T_ID


def test_get():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)
        # print(f'\nres: {branch_client}\n')
        assert isinstance(branch_client, BranchClient)


def test_create_update_and_delete_block():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)
        battery_cell_client = branch_client.BatteryCell.create(
            partNumber='987654321',
            manufacturer='Sedaro Corporation',
            esr=0.01,
            maxChargeCurrent=15,
            maxDischargeCurrent=100,
            minSoc=0.2,
            capacity=500,
            curve=[[0, 0.5, 1], [12.2, 14.1, 16.8]],
            topology='10',
        )

        bc_id = battery_cell_client.id

        assert battery_cell_client == branch_client.BatteryCell.get(bc_id)

        new_part_number = "Let's gooo!!!!!!!!!!!!"

        # print(battery_cell_client)

        battery_cell_client.update(partNumber=new_part_number)

        assert branch_client.BatteryCell.get(
            bc_id).partNumber == battery_cell_client.partNumber == new_part_number

        # print(battery_cell_client)

        battery_cell_client.delete()

        try:
            battery_cell_client.update(partNumber="123456789")
        except NonexistantBlockError as e:
            msg = str(e)
            assert msg == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'


def test_update_rel_and_cascade_delete():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)

        subsystem_client = branch_client.Subsystem.create(
            name='Temp Custom Subsystem ' + str(randrange(1, 100000)),
            satellite=branch_client.Satellite.get_first().id
        )

        component_client = branch_client.Component.create(
            name='Temp custom component',
            subsystem=subsystem_client.id
        )

        c_id = component_client.id
        ss_id = subsystem_client.id

        # make sure other side of relationship was also updated
        assert component_client.id in [
            c.id for c in subsystem_client.components
        ]

        subsystem_client.delete()

        try:
            subsystem_client.delete()
        except NonexistantBlockError as e:
            msg = str(e)
            assert msg == f'The referenced "Subsystem" (id: {ss_id}) no longer exists.'

        # make sure component is also deleted when subsystem is deleted
        try:
            component_client.update(name='Trying to update name')
        except NonexistantBlockError as e:
            msg = str(e)
            assert msg == f'The referenced "Component" (id: {c_id}) no longer exists.'


def test_traversing_and_equality():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)

        solar_panel_client = branch_client.SolarPanel.get_first()

        assert isinstance(
            solar_panel_client.cell.topology.subsystem.satellite.components[
                0].thermal_interface_A[0].satellite.topology,
            BlockClient
        )

        con_ops_client = branch_client.ConOps.get_first()
        assert isinstance(
            list(con_ops_client.targetGroups[0].targetAssociations.keys())[0],
            BlockClient
        )

        assert solar_panel_client == branch_client.SolarPanel.get_first()
        assert solar_panel_client is not branch_client.SolarPanel.get_first()


def test_block_client_equality():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)

        subsystem_client = branch_client.Subsystem.create(
            name='One subsystem to rule them all',
            satellite='5'
        )

        subsystem_client_2 = subsystem_client.update(
            name='One subsystem to find them')

        subsystem_client_3 = branch_client.Subsystem.get(subsystem_client.id)

        assert subsystem_client == subsystem_client_2 == subsystem_client_3

        subsystem_client.delete()


def run_tests():
    test_get()
    test_create_update_and_delete_block()
    test_update_rel_and_cascade_delete()
    test_traversing_and_equality()
    test_block_client_equality()
