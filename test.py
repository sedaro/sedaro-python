from random import randrange
import time

from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError
from sedaro.block_class_client import BlockClassClient
from sedaro.branch_client import BranchClient

HOST = 'http://localhost:80'
# TODO: remove this
# NOTE: update the API_KEY and WILDFIRE_A_T_ID for things that work with your dev environment
# NOTE: these are temporary for Zach's dev environment
API_KEY = '1.-RjK0kE34B5z-V7BqBVdhSMLgHq9UTGB7iIZYTpoDGfZpn2cQPWE9kz_G9LapUshx7inFFTmN_xNMS5YnGMW-w'
WILDFIRE_A_T_ID = 55
WILDFIRE_SCENARIO_ID = 57


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
            battery_cell_client.update(partNumber="123456789")
        except NonexistantBlockError as e:
            msg = str(e)
            assert msg == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'


def test_update_rel_and_cascade_delete():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)

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

        solar_panel_client = branch_client.solarPanel.get_first()
        solar_panel_client.cell.panels[-1].subsystem.satellite.components[0].thermal_interface_A[0].satellite.topology

        con_ops_client = branch_client.con_ops.get_first()
        con_ops_client.targetGroups[0].targetAssociations

        assert branch_client.solarPanel.get_first(
        ) == solar_panel_client.cell.panels[0]

        assert branch_client.solarPanel.get_first(
        ) is not solar_panel_client.cell.panels[0]


def test_different_block():
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)

        subsystem_client = branch_client.subsystem.create(
            name='One subsystem to rule them all',
            satellite='5'
        )

        subsystem_client_2 = subsystem_client.update(
            name='One subsystem to find them')

        subsystem_client_3 = branch_client.subsystem.get(subsystem_client.id)

        assert subsystem_client == subsystem_client_2 == subsystem_client_3

        subsystem_client.delete()


def test_block_class_client_options():
    agent_template_blocks = [
        'TriadAlgorithm',
        'AveragingAlgorithm',
        'MEKFAlgorithm',
        'EKFAlgorithm',
        'GPSAlgorithm',
        'SlidingModeAlgorithm',
        'Battery',
        'BatteryCell',
        'BodyFrameVector',
        'BusRegulator',
        'Component',
        'BatteryPack',
        'SolarPanel',
        'QuasiRegDetTopology',
        'FullyRegDetTopology',
        'SingleConvHybridTopology',
        'TwoConvMpptTopology',
        'SingleConvMpptTopology',
        'Topology',
        'ReactionWheel',
        'Magnetorquer',
        'DirectionSensor',
        'OpticalAttitudeSensor',
        'VectorSensor',
        'PositionSensor',
        'AngularVelocitySensor',
        'Cooler',
        'Heater',
        'SphericalFuelTank',
        'SpherocylinderFuelTank',
        'ConOps',
        'GroupCondition',
        'Condition',
        'SameTargetConditionGrouping',
        'ResistanceLoad',
        'PowerLoad',
        'ActuatorLoad',
        'LoadState',
        'CircularFieldOfView',
        'RectangularFieldOfView',
        'FOVConstraint',
        'FuelReservoir',
        'OperationalMode',
        # 'Orbit',  # TODO -- this is a valid option, but it shouldn't be -- see model/templates.py
        'PassivePointingMode',
        'LockPointingMode',
        'MaxAlignPointingMode',
        'PointingMode',
        'ActivePointingMode',
        'CelestialVector',
        'LocalVector',
        'TargetVector',
        'TargetGroupVector',
        'ReferenceVector',
        'Satellite',
        'SimulatableSatellite',
        'SolarArray',
        'SolarCell',
        'Subsystem',
        'FixedSurface',
        'SunTrackingSurface',
        'AntiSunTrackingSurface',
        'SurfaceMaterial',
        'TargetGroup',
        'SpaceTarget',
        'GroundTarget',
        'CelestialTarget',
        'TempControllerState',
        'ThermalInterface',
        'ThermalInterfaceMaterial'
    ]
    scenario_blocks = [
        'Agent',
        'ClockConfig',
        'Orbit',
    ]
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        vehicle_branch_client = sedaro_client.get_branch(WILDFIRE_A_T_ID)
        for block in agent_template_blocks:
            assert isinstance(
                getattr(vehicle_branch_client, block), BlockClassClient
            )
        scenario_branch_client = sedaro_client.get_branch(WILDFIRE_SCENARIO_ID)
        for block in scenario_blocks:
            assert isinstance(
                getattr(scenario_branch_client, block), BlockClassClient
            )


if __name__ == "__main__":
    # start timer after first get to make sure backend is ready to accept request
    start_time = time.perf_counter()
    print('\nstarting\n')
    test_get()
    # test_create_update_and_delete_block()
    # test_update_rel_and_cascade_delete()
    # test_traversing_and_equality()
    # test_different_block()
    # test_block_class_client_options()
    print(f'\ndone in {round(time.perf_counter() - start_time, 2)} seconds\n')
