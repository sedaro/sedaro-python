from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ..block_class_client import BlockClassClient
from ..settings import SCENARIO_TEMPLATE
from ..sim_client import SimClient
from .branch_client import BranchClient

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class ScenarioBranch(BranchClient):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) != SCENARIO_TEMPLATE:
            raise TypeError(f'Branch must be of type {SCENARIO_TEMPLATE} not {type_}')

    def simulation(self) -> SimClient:
        """Get a `SimClient` to interact with the simulation connected to this Sedaro scenario `Branch`.

        Returns:
            SimClient: a `SimClient`
        """
        # update methods inside sim client to call the context manager inside rather than expecting context manager
        # to already be instantiated
        return SimClient(self._sedaro, self.id)

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
