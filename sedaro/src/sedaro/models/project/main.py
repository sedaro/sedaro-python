from typing import TYPE_CHECKING, ClassVar

from ..BaseModel import BaseModel
from ..BaseModelManager import BaseModelManager

if TYPE_CHECKING:
    from ..workspace.main import Workspace


class Project(BaseModel):
    pass

    def delete(self):
        self._delete(query_params={'delete': 'true'})

    @property
    def workspace(self) -> 'Workspace':
        '''Get the workspace of the project.'''
        from ..workspace.main import Workspace
        return self._get_rel('workspace', Workspace)


class ProjectManager(BaseModelManager[Project]):

    _BASE_PATH: 'ClassVar[str]' = '/projects'
    _MODEL = Project
