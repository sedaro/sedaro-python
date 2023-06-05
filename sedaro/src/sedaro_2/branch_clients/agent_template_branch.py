from typing import TYPE_CHECKING

from sedaro_base_client.paths.models_branches_branch_id.get import \
    SchemaFor200ResponseBodyApplicationJson

from ..block_class_client import BlockClassClient
from ..settings import VEHICLE_TEMPLATE
from .branch_client import BranchClient

if TYPE_CHECKING:
    from ..sedaro_api_client import SedaroApiClient


class AgentTemplateBranch(BranchClient):

    def __init__(self, body: SchemaFor200ResponseBodyApplicationJson, sedaro: 'SedaroApiClient'):
        super().__init__(body, sedaro)
        if (type_ := self.data['type']) != VEHICLE_TEMPLATE:
            raise TypeError(f'Branch must be of type {VEHICLE_TEMPLATE} not {type_}')

    # ==============================================================================================================
    # For intellisense
    # ==============================================================================================================

    # AGENT TEMPLATE
    AngularVelocitySensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Antenna: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    AveragingAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Battery: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryCell: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BatteryPack: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyFrameVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BodyInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    BusRegulator: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CelestialVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CircularFieldOfView: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Component: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ComponentToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CompoundCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Cooler: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    CooperativeTransmitInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataBus: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataStorage: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DataType: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    DirectionSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    EkfAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FixedSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FuelReservoir: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    FullyRegDetPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GpsAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    GroundTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Heater: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    InternalDataInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LaserCommModule: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LoadState: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LocalVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    LockPointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Magnetorquer: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MaxAlignPointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    MekfAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Modem: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OperationalMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    OpticalAttitudeSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Orbit: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassivePointingMode: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PassiveTransmitInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PidAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PositionSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PowerLoad: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    PowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    QuasiRegDetPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReactionWheel: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ReceiveInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    RectangularFieldOfView: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ResistanceLoad: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SameTargetMultiCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Satellite: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToSatelliteCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SatelliteToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvHybridPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SingleConvMpptPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SlidingModeAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarArray: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarCell: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SolarPanel: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpaceTarget: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SphericalFuelTank: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SpherocylinderFuelTank: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    StaticThrustControlAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Subsystem: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SunTrackingSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    SurfaceMaterial: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroup: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToSatelliteCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetGroupVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToScalarCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetToTargetCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TargetVector: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TempControllerState: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    ThermalInterfaceMaterial: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    Thruster: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TimeCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TriadAlgorithm: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    TwoConvMpptPowerProcessor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorInFovCondition: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorSensor: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
    VectorTrackingSurface: BlockClassClient
    """A Sedaro `Block` class on an `AgentTemplate` branch"""
