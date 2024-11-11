from typing import TYPE_CHECKING, ClassVar

from ..BaseModel import BaseModel
from ..BaseModelManager import BaseModelManager

if TYPE_CHECKING:
    from ..workspace.main import Workspace


class Repository(BaseModel):
    pass

    @property
    def workspace(self) -> 'Workspace':
        '''Get the workspace of the repository.'''
        from ..workspace.main import Workspace
        return self._get_rel('workspace', Workspace)


class RepositoryManager(BaseModelManager[Repository]):

    _BASE_PATH: 'ClassVar[str]' = '/models/repositories'
    _MODEL = Repository
