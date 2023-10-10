from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ..settings import VEHICLE_TEMPLATES
from .blocks import BlockType
from .branch import Branch

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class AgentTemplateBranch(Branch):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) not in VEHICLE_TEMPLATES:
            raise TypeError(f'Branch must be of type "{VEHICLE_TEMPLATES}" not "{type_}"')

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # next line used to know where to start auto edit
    # $AUTO_EDIT_START$

    AngularVelocitySensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Antenna: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    AreaTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    AttitudeDynamics: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    AveragingAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Battery: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryCell: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryPack: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyFrameVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BusRegulator: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CircularFieldOfView: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Component: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ComponentToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CompoundCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Cooler: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CooperativeTransmitInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataBus: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataStorage: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataType: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DirectionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    EkfAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ElapsedTimeCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FixedSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FuelReservoir: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FullyRegDetPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GenericAdAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GenericOdAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GpsAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GroundTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Heater: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    IdealOrbitalAttitudeDynamics: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    InternalDataInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LaserCommModule: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LoadState: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LocalVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LockPointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Magnetorquer: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MaxAlignPointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MekfAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Modem: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OpticalAttitudeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Orbit: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OrbitalAttitudeDynamics: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassivePointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassiveTransmitInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PhotovoltaicPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PidAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PositionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PowerLoad: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    QuasiRegDetPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReactionWheel: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReceiveInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    RectangularFieldOfView: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ResistanceLoad: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SameTargetMultiCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToSatelliteCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ScanFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvHybridPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvMpptPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SlidingModeAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarArray: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarCell: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarPanel: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpaceTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpacecraftOperationalMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SphericalFuelTank: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpherocylinderFuelTank: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    StaticFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    StaticThrustControlAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Subsystem: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SunTrackingSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SurfaceMaterial: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetAttitudeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroup: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToSatelliteCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetPositionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetRangeRateSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetRangeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TempControllerState: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalDesignLayout: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterfaceMaterial: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Thruster: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TimeCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TrackingFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TriadAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TwoConvMpptPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorTrackingSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
