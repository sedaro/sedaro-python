from config import API_KEY, HOST, SIMPLESAT_A_T_ID, SIMPLESAT_SCENARIO_ID

from sedaro import SedaroApiClient
from sedaro.branches import AgentTemplateBranch, ScenarioBranch
from sedaro.branches.blocks import Block, BlockType

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)


def test_block_type_options():
    for get_method, branch_id, TemplateBranch in [
        [sedaro.agent_template, SIMPLESAT_A_T_ID, AgentTemplateBranch],
        [sedaro.scenario, SIMPLESAT_SCENARIO_ID, ScenarioBranch]
    ]:
        expected_block_names = sorted([k for k,v in TemplateBranch.__dict__['__annotations__'].items() if v == BlockType])
        branch = get_method(branch_id)
        branch_block_names = sorted(branch.data['_blockNames'])
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
