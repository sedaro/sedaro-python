from typing import ClassVar

from ...branches import Branch
from ..BaseModelManager import BaseModelManager

# TODO: Need to:
# - update Branch model to inherit from BaseModel
# - update its relationships to return the respective instances
# - update its `update` method to be consistent with the other BaseModel classes
# - can also update or remove the `SedaroApiClient` `scenario` and `agent_template` methods


class BranchManager(BaseModelManager[Branch]):
    _BASE_PATH: 'ClassVar[str]' = '/models/branches'
    _MODEL = Branch

    def create(self, from_: 'str', /, *, name: 'str', description: 'str' = ''):
        '''Create a new branch from the given branch id.'''
        return super()._create(_id_in_url=from_, name=name, description=description)
