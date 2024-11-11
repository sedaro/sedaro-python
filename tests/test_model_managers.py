import time

import pytest
from config import API_KEY, HOST

from sedaro import SedaroApiClient
from sedaro.exceptions import SedaroApiException
from sedaro.models.project import Project
from sedaro.models.repository import Repository
from sedaro.models.workspace import Workspace
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
        assert w_new.id not in {w.id for w in sedaro.Workspace.get()}

    with pytest.raises(
        SedaroApiException,
        match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
    ):
        sedaro.Workspace.get(w_new.id)


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
        assert p_new.id not in {p.id for p in sedaro.Project.get()}

        with pytest.raises(
            SedaroApiException,
            match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
        ):
            p_new2.refresh()
    finally:
        w_new.delete()


def test_repository():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    w_new = sedaro.Workspace.create(name='new workspace')

    try:
        repos = sedaro.Repository.get()
        assert all(isinstance(r, Repository) for r in repos)
        repo_new = sedaro.Repository.create(name='new repo', metamodelType=SCENARIO, workspace=w_new.id)
        assert isinstance(repo_new, Repository)
        assert repo_new.metamodelType == SCENARIO
        assert repo_new.workspace.id == w_new.id
        assert repo_new.name == 'new repo'

        repo_new2 = sedaro.Repository.get(repo_new.id)
        assert repo_new2.id == repo_new.id

        repo_new.update(name='newer repo')
        assert repo_new.name == 'newer repo'
        assert repo_new2.name != repo_new.name
        repo_new2.refresh()
        assert repo_new2.name == repo_new.name

        repo_new.delete()
        assert repo_new.id not in {r.id for r in sedaro.Repository.get()}

        with pytest.raises(
            SedaroApiException,
            match="RESOURCE_NOT_FOUND: The requested resource does not exist or is not accessible"
        ):
            repo_new.refresh()

    finally:
        w_new.delete()


def test_relationships():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    w_new = sedaro.Workspace.create(name='new workspace')

    try:
        p_new = sedaro.Project.create(name='new project', workspace=w_new.id)
        assert isinstance(p_new, Project)

        r_new = sedaro.Repository.create(name='new repo', metamodelType=SCENARIO, workspace=w_new.id, project=p_new.id)
        assert isinstance(r_new, Repository)

        w_new.refresh()
        p_new.refresh()

        # ----------------- workspace rels -----------------
        assert all(isinstance(p, Project) for p in w_new.projects)
        assert p_new.id in {p.id for p in w_new.projects}

        assert all(isinstance(r, Repository) for r in w_new.repositories)
        assert r_new.id in {r.id for r in w_new.repositories}

        # ----------------- project rels -----------------
        assert all(isinstance(r, Repository) for r in p_new.repositories)
        assert r_new.id in {r.id for r in p_new.repositories}

        assert isinstance(p_new.workspace, Workspace)
        assert p_new.workspace.id == w_new.id

        # ----------------- repository rels -----------------
        assert isinstance(r_new.project, Project)
        assert r_new.project.id == p_new.id

        assert isinstance(r_new.workspace, Workspace)
        assert r_new.workspace.id == w_new.id

        # ----------------- equality and identity -----------------
        assert p_new.workspace == r_new.workspace == w_new
        assert p_new.workspace is not w_new
        assert r_new.workspace is not w_new

        p_new_workspace_b4_refresh = p_new.workspace
        assert p_new.workspace is p_new_workspace_b4_refresh
        p_new.refresh()
        assert p_new.workspace is not p_new_workspace_b4_refresh
        assert p_new.workspace == p_new_workspace_b4_refresh

    finally:
        w_new.delete()


def test_branching():
    sedaro = SedaroApiClient(api_key=API_KEY, host=HOST)

    w_new = sedaro.Workspace.create(name='new workspace')

    try:
        repo_new = sedaro.Repository.create(name='new repo', metamodelType=SCENARIO, workspace=w_new.id)

        assert len(repo_new.branches) == 1

        num_branchs = 1

        for (name, description, method) in (
            ('new branch', 'new branch description', sedaro.Branch.create),
            ('new branch 2', 'new branch description 2', repo_new.branch_from),
        ):
            b = method(repo_new.branches[0], name=name, description=description)
            num_branchs += 1

            assert b.name == name
            assert b.description == description

            assert b.data == sedaro.Branch.get(repo_new.branches[0]).data

            repo_new.refresh()
            assert len(repo_new.branches) == num_branchs

    finally:
        w_new.delete()


def run_tests():
    test_workspace()
    test_project()
    test_repository()
    test_relationships()
