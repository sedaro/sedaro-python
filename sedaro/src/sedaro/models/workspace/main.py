from typing import TYPE_CHECKING, ClassVar

from ..BaseModel import BaseModel
from ..BaseModelManager import BaseModelManager

if TYPE_CHECKING:
    from ..project import Project
    from ..repository import Repository


class Workspace(BaseModel):

    @property
    def projects(self) -> 'list[Project]':
        '''Get the projects of the workspace.'''
        from ..project import Project
        return self._get_rel('projects', Project)

    @property
    def repositories(self) -> 'list[Repository]':
        '''Get the repositories of the workspace.'''
        from ..repository import Repository
        return self._get_rel('repositories', Repository)


class WorkspaceManager(BaseModelManager[Workspace]):

    _BASE_PATH: 'ClassVar[str]' = '/workspaces'
    _MODEL = Workspace
