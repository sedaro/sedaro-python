from typing import TYPE_CHECKING, ClassVar

from ..BaseModel import BaseModel
from ..BaseModelManager import BaseModelManager

if TYPE_CHECKING:
    from ..project import Project
    from ..workspace import Workspace


class Repository(BaseModel):
    pass

    @property
    def project(self) -> 'Project':
        '''Get the project of the repository.'''
        from ..project import Project
        return self._get_rel('project', Project)

    @property
    def workspace(self) -> 'Workspace':
        '''Get the workspace of the repository.'''
        from ..workspace import Workspace
        return self._get_rel('workspace', Workspace)


class RepositoryManager(BaseModelManager[Repository]):

    _BASE_PATH: 'ClassVar[str]' = '/models/repositories'
    _MODEL = Repository
