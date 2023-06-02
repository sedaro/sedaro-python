import string
from random import choices

import pytest
from config import API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID
from sedaro_2 import SedaroApiClient
from sedaro_2.block_client import BlockClient
from sedaro_2.branch_clients import (AgentTemplateBranch, BranchClient,
                                     ScenarioBranch)
from sedaro_2.exceptions import NonexistantBlockError, SedaroApiException
from sedaro_2.settings import ID

_letters_and_numbers = string.ascii_uppercase + string.digits + string.ascii_lowercase


def _random_str(length=10):
    return ''.join(choices(_letters_and_numbers, k=length))


sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def test_get():
    # test get agent template
    assert isinstance(
        sedaro.agent_template_branch(SIMPLESAT_A_T_ID), AgentTemplateBranch
    )
    with pytest.raises(TypeError, match='VehicleTemplate not ScenarioTemplate'):
        sedaro.agent_template_branch(SIMPLESAT_SCENARIO_ID)

    # test get scenario
    assert isinstance(
        sedaro.scenario_branch(SIMPLESAT_SCENARIO_ID), ScenarioBranch
    )
    with pytest.raises(TypeError, match='ScenarioTemplate not VehicleTemplate'):
        sedaro.scenario_branch(SIMPLESAT_A_T_ID)


def test_get_blocks_all_and_single():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)
    components = branch.Component.get_all()
    component = components[-1]
    assert branch.Component.get(component.id) == component

    with pytest.raises(KeyError, match='no Block with id'):
        branch.Component.get('not-an-id')

    with pytest.raises(KeyError, match='no "PowerProcessor" with id'):
        battery_id = branch.Battery.get_all_ids()[0]
        branch.PowerProcessor.get(battery_id)


def test_create_update_and_delete_block():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    battery_cell_client = branch.BatteryCell.create(
        partNumber='987654321',
        manufacturer='Sedaro Corporation',
        esr=0.01,
        maxChargeCurrent=15,
        maxDischargeCurrent=100,
        minSoc=0.2,
        capacity=500,
        curve=[[0, 0.5, 1], [12.2, 14.1, 16.8]],
    )

    bc_id = battery_cell_client.id

    assert battery_cell_client == branch.BatteryCell.get(bc_id)

    new_part_number = "Let's gooo!!!!!!!!!!!!"

    updated = battery_cell_client.update(partNumber=new_part_number)

    assert new_part_number == battery_cell_client.partNumber == branch.BatteryCell.get(
        bc_id).partNumber == updated.partNumber

    res = battery_cell_client.delete()
    assert res == bc_id

    try:
        battery_cell_client.update(partNumber="123456789")
    except NonexistantBlockError as e:
        msg = str(e)
        assert msg == f'The referenced "BatteryCell" (id: {bc_id}) no longer exists.'


def test_update_rel_and_cascade_delete():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    num_subsystems = len(branch.Subsystem.get_all_ids())

    subsystem = branch.Subsystem.create(
        name=_random_str(),
    )

    ss_id = subsystem.id

    assert len(branch.Subsystem.get_all_ids()) == num_subsystems + 1
    assert ss_id in branch.Subsystem.get_all_ids()

    component = branch.Component.create(
        name=_random_str(),
        subsystem=ss_id
    )
    c_id = component.id

    # make sure other side of relationship was also updated
    assert component in subsystem.components

    subsystem.delete()

    try:
        subsystem.delete()
    except NonexistantBlockError as e:
        msg = str(e)
        assert msg == f'The referenced "Subsystem" (id: {ss_id}) no longer exists.'

    # make sure component is also deleted when subsystem is deleted
    try:
        component.update(name='Trying to update name')
    except NonexistantBlockError as e:
        msg = str(e)
        assert msg == f'The referenced "Component" (id: {c_id}) no longer exists.'


def test_traversing_and_equality_and_some_get_methods():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)
    power_subsystem = branch.Subsystem.get_where(category='POWER')[0]

    solar_cell = branch.SolarCell.create(
        partNumber=_random_str(),
        manufacturer='Sedaro Corporation',
        openCircuitVoltage=3.95,
        shortCircuitCurrent=0.36,
        maxPowerVoltage=3.54,
        maxPowerCurrent=0.345,
        numJunctions=3,
    )
    solar_panel = branch.SolarPanel.create(
        name=_random_str(),
        numSeries=1,
        numParallel=1,
        blockingDiodeDrop=1,
        subsystem=power_subsystem.id,
        cell=solar_cell.id
    )

    assert solar_panel == branch.SolarPanel.get_last()
    assert solar_panel in branch.SolarPanel.get_all()
    assert solar_cell == power_subsystem.components[-1].cell

    assert isinstance(branch.PowerProcessor.get_first(), BlockClient)

    solar_cell.delete()
    solar_panel.delete()


def test_block_client_equality():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    subsystem = branch.Subsystem.create(
        name='One subsystem to rule them all',
    )

    subsystem_2 = subsystem.update(
        name='One subsystem to find them')

    subsystem_3 = branch.Subsystem.get(subsystem.id)

    assert subsystem == subsystem_2 == subsystem_3

    subsystem.delete()


def test_block_client_clone():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    # a Block that requires a unique "name" attribute
    subsystem = branch.Subsystem.create(
        name='Custom Subsystem',
    )

    subsystem_clone = subsystem.clone()
    assert isinstance(subsystem_clone, BlockClient)

    # a Block without a "name" attribute
    solar_cell = branch.SolarCell.create(
        partNumber=_random_str(),
        manufacturer='Sedaro Corporation',
        openCircuitVoltage=3.95,
        shortCircuitCurrent=0.36,
        maxPowerVoltage=3.54,
        maxPowerCurrent=0.345,
        numJunctions=3,
    )

    solar_cell_clone = solar_cell.clone()
    assert isinstance(solar_cell_clone, BlockClient)

    branch.crud(delete=[subsystem_clone.id, subsystem.id, solar_cell_clone.id, solar_cell.id])


