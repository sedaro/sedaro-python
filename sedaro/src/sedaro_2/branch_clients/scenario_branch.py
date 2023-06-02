from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ..block_class_client import BlockClassClient
from ..settings import SCENARIO
from .branch_client import BranchClient

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class ScenarioBranch(BranchClient):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, client: 'SedaroApiClient'):
        super().__init__(body, client)
        if (type_ := self.data['type']) != SCENARIO:
            raise TypeError(f'Branch must be of type {SCENARIO} not {type_}')

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # SCENARIO
    Agent: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    AgentGroup: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    ClockConfig: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    Orbit: BlockClassClient
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
