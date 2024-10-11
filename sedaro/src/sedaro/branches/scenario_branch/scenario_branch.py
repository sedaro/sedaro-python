from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import SchemaFor200ResponseBodyApplicationJson

from ... import modsim as ms
from ...settings import SCENARIO
from ..blocks import BlockType
from ..branch import Branch

if TYPE_CHECKING:
    from ...sedaro_api_client import SedaroApiClient


class ScenarioBranch(Branch):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) != SCENARIO:
            raise TypeError(
                f'Branch must be of type "{SCENARIO}" not "{type_}"')

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

    def delete_all_external_state_blocks(self):
        """Delete all ExternalState blocks in the scenario branch."""
        if existing_externals := self.ExternalState.get_all_ids():
            self.crud(delete=existing_externals)

    def set_start_time_to_now(self, elapsed_time_seconds):
        """Set the start time of the scenario to the current time and the stop time to the current time plus the passed elapsed time in seconds."""
        start_time_mjd = ms.datetime_to_mjd(ms.datetime_now_utc())
        return self.clockConfig.update(
            startTime=start_time_mjd,
            stopTime=start_time_mjd+(elapsed_time_seconds/86400)
        )

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # next line used to know where to start auto edit
    # $AUTO_EDIT_START$

    AgentGroup: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    ClockConfig: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    Menu: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    MenuItem: BlockType
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
    PeripheralGroundArea: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    SpkEphemeris: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PeripheralSpacePoint: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PropagatedOrbitKinematics: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    EcefStationaryKinematics: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PeripheralGroundPoint: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    OverrideSet: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    StkEphemeris: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PeripheralAgent: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    PeripheralCelestialPoint: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    TemplatedAgent: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    AuxiliaryService: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
    DynamicWaypointPath: BlockType
    """A Sedaro `Block` class on a `ScenarioBranch`"""
