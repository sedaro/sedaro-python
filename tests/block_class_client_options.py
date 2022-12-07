from sedaro import SedaroApiClient
from sedaro.block_class_client import BlockClassClient

from config import HOST, API_KEY, WILDFIRE_A_T_ID, WILDFIRE_SCENARIO_ID


def test_block_class_client_options():
    agent_template_blocks = [
        'ActuatorLoad',
        'AngularVelocitySensor',
        'AveragingAlgorithm',
        'Battery',
        'BatteryCell',
        'BatteryPack',
        'BodyFrameVector',
        'BusRegulator',
        'CelestialTarget',
        'CelestialVector',
        'CircularFieldOfView',
        'Component',
        'Condition',
        'ConstantLoad',
        'Cooler',
        'DirectionSensor',
        'EkfAlgorithm',
        'FovConstraint',
        'GpsAlgorithm',
        'GroundTarget',
        'GroupCondition',
        'Heater',
        'LoadState',
        'LocalVector',
        'LockPointingMode',
        'Magnetorquer',
        'MaxAlignPointingMode',
        'MekfAlgorithm',
        'OperationalMode',
        'OpticalAttitudeSensor',
        'PassivePointingMode',
        'PositionSensor',
        'ReactionWheel',
        'RectangularFieldOfView',
        'Satellite',
        'SlidingModeAlgorithm',
        'SolarArray',
        'SolarCell',
        'SolarPanel',
        'SpaceTarget',
        'Subsystem',
        'Surface',
        'SurfaceMaterial',
        'TargetGroup',
        'TargetGroupVector',
        'TargetVector',
        'TempControllerState',
        'ThermalInterface',
        'ThermalInterfaceMaterial',
        'Topology',
        'TriadAlgorithm',
        'VectorSensor',
    ]
    scenario_blocks = [
        'Agent',
        'ClockConfig',
        'Orbit',
    ]
    with SedaroApiClient(api_key=API_KEY, host=HOST) as sedaro_client:
        for branch_id, blocks in [[WILDFIRE_A_T_ID, agent_template_blocks], [WILDFIRE_SCENARIO_ID, scenario_blocks]]:
            branch_client = sedaro_client.get_branch(branch_id)

            for block in blocks:
                bcc = getattr(branch_client, block)
                assert isinstance(bcc, BlockClassClient)

                # these blocks can't be "created"
                if any(string in block for string in ['Topology', 'Satellite']) or block == 'Battery':
                    try:
                        getattr(bcc, 'create')()
                    except AttributeError as e:
                        err_msg = str(e)
                        assert err_msg == f'There is no create method on a "{block}" BlockClassClient because this type of Sedaro Block is not createable.'
                    continue

                try:
                    getattr(bcc, 'create')()
                except TypeError as e:
                    # make sure create property exists, can be called, and raises error when called empty
                    if not (all(
                        s in str(e) for s in {'__new__() missing', 'required keyword-only argument'}
                    ) or str(e) == 'No input given. args or kwargs must be given.'):
                        print(block, type(e), str(e))
                except Exception as e:
                    # print any other erros that happen
                    print(block, type(e), str(e))


def run_tests():
    test_block_class_client_options()
