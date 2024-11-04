def test_workspace():
    HOST = 'http://localhost'
    API_KEY = 'PPM4H8839D26YcC6bk5gVB.5gfD7EMb4x20KlXcnJJkJ2FwHEX9dfjwl5Qdkh3E_zSUpOCaXVHPaK8CW7TOTc5XMwxX58yn4uig-t5nUNqKXA'

    import time

    import pytest

    from sedaro import SedaroApiClient
    from sedaro.exceptions import SedaroApiException
    from sedaro.models.workspace.Workspace import Workspace

    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    workspaces1 = sedaro.Workspace.get()
    assert all(isinstance(w, Workspace) for w in workspaces1)

    w_new = sedaro.Workspace.create(name='1')
    assert (isinstance(w_new, Workspace))

    time.sleep(3)  # need time for newly created workspace to be retreivable

    workspaces2 = sedaro.Workspace.get()
    assert len(workspaces2) == len(workspaces1) + 1

    w_new2 = sedaro.Workspace.get(w_new.id)
    assert (isinstance(w_new2, Workspace))
    assert w_new2.id == w_new.id

    w_new2.delete()

    with pytest.raises(
        SedaroApiException,
        match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
    ):
        sedaro.Workspace.get(w_new.id)


def run_tests():
    test_workspace()
