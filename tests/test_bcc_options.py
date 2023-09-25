from sedaro import SedaroApiClient
from sedaro.branches.blocks import Block, BlockType

from config import API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


# TODO: if update these lists, also update type hints of respective AgentTemplateBranch
agent_template_blocks = [
    'AngularVelocitySensor',
    'Antenna',
    'AveragingAlgorithm',
    'Battery',
    'BatteryCell',
    'BatteryPack',
    'BodyFrameVector',
    'BodyInFovCondition',
    'BusRegulator',
    'CelestialTarget',
    'CelestialVector',
    'CircularFieldOfView',
    'Component',
    'ComponentToScalarCondition',
    'CompoundCondition',
    'Cooler',
    'CooperativeTransmitInterface',
    'DataBus',
    'DataInterface',
    'DataMode',
    'DataStorage',
    'DataType',
    'DirectionSensor',
    'EkfAlgorithm',
    'FixedSurface',
    'FuelReservoir',
    'FullyRegDetPowerProcessor',
    'GpsAlgorithm',
    'GroundTarget',
    'Heater',
    'InternalDataInterface',
    'LaserCommModule',
    'LoadState',
    'LocalVector',
    'LockPointingMode',
    'Magnetorquer',
    'MaxAlignPointingMode',
    'MekfAlgorithm',
    'Modem',
    'SpacecraftOperationalMode',
    'OpticalAttitudeSensor',
    'Orbit',
    'PassivePointingMode',
    'PassiveTransmitInterface',
    'PidAlgorithm',
    'PositionSensor',
    'PowerLoad',
    'PhotovoltaicPowerProcessor',
    'QuasiRegDetPowerProcessor',
    'ReactionWheel',
    'ReceiveInterface',
    'RectangularFieldOfView',
    'ResistanceLoad',
    'SameTargetMultiCondition',
    'SatelliteToSatelliteCondition',
    'SatelliteToScalarCondition',
    'SatelliteToTargetCondition',
    'ScanFieldOfViewArticulationMode',
    'SingleConvHybridPowerProcessor',
    'SingleConvMpptPowerProcessor',
    'SlidingModeAlgorithm',
    'SolarArray',
    'SolarCell',
    'SolarPanel',
    'SpaceTarget',
    'SphericalFuelTank',
    'SpherocylinderFuelTank',
    'StaticFieldOfViewArticulationMode',
    'StaticThrustControlAlgorithm',
    'Subsystem',
    'SunTrackingSurface',
    'SurfaceMaterial',
    'TargetGroup',
    'TargetGroupInFovCondition',
    'TargetGroupToSatelliteCondition',
    'TargetGroupToScalarCondition',
    'TargetGroupToTargetCondition',
    'TargetGroupVector',
    'TargetInFovCondition',
    'TargetToScalarCondition',
    'TargetToTargetCondition',
    'TargetVector',
    'TempControllerState',
    'ThermalDesignLayout',
    'ThermalInterface',
    'ThermalInterfaceMaterial',
    'Thruster',
    'TimeCondition',
    'TrackingFieldOfViewArticulationMode',
    'TriadAlgorithm',
    'TwoConvMpptPowerProcessor',
    'VectorInFovCondition',
    'VectorSensor',
    'VectorTrackingSurface'
]

# TODO: if update these lists, also update type hints of ScenarioBranch
scenario_blocks = [
    'Agent',
    'AgentGroup',
    'ClockConfig',
    'Orbit',
    'PerRoundExternalState',
    'SpontaneousExternalState',
    'WaypointPathWithDuration',
    'WaypointPathWithTimestamps',
    'WaypointPathWithSpeed'
]


def test_block_type_options():
    for get_method, branch_id, _expected_block_names in [
        [sedaro.agent_template, SIMPLESAT_A_T_ID, agent_template_blocks],
        [sedaro.scenario, SIMPLESAT_SCENARIO_ID, scenario_blocks]
    ]:
        branch = get_method(branch_id)
        branch_block_names = sorted(branch.data['_blockNames'])
        expected_block_names = sorted(_expected_block_names)
        # CHECK: lists above are correct
        assert expected_block_names == branch_block_names, f'Extra: {set(expected_block_names) - set(branch_block_names)}, Missing: {set(branch_block_names) - set(expected_block_names)}'

        for block_name in branch_block_names:
            block_type: BlockType = getattr(branch, block_name)

            # CHECK: is a BlockType
            assert isinstance(block_type, BlockType)

            # CHECK: can use create method
            try:
                block_type.create()
            except Exception as e:
                assert isinstance(e, ValueError)
                assert 'Must provide fields' in str(e)

            # CHECK: can use get_all method
            all_blocks_of_type = block_type.get_all()
            assert type(all_blocks_of_type) == list
            if len(all_blocks_of_type):
                assert isinstance(all_blocks_of_type[0], Block)

        # CHECK: bad BlockTypes
        for bad_block in ['try_me', 'and_me', 'NO_wayYou_will_CatchMe!!!!!!']:
            try:
                getattr(branch, bad_block)
            except Exception as e:
                assert isinstance(e, AttributeError)
                expected_err = f'Unable to find an attribute or create a "{BlockType.__name__}" from string: "{bad_block}".'
                assert expected_err in str(e)


def run_tests():
    test_block_type_options()
