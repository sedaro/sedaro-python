from random import randrange
import time

from sedaro import SedaroApiClient
from sedaro.exceptions import NonexistantBlockError
from sedaro.block_class_client import BlockClassClient
from sedaro.block_client import BlockClient
from sedaro.branch_client import BranchClient

HOST = 'http://localhost:80'
# TODO: remove this
# NOTE: update the API_KEY and WILDFIRE_A_T_ID for things that work with your dev environment
# NOTE: these are temporary for Zach's dev environment
API_KEY = '1.-RjK0kE34B5z-V7BqBVdhSMLgHq9UTGB7iIZYTpoDGfZpn2cQPWE9kz_G9LapUshx7inFFTmN_xNMS5YnGMW-w'
WILDFIRE_A_T_ID = 53
WILDFIRE_SCENARIO_ID = 55


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


def test_different_block():
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


def test_run_simulation():
    from sedaro_base_client.apis.tags import jobs_api

    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        print('\nTesting running simulation from client...\n')
        scenario_client = sedaro_client.get_branch(WILDFIRE_SCENARIO_ID)

        # Start simulation
        jobs_api_client = jobs_api.JobsApi(sedaro_client)
        response = jobs_api_client.start_simulation(
            path_params={'branchId': scenario_client.id})

        # Get status #1
        response = jobs_api_client.get_simulations(
            path_params={'branchId': scenario_client.id}, query_params={'latest': ''}
        )
        job = response.body[0]
        print(job['status'], '-', round(
            job['progress']['percentComplete'], 2), '%')
        time.sleep(5)

        # Get status #2
        response = jobs_api_client.get_simulations(
            path_params={'branchId': scenario_client.id}, query_params={'latest': ''}
        )
        job = response.body[0]
        print('')
        print(job['status'], '-', round(
            job['progress']['percentComplete'], 2), '%')
        time.sleep(5)

        # Terminate
        print('\nTerminating...')
        response = jobs_api_client.terminate_simulation(
            path_params={'branchId': scenario_client.id, 'jobId': job.id}
        )
        print('')
        print(response.body['message'])
        print('\nDone!\n')


if __name__ == "__main__":
    # start timer after first get to make sure backend is ready to accept request
    test_get()

    start_time = time.perf_counter()
    print('\nRunning client tests and starting timer')
    test_create_update_and_delete_block()
    test_update_rel_and_cascade_delete()
    test_traversing_and_equality()
    test_different_block()
    test_block_class_client_options()
    print(
        f'\nFinished tests in {round(time.perf_counter() - start_time, 2)} seconds'
    )

    # test simulation outside of timer above
    test_run_simulation()
