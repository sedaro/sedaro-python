from typing import TYPE_CHECKING

from ..BaseModel import BaseModel

if TYPE_CHECKING:
    from ..workspace.Workspace import Workspace


class Project(BaseModel):
    pass

    def delete(self):
        self._delete(query_params={'delete': 'true'})

    @property
    def workspace(self) -> 'Workspace':
        '''Get the workspace of the project.'''
        from ..workspace.Workspace import Workspace
        return self._get_rel('workspace', Workspace)
