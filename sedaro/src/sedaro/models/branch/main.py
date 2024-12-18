from typing import ClassVar

from ...branches import Branch
from ..BaseModelManager import BaseModelManager

# TODO: Need to:
# - update Branch model to inherit from BaseModel
# - update its relationships to return the respective instances
# - update its `update` method to be consistent with the other BaseModel classes
# - remove the `SedaroApiClient` `scenario` and `agent_template` methods and move
#   them onto BranchManager
# - add more git functions, such as `commit` and `merge`


class BranchManager(BaseModelManager[Branch]):
    _BASE_PATH: 'ClassVar[str]' = '/models/branches'
    # TODO: Branch currently does not inherit from BaseModel as expected. Everything still works correctly on
    # BranchManager, because it's instantiation is similar enough; however, it does not have the expected methods
    # see other TODO above
    _MODEL = Branch

    def create(self, from_: 'str', /, *, name: 'str', description: 'str' = ''):
        '''Create a new branch from the given branch id.'''
        return super()._create(_id_in_url=from_, name=name, description=description)
