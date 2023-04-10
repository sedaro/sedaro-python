from config import (API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID,
                    WILDFIRE_A_T_ID, WILDFIRE_SCENARIO_ID)

from sedaro import SedaroApiClient
from sedaro.block_class_client import BlockClassClient
from sedaro.block_client import BlockClient

agent_template_blocks = [
    'DataBus',
    'Modem',
    'OpticalAttitudeSensor',
    'SurfaceMaterial',
    'TempControllerState',
    'DirectionSensor',
    'FullyRegDetPowerProcessor',
    'FuelReservoir',
    'TimeCondition',
    'SphericalFuelTank',
    'ReactionWheel',
    'TargetGroupToScalarCondition',
    'BatteryCell',
    'TwoConvMpptPowerProcessor',
    'DataStorage',
    'TransmitDataInterface',
    'SolarArray',
    'GpsAlgorithm',
    'TargetGroup',
    'CooperativeTransmitInterface',
    'PidAlgorithm',
    'Orbit',
    'VectorInFovCondition',
    'ReceiveInterface',
    'OperationalMode',
    'FixedSurface',
    'RectangularFieldOfView',
    'InternalDataInterface',
    'BodyFrameVector',
    'SolarPanel',
    'GroundTarget',
    'VectorTrackingSurface',
    'ActivePointingMode',
    'ExternalDataInterface',
    'Magnetorquer',
    'PowerProcessor',
    'PassivePointingMode',
    'SunTrackingSurface',
    'BusRegulator',
    'Thruster',
    'PowerLoad',
    'SatelliteToTargetCondition',
    'TargetGroupInFovCondition',
    'VectorSensor',
    'LaserCommModule',
    'BatteryPack',
    'ResistanceLoad',
    'ReferenceVector',
    'PassiveTransmitInterface',
    'PositionSensor',
    'DataInterface',
    'SatelliteToScalarCondition',
    'TargetGroupVector',
    'SpaceTarget',
    'Heater',
    'StaticThrustControlAlgorithm',
    'CelestialTarget',
    'TriadAlgorithm',
    'CompoundCondition',
    'QuasiRegDetPowerProcessor',
    'SingleConvHybridPowerProcessor',
    'DataType',
    'LocalVector',
    'TargetVector',
    'Satellite',
    'AveragingAlgorithm',
    'Antenna',
    'SatelliteToSatelliteCondition',
    'DataMode',
    'BodyInFovCondition',
    'TargetGroupToTargetCondition',
    'EkfAlgorithm',
    'Subsystem',
    'TargetGroupToSatelliteCondition',
    'MaxAlignPointingMode',
    'Battery',
    'CircularFieldOfView',
    'SolarCell',
    'AngularVelocitySensor',
    'CelestialVector',
    'Component',
    'MekfAlgorithm',
    'ThermalInterfaceMaterial',
    'SpherocylinderFuelTank',
    'TargetInFovCondition',
    'Cooler',
    'LoadState',
    'SingleConvMpptPowerProcessor',
    'SlidingModeAlgorithm',
    'ThermalInterface',
    'TargetToScalarCondition',
    'LockPointingMode',
    'TargetToTargetCondition',
    'SameTargetMultiCondition'
]
scenario_blocks = ['AgentGroup', 'ClockConfig', 'Orbit', 'Agent']


def test_block_class_client_options():
    for branch_id, blocks in [[SIMPLESAT_A_T_ID, agent_template_blocks], [SIMPLESAT_SCENARIO_ID, scenario_blocks]]:
        with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro:
            branch = sedaro.get_branch(branch_id)
            branch_blocks = list(branch.data['_block_names'])

            # CHECK: lists above are correct
            assert len(blocks) == len(branch_blocks)
            assert set(blocks) == set(branch_blocks)

            for block in branch_blocks:
                block_class_client: BlockClassClient = getattr(branch, block)

                # CHECK: is a Block Class Client
                assert isinstance(block_class_client, BlockClassClient)

                # CHECK: can use create method
                try:
                    block_class_client.create()
                except Exception as e:
                    assert isinstance(e, ValueError)
                    assert 'Must provide fields' in str(e)

                # CHECK: can use get_all method
                all_blocks_of_type = block_class_client.get_all()
                assert type(all_blocks_of_type) == list
                if len(all_blocks_of_type):
                    assert isinstance(all_blocks_of_type[0], BlockClient)

        # CHECK: bad block class clients
        for bad_block in ['try_me', 'and_me', 'NO_wayYou_will_CatchMe!!!!!!']:
            try:
                getattr(branch, bad_block)
            except Exception as e:
                assert isinstance(e, AttributeError)
                assert f'Unable to create a "BlockClassClient" from string: "{bad_block}".' in str(e)


def run_tests():
    test_block_class_client_options()
