import string
from random import choices

import pytest
from config import API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID, WILDFIRE_A_T_ID

from sedaro import SedaroApiClient
from sedaro.branches import AgentTemplateBranch, Branch, ScenarioBranch
from sedaro.branches.blocks import Block
from sedaro.exceptions import NonexistantBlockError, SedaroApiException
from sedaro.settings import ID

_letters_and_numbers = string.ascii_uppercase + \
    string.digits + string.ascii_lowercase


def _random_str(length=10):
    return ''.join(choices(_letters_and_numbers, k=length))


sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def test_get():
    # test get agent template
    assert isinstance(
        sedaro.agent_template(SIMPLESAT_A_T_ID), AgentTemplateBranch
    )
    with pytest.raises(TypeError, match='cannot be of type "Scenario".'):
        sedaro.agent_template(SIMPLESAT_SCENARIO_ID)

    # test get scenario
    assert isinstance(
        sedaro.scenario(SIMPLESAT_SCENARIO_ID), ScenarioBranch
    )
    with pytest.raises(TypeError, match='not "Spacecraft"'):
        sedaro.scenario(SIMPLESAT_A_T_ID)

    for id_ in (SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID):
        assert isinstance(sedaro.Branch.get(id_), Branch)


def test_keying_into_root_attrs():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    assert branch.type == 'Spacecraft'
    assert isinstance(branch.attitude, dict)
    assert isinstance(branch.enabledModules, list)
    assert isinstance(branch.angularVelocity, dict)
    assert isinstance(branch.migrated, (type(None), str))


def test_updating_root_attrs():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    prev_mass = branch.mass

    branch.update(mass=prev_mass + 1)
    assert branch.mass == prev_mass + 1

    branch.update(mass=prev_mass)
    assert branch.mass == prev_mass


def test_get_blocks_all_and_single():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    components = branch.Component.get_all()
    component = components[-1]
    assert branch.Component.get(component.id) == component

    with pytest.raises(KeyError, match='no Block with id'):
        branch.Component.get('not-an-id')

    with pytest.raises(KeyError, match='no "PowerProcessor" with id'):
        battery_id = branch.Battery.get_all_ids()[0]
        branch.PowerProcessor.get(battery_id)


def test_create_update_and_delete_block():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

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
        assert msg == f'The referenced Block with ID: {bc_id} no longer exists.'


def test_update_rel_and_cascade_delete():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

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
        assert msg == f'The referenced Block with ID: {ss_id} no longer exists.'

    # make sure component is also deleted when subsystem is deleted
    try:
        component.update(name='Trying to update name')
    except NonexistantBlockError as e:
        msg = str(e)
        assert msg == f'The referenced Block with ID: {c_id} no longer exists.'


def test_traversing_and_equality_and_some_get_methods():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
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

    assert isinstance(branch.PowerProcessor.get_first(), Block)
    assert branch.powerProcessor == branch.PowerProcessor.get_first()

    solar_cell.delete()
    solar_panel.delete()


def test_block_client_equality():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

    subsystem = branch.Subsystem.create(
        name=f'One subsystem to rule them all {_random_str()}',
    )

    subsystem_2 = subsystem.update(
        name=f'One subsystem to find them {_random_str()}')

    subsystem_3 = branch.Subsystem.get(subsystem.id)

    assert subsystem == subsystem_2 == subsystem_3

    subsystem.delete()


def test_block_client_clone():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

    # a Block that requires a unique "name" attribute
    subsystem = branch.Subsystem.create(
        name=f'Custom Subsystem {_random_str()}',
    )

    subsystem_clone = subsystem.clone()
    assert isinstance(subsystem_clone, Block)

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
    assert isinstance(solar_cell_clone, Block)

    branch.update(delete=[subsystem_clone.id, subsystem.id, solar_cell_clone.id, solar_cell.id])


def test_some_errors():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

    subsystem = branch.Subsystem.create(name=_random_str())

    with pytest.raises(ValueError, match=f'Invalid value for "{ID}"'):
        subsystem.update(**{**subsystem.data, **{ID: 'asdfasdfasdf'}})

    subsystem.delete()


