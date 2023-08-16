from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ...settings import SCENARIO_TEMPLATE
from ..blocks import BlockType
from ..branch import Branch

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient


class ScenarioBranch(Branch):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) != SCENARIO_TEMPLATE:
            raise TypeError(
                f'Branch must be of type "{SCENARIO_TEMPLATE}" not "{type_}"')

    @property
    def simulation(self):
        """A `Simulation` instance to interact with the simulation connected to this scenario branch.

        Returns:
            Simulation: a `Simulation`
        """
        from .sim_client import Simulation
        return Simulation(self._sedaro, self)

    @property
    def study(self):
        """A `Sttudy` instance to interact with a study connected to this scenario branch.

        Returns:
            Study: a `Study`
        """
        from .study_client import Study
        return Study(self._sedaro, self)

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # SCENARIO
    Agent: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
    AgentGroup: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
    ClockConfig: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
    Orbit: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
    PerRoundExternalState: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
    SpontaneousExternalState: BlockType
    """A Sedaro `Block` class on a `Scenario` branch"""
