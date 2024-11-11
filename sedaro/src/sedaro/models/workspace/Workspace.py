from typing import TYPE_CHECKING

from ..BaseModel import BaseModel

if TYPE_CHECKING:
    from ..project.Project import Project


class Workspace(BaseModel):
    pass

    @property
    def projects(self) -> 'list[Project]':
        from ..project.Project import Project
        return self._get_rel('projects', Project)
