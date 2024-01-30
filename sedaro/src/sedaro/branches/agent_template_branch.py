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
            raise TypeError(
                f'Branch must be of type "{VEHICLE_TEMPLATES}" not "{type_}"')

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # next line used to know where to start auto edit
    # $AUTO_EDIT_START$

    AngularVelocitySensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Antenna: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    AreaTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    AveragingAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Battery: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    BatteryCell: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    BatteryPack: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    BodyFrameVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    BodyInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    BusRegulator: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CelestialTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CelestialVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CircularFieldOfView: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Component: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ComponentToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CompoundCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Cooler: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CooperativeTransmitInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DataBus: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DataInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DataMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DataStorage: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DataType: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DirectionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    EkfAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ElapsedTimeCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FixedSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FuelReservoir: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FullyRegDetPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    GenericAdAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    GenericOdAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    GpsAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    GroundTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Heater: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    IdealOrbitalAttitudeDynamics: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    InternalDataInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    LaserCommModule: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    LoadState: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    LocalVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    MagneticHysteresisRod: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Magnetorquer: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    MaxAlignPointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    MekfAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Modem: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    OpticalAttitudeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    OrbitalAttitudeDynamics: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PassivePointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PassiveTransmitInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PermanentDipoleMagnet: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PhotovoltaicPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PidAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PositionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PowerLoad: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    QuasiRegDetPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ReactionWheel: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ReceiveInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    RectangularFieldOfView: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ResistanceLoad: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SameTargetMultiCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SatelliteToSatelliteCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SatelliteToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SatelliteToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ScanFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SingleConvHybridPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SingleConvMpptPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SlidingModeAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SolarArray: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SolarCell: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SolarPanel: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SpaceTarget: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SphericalFuelTank: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SpherocylinderFuelTank: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    StaticFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    StaticThrustControlAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Subsystem: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SunTrackingSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SurfaceMaterial: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetAttitudeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroup: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroupInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroupToSatelliteCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroupToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroupToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetGroupVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetPositionSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetRangeRateSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetRangeSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetToTargetCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TargetVector: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TempControllerState: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ThermalDesignLayout: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ThermalInterface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ThermalInterfaceMaterial: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Thruster: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TimeCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TrackingFieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TriadAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TwoConvMpptPowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    VectorInFovCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    VectorSensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    VectorTrackingSurface: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    UnresponsiveThrusterFailureMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    UnresponsiveSensorFailureMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CombinationalLogic: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    TriadAttitudeInitializer: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    MagneticDetumblingAlgorithm: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    GeoAreaDateTimeGroup: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CloudFractionGroup: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    UnresponsiveReactionWheelFailureMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SensorFailureMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    CloudFractionGroupToScalarCondition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FieldOfViewArticulationMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PropagatedOrbitKinematics: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    SpkEphemeris: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DynamicallyLoadedComponent: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    LockSpinPointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FiniteStateMachine: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    RelativeSchedule: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    LogicalConfiguration: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FixedSchedule: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    ActivePointingMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    StkEphemeris: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    StateTransition: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Sensor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    PowerProcessor: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    FiniteDifferenceOrbitInitializer: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    UnresponsiveMagnetorquerFailureMode: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    DirectMeasurementAttitudeInitializer: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    Routine: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
    StaticAttitudeInitializer: BlockType
    """A Sedaro `Block` class on an `AgentTemplateBranch`"""