def test_ignore_id_and_type_in_create():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

    BAD_ID = 'catch me if you can'

    subsystem = branch.Subsystem.create(
        name=_random_str(),
        id=BAD_ID,
        type='WrongType'
    )

    assert isinstance(subsystem, Block)
    assert subsystem.type == 'Subsystem'
    assert subsystem.id != BAD_ID

    subsystem.delete()


def test_active_comm_interfaces_tuple():
    """Check validation of the Vehicle Template activeCommInterfaces field"""
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)

    def crud_aci(val): branch.update(activeCommInterfaces=val)

    # Check valid tuples
    crud_aci([[False, "Comms", 5], [True, "Interface", 112]])

    for val in [
        [[False, "Interface", 5], [0.5, "Interface", 5]],  # invalid value type
        [[5, "Interface", 5]],  # int at wrong index
        [[False, True, 5]],  # bool at wrong index
        [[False, "Interface", "5"]],  # string at wrong index
        [[False, "Interface"]],  # size less than 3
        [[False, "Interface", 5, True]],  # size greater than 3
    ]:
        with pytest.raises(SedaroApiException):
            crud_aci(val)


def test_attitude_solution_error_tuple():
    """Check validation of the Vehicle Template attitudeSolutionError field"""
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    valid_list = [0.25, 0.5, 0.75]

    def crud_ase(val): branch.update(attitudeSolutionError=val)

    # Check valid tuple
    crud_ase(None)
    crud_ase(valid_list)

    def check_bad_ase(val):
        """Update attitudeSolutionError field with val and ensure raises error"""
        with pytest.raises(SedaroApiException):
            crud_ase(val)

    check_bad_ase(valid_list[:-1])  # Check size less than 3
    check_bad_ase(valid_list + [1.0])  # Check size greater than 3
    for i in range(len(valid_list)):  # Check non-float values in list
        failList = valid_list.copy()
        failList[i] = "Fail"
        check_bad_ase(failList)
    check_bad_ase(50)  # Check non-list value


def test_multiblock_crud_with_ref_ids():
    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    batt_pack_name = f'Battery Pack {_random_str()}'
    batt_cell_part_number = f'Battery Cell {_random_str()}'
    branch.update(blocks=[
        {'type': 'BatteryPack', 'name': batt_pack_name,
            "numSeries": 1, "numParallel": 1, 'cell': '$-batt-cell'},
        {
            'id': '$-batt-cell',
            'type': 'BatteryCell',
            'partNumber': batt_cell_part_number,
            'esr': 0.01,
            'maxChargeCurrent': 15,
            'maxDischargeCurrent': 100,
            'minSoc': 0.2,
            'capacity': 500,
            'curve': [[0, 0.5, 1], [12.2, 14.1, 16.8]],
        },
    ])

    bp = branch.BatteryPack.get_where(name=batt_pack_name)[0]
    bc = branch.BatteryCell.get_where(partNumber=batt_cell_part_number)[0]
    try:
        assert bp.cell.id == bc.id
    finally:
        branch.update(delete=[bp.id, bc.id])


def test_no_duplicates_in_get_all():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)
    vehicle = sedaro.agent_template(WILDFIRE_A_T_ID)

    eDIs = vehicle.ExternalDataInterface.get_all()

    # make sure there are no duplicates even w/ double inheritance
    assert len(set(eDIs)) == len(eDIs) > 0


def run_tests():
    test_get()
    test_keying_into_root_attrs()
    test_updating_root_attrs()
    test_get_blocks_all_and_single()
    test_create_update_and_delete_block()
    test_update_rel_and_cascade_delete()
    test_traversing_and_equality_and_some_get_methods()
    test_block_client_equality()
    test_block_client_clone()
    test_some_errors()
    test_ignore_id_and_type_in_create()
    test_active_comm_interfaces_tuple()
    test_attitude_solution_error_tuple()
    test_multiblock_crud_with_ref_ids()
    test_get_all_no_duplicates()
