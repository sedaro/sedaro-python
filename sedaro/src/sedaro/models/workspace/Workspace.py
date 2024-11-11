from typing import TYPE_CHECKING

from ..BaseModel import BaseModel

if TYPE_CHECKING:
    from ..project.Project import Project
    from ..repository.Repository import Repository


class Workspace(BaseModel):
    pass

    @property
    def projects(self) -> 'list[Project]':
        from ..project.Project import Project
        return self._get_rel('projects', Project)

    @property
    def repositories(self) -> 'list[Repository]':
        from ..repository.Repository import Repository
        return self._get_rel('repositories', Repository)
