from sedaro import SedaroApiClient
from sedaro.block_class_client import BlockClassClient

from config import HOST, API_KEY, WILDFIRE_A_T_ID, WILDFIRE_SCENARIO_ID


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
        # 'Orbit',  # TODO -- this is a temporarily valid option, but it shouldn't be (so don't show to users in readme) -- see model/templates.py
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


def run_tests():
    test_block_class_client_options()
