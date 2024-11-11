from typing import TYPE_CHECKING

from ..BaseModel import BaseModel

if TYPE_CHECKING:
    from ..workspace.Workspace import Workspace


class Repository(BaseModel):
    pass

    @property
    def workspace(self) -> 'Workspace':
        '''Get the workspace of the repository.'''
        from ..workspace.Workspace import Workspace
        return self._get_rel('workspace', Workspace)
