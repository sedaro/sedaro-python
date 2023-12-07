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
        """A `Study` instance to interact with a study connected to this scenario branch.

        Returns:
            Study: a `Study`
        """
        from .study_client import Study
        return Study(self._sedaro, self)

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # next line used to know where to start auto edit
    # $AUTO_EDIT_START$

    Agent: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    AgentGroup: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    ClockConfig: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    Menu: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    MenuItem: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    Orbit: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PerRoundExternalState: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    SpontaneousExternalState: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    WaypointPathWithDuration: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    WaypointPathWithSpeed: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    WaypointPathWithTimestamps: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    WidgetSpec: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
