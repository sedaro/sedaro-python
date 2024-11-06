import time

import pytest
from config import API_KEY, HOST

from sedaro import SedaroApiClient
from sedaro.exceptions import SedaroApiException
from sedaro.models.project.Project import Project
from sedaro.models.repository.Repository import Repository
from sedaro.models.workspace.Workspace import Workspace
from sedaro.settings import SCENARIO


def test_workspace():

    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    workspaces1 = sedaro.Workspace.get()
    assert all(isinstance(w, Workspace) for w in workspaces1)

    w_new = sedaro.Workspace.create(name='new workspace')
    try:
        assert (isinstance(w_new, Workspace))

        time.sleep(4)  # need time for newly created workspace to be retreivable

        workspaces2 = sedaro.Workspace.get()
        assert len(workspaces2) == len(workspaces1) + 1

        w_new2 = sedaro.Workspace.get(w_new.id)
        assert (isinstance(w_new2, Workspace))
        assert w_new2.id == w_new.id

        w_new.update(name='newer workspace')
        assert w_new.name == 'newer workspace'
        assert w_new2.name != w_new.name

        w_new.refresh()
        assert w_new.name == w_new.name

    finally:
        w_new.delete()

    with pytest.raises(
        SedaroApiException,
        match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
    ):
        sedaro.Workspace.get(w_new.id)


def test_repository():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    w_new = sedaro.Workspace.create(name='new workspace')

    try:
        repos = sedaro.Repository.get()
        assert all(isinstance(r, Repository) for r in repos)
        repo_new = sedaro.Repository.create(name='new repo', metamodelType=SCENARIO, workspace=w_new.id)
        assert isinstance(repo_new, Repository)
        assert repo_new.metamodelType == SCENARIO
        assert repo_new.workspace['id'] == w_new.id
        assert repo_new.name == 'new repo'

        repo_new2 = sedaro.Repository.get(repo_new.id)
        assert repo_new2.id == repo_new.id

        repo_new.update(name='newer repo')
        assert repo_new.name == 'newer repo'
        assert repo_new2.name != repo_new.name
        repo_new2.refresh()
        assert repo_new2.name == repo_new.name

        all_repos = sedaro.Repository.get()

        repo_new.delete()

        assert len(sedaro.Repository.get()) == len(all_repos) - 1

        with pytest.raises(
            SedaroApiException,
            match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
        ):
            repo_new.refresh()

    finally:
        w_new.delete()


def test_project():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    w_new = sedaro.Workspace.create(name='new workspace')

    try:
        all_projects = sedaro.Project.get()
        assert all(isinstance(p, Project) for p in all_projects)

        p_new = sedaro.Project.create(name='new project', workspace=w_new.id)
        assert isinstance(p_new, Project)

        p_new2 = sedaro.Project.get(p_new.id)
        assert p_new.id == p_new2.id

        p_new.update(name='new project 2')
        assert p_new.name == 'new project 2'
        assert p_new2.name != p_new.name
        p_new2.refresh()
        assert p_new2.name == p_new.name

        p_new.delete()

        with pytest.raises(
            SedaroApiException,
            match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
        ):
            p_new2.refresh()
    finally:
        w_new.delete()


def run_tests():
    test_workspace()
    test_repository()
    test_project()