def test_some_errors():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    with pytest.raises(ValueError, match=f'Must provide fields'):
        branch.Subsystem.create()

    subsystem = branch.Subsystem.create(name=_random_str())

    with pytest.raises(ValueError, match=f'Invalid value for "{ID}"'):
        subsystem.update(**{**subsystem.data, **{ID: 'asdfasdfasdf'}})

    subsystem.delete()


def test_ignore_id_and_type_in_create():
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)

    BAD_ID = 'catch me if you can'

    subsystem = branch.Subsystem.create(
        name=_random_str(),
        id=BAD_ID,
        type='WrongType'
    )

    assert isinstance(subsystem, BlockClient)
    assert subsystem.type == 'Subsystem'
    assert subsystem.id != BAD_ID

    subsystem.delete()


def test_active_comm_interfaces_tuple():
    """Check validation of the Vehicle Template activeCommInterfaces field"""
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)
    # Check valid tuples
    if not branch.crud(
        root={'activeCommInterfaces': [[False, "Comms", 5], [True, "Interface", 112]]}
    ):
        assert False
    # Check invalid value type
    try:
        branch.crud(
            root={'activeCommInterfaces': [[False, "Interface", 5], [0.5, "Interface", 5]]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check int at wrong index
    try:
        branch.crud(
            root={'activeCommInterfaces': [[5, "Interface", 5]]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check bool at wrong index
    try:
        branch.crud(
            root={'activeCommInterfaces': [[False, True, 5]]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check string at wrong index
    try:
        branch.crud(
            root={'activeCommInterfaces': [[False, "Interface", "5"]]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check size less than 3
    try:
        branch.crud(
            root={'activeCommInterfaces': [[False, "Interface"]]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check size greater than 3
    try:
        branch.crud(
            root={'activeCommInterfaces': [[False, "Interface", 5, True]]},
        )
        assert False
    except SedaroApiException as e:
        pass

    assert True


def test_attitude_solution_error_tuple():
    """Check validation of the Vehicle Template attitudeSolutionError field"""
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)
    validList = [0.25, 0.5, 0.75]
    # Check valid tuple
    if not branch.crud(root={'attitudeSolutionError': None}) or \
            not branch.crud(root={'attitudeSolutionError': validList}):
        assert False
    # Check size less than 3
    try:
        branch.crud(
            root={'attitudeSolutionError': validList[:-1]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check size greater than 3
    try:
        branch.crud(
            root={'attitudeSolutionError': validList + [1.0]},
        )
        assert False
    except SedaroApiException as e:
        pass
    # Check non-float values
    for i in range(len(validList)):
        failList = validList.copy()
        failList[i] = "Fail"
        try:
            branch.crud(
                root={'attitudeSolutionError': failList},
            )
            assert False
        except SedaroApiException as e:
            pass
    # Check non-list value
    try:
        branch.crud(
            root={'attitudeSolutionError': 50},
        )
        assert False
    except SedaroApiException as e:
        pass

    assert True


def test_power_command_tuple():
    """Check validation of the Solar Array powerCommand field"""
    branch = sedaro.agent_template_branch(SIMPLESAT_A_T_ID)
    # Check valid tuples
    if not branch.crud(blocks=[{
        'type': "SolarArray",
        'name': "Temp Array 1",
            'powerCommand': [None, None]}]):
        assert False
    if not branch.crud(blocks=[{
        'type': "SolarArray",
        'name': "Temp Array 2",
            'powerCommand': [0.0, None]}]):
        assert False
    if not branch.crud(blocks=[{
        'type': "SolarArray",
        'name': "Temp Array 3",
            'powerCommand': [None, 0.5]}]):
        assert False
    if not branch.crud(blocks=[{
        'type': "SolarArray",
        'name': "Temp Array 4",
            'powerCommand': [0.0, 0.5]}]):
        assert False
    # Delete created solar arrays
    branch.crud(delete=branch.data['index']['SolarArray'])
    # Check non-float values
    try:
        branch.crud(blocks=[{
            'type': "SolarArray",
            'name': "Temp Array 1",
            'powerCommand': ["Fail", 0.5]}])
        assert False
    except SedaroApiException as e:
        pass
    # Check size greater than 2
    try:
        branch.crud(blocks=[{
            'type': "SolarArray",
            'name': "Temp Array 1",
            'powerCommand': [0.25, 0.5, 0.75]}])
        assert False
    except SedaroApiException as e:
        pass
    # Check size less than 2
    try:
        branch.crud(blocks=[{
            'type': "SolarArray",
            'name': "Temp Array 1",
            'powerCommand': []}])
        assert False
    except SedaroApiException as e:
        pass
    # Check non-list value
    try:
        branch.crud(blocks=[{
            'type': "SolarArray",
            'name': "Temp Array 1",
            'powerCommand': "Fail"}])
        assert False
    except SedaroApiException as e:
        pass
    # All tests passed
    assert True


def run_tests():
    test_get()
    test_get_blocks_all_and_single()
    test_create_update_and_delete_block()
    test_update_rel_and_cascade_delete()
    test_traversing_and_equality_and_some_get_methods()
    test_block_client_equality()
    test_block_client_clone()
    test_some_errors()
    test_active_comm_interfaces_tuple()
    test_attitude_solution_error_tuple()
    test_power_command_tuple()
