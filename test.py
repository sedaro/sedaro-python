from random import randrange

from sedaro import SedaroApiClient
from sedaro.exceptions import SedaroException

# TODO: remove this
# NOTE: update the API_KYE and BRANCH_ID for things that work with your dev environment
API_KEY = '2.6YnJx9FECI0_tweCHBVoDw1NpkqXpX0g2SbivoWk1js8tIigEcAFo9ebQ2pzSqpO-fHqzVikT2njA6xXNRTslw'
BRANCH_ID = 14


def test_get():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch_client = sedaro_client.get_branch(BRANCH_ID)
        # print(f'\nres: {branch_client}\n')


def test_create_update_and_delete_block():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch_client = sedaro_client.get_branch(BRANCH_ID)
        battery_cell_client = branch_client.BatteryCell.create(
            partNumber='987654321',
            manufacturer='Oh Yeah!!!!!!!!!',
            esr=1.0,
            maxChargeCurrent=100,
            maxDischargeCurrent=100,
            minSoc=1,
            capacity=5000,
            curve=[[0, 1], [3, 5]],
            topology='11',
        )

        bc_id = battery_cell_client.id

        assert battery_cell_client == branch_client.BatteryCell.get(
            bc_id)

        new_part_number = "Let's gooo!!!!!!!!!!!!"

        # print(battery_cell_client)

        battery_cell_client.update(partNumber=new_part_number)

        assert branch_client.BatteryCell.get(
            bc_id).partNumber == battery_cell_client.partNumber == new_part_number

        # print(battery_cell_client)

        battery_cell_client.delete()

        try:
            print(battery_cell_client)
        except SedaroException as e:
            msg = str(e)
            assert msg == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'


def test_update_rel_and_cascade_delete():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch_client = sedaro_client.get_branch(BRANCH_ID)

        subsystem_client = branch_client.subsystem.create(
            name='Temp Custom Subsystem ' + str(randrange(1, 100000)),
            satellite=branch_client.satellite.get_first().id
        )

        component_client = branch_client.component.create(
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
        except SedaroException as e:
            msg = str(e)
            assert msg == f'The referenced "Subsystem" (id: {ss_id}) no longer exists.'

        # make sure component is also deleted when subsystem is deleted
        try:
            component_client.update(name='Trying to update name')
        except SedaroException as e:
            msg = str(e)
            assert msg == f'The referenced "Component" (id: {c_id}) no longer exists.'


def test_traversing():
    with SedaroApiClient(api_key=API_KEY) as sedaro_client:
        branch_client = sedaro_client.get_branch(BRANCH_ID)

        solar_panel_client = branch_client.solarPanel.get_first()
        solar_panel_client.cell.panels[-1].subsystem.satellite.components[0].thermal_interface_A[0].satellite.topology

        con_ops_client = branch_client.con_ops.get_first()
        con_ops_client.targetGroups[0].targetAssociations.keys()

        assert branch_client.solarPanel.get_first(
        ) == solar_panel_client.cell.panels[0]


if __name__ == "__main__":
    test_get()
    test_create_update_and_delete_block()
    test_update_rel_and_cascade_delete()
    test_traversing()
    print('\ndone\n')
