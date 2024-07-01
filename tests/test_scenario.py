from config import API_KEY, HOST, WILDFIRE_SCENARIO_ID

from sedaro import SedaroApiClient

sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

def test_externals_delete():
    scenario = sedaro.scenario(WILDFIRE_SCENARIO_ID)
    created_blocks = []
    try:
        block = scenario.PerRoundExternalState.create(
            agents=[scenario.Agent.get_first().id],
            engineIndex=2,
            produced=['block.a.maxPower'],
            consumed=['block.b.compliance']
        )
        created_blocks.append(block.id)

        assert len(scenario.ExternalState.get_all_ids()) > 0

        scenario.delete_all_external_state_blocks()

        assert len(scenario.ExternalState.get_all_ids()) == 0
    finally:
        # Delete all potentially added blocks to avoid leaving behind unintended changes
        if len(created_blocks):
            try:
                scenario.delete_all_external_state_blocks()
            except:
                scenario.update(delete=created_blocks)

def run_tests():
    test_externals_delete()
