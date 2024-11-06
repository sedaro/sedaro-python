from ..BaseModel import BaseModel


class Project(BaseModel):
    pass

    def delete(self):
        self._delete({'delete': 'true'})
