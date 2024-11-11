from typing import ClassVar

from ...branches import Branch
from ..BaseModelManager import BaseModelManager


class BranchManager(BaseModelManager[Branch]):
    _BASE_PATH: 'ClassVar[str]' = '/models/branches'
    _MODEL = Branch

    def create(self, from_: 'str', /, *, name: 'str', description: 'str' = ''):
        '''Create a new branch from the given branch id.'''
        return super()._create(_id_in_url=from_, name=name, description=description)
