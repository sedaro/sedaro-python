from config import HOST, SIMPLESAT_A_T_ID

from sedaro import SedaroApiClient
from sedaro.branches import AgentTemplateBranch


def test_crud_using_auth_handle():

    try:
        from config import AUTH_HANDLE
    except ImportError:
        raise ImportError('Test failed because AUTH_HANDLE not found in config.py. Please add AUTH_HANDLE to config.py')

    from tests.test_crud_and_traversal import _random_str

    sedaro = SedaroApiClient(host=HOST, auth_handle=AUTH_HANDLE)

    branch = sedaro.agent_template(SIMPLESAT_A_T_ID)
    # test get agent template
    assert isinstance(branch, AgentTemplateBranch)

    subsystem = branch.Subsystem.create(name=_random_str())

    subsystem.update(name=_random_str())

    subsystem.delete()
