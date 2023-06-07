from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ...settings import SCENARIO_TEMPLATE
from ..blocks import BlockType
from ..branch import Branch
from .sim_client import Simulation

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient


class ScenarioBranch(Branch):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) != SCENARIO_TEMPLATE:
            raise TypeError(f'Branch must be of type {SCENARIO_TEMPLATE} not {type_}')

    @property
    def simulation(self) -> 'Simulation':
        """A `Simulation` instance to interact with the simulation connected to this Sedaro scenario `Branch`.

        Returns:
            Simulation: a `Simulation`
        """
        return Simulation(self._sedaro, self.id)

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # SCENARIO
    Agent: BlockType
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    AgentGroup: BlockType
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    ClockConfig: BlockType
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
    Orbit: BlockType
    """A Sedaro `Block` class on a `ScenarioTemplate` branch"""
