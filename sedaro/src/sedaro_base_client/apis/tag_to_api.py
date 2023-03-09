import typing_extensions

from sedaro_base_client.apis.tags import TagValues
from sedaro_base_client.apis.tags.branches_api import BranchesApi
from sedaro_base_client.apis.tags.data_api import DataApi
from sedaro_base_client.apis.tags.agent_api import AgentApi
from sedaro_base_client.apis.tags.angular_velocity_sensor_api import AngularVelocitySensorApi
from sedaro_base_client.apis.tags.antenna_api import AntennaApi
from sedaro_base_client.apis.tags.averaging_algorithm_api import AveragingAlgorithmApi
from sedaro_base_client.apis.tags.battery_api import BatteryApi
from sedaro_base_client.apis.tags.battery_cell_api import BatteryCellApi
from sedaro_base_client.apis.tags.battery_pack_api import BatteryPackApi
from sedaro_base_client.apis.tags.body_frame_vector_api import BodyFrameVectorApi
from sedaro_base_client.apis.tags.bus_regulator_api import BusRegulatorApi
from sedaro_base_client.apis.tags.celestial_target_api import CelestialTargetApi
from sedaro_base_client.apis.tags.celestial_vector_api import CelestialVectorApi
from sedaro_base_client.apis.tags.circular_field_of_view_api import CircularFieldOfViewApi
from sedaro_base_client.apis.tags.clock_config_api import ClockConfigApi
from sedaro_base_client.apis.tags.component_api import ComponentApi
from sedaro_base_client.apis.tags.condition_api import ConditionApi
from sedaro_base_client.apis.tags.constant_load_api import ConstantLoadApi
from sedaro_base_client.apis.tags.cooler_api import CoolerApi
from sedaro_base_client.apis.tags.cooperative_transmit_interface_api import CooperativeTransmitInterfaceApi
from sedaro_base_client.apis.tags.data_bus_api import DataBusApi
from sedaro_base_client.apis.tags.data_mode_api import DataModeApi
from sedaro_base_client.apis.tags.data_storage_api import DataStorageApi
from sedaro_base_client.apis.tags.data_type_api import DataTypeApi
from sedaro_base_client.apis.tags.direction_sensor_api import DirectionSensorApi
from sedaro_base_client.apis.tags.ekf_algorithm_api import EKFAlgorithmApi
from sedaro_base_client.apis.tags.fov_constraint_api import FOVConstraintApi
from sedaro_base_client.apis.tags.fuel_reservoir_api import FuelReservoirApi
from sedaro_base_client.apis.tags.gps_algorithm_api import GPSAlgorithmApi
from sedaro_base_client.apis.tags.ground_target_api import GroundTargetApi
from sedaro_base_client.apis.tags.group_condition_api import GroupConditionApi
from sedaro_base_client.apis.tags.heater_api import HeaterApi
from sedaro_base_client.apis.tags.internal_data_interface_api import InternalDataInterfaceApi
from sedaro_base_client.apis.tags.jobs_api import JobsApi
from sedaro_base_client.apis.tags.laser_comm_module_api import LaserCommModuleApi
from sedaro_base_client.apis.tags.load_state_api import LoadStateApi
from sedaro_base_client.apis.tags.local_vector_api import LocalVectorApi
from sedaro_base_client.apis.tags.lock_pointing_mode_api import LockPointingModeApi
from sedaro_base_client.apis.tags.mekf_algorithm_api import MEKFAlgorithmApi
from sedaro_base_client.apis.tags.magnetorquer_api import MagnetorquerApi
from sedaro_base_client.apis.tags.max_align_pointing_mode_api import MaxAlignPointingModeApi
from sedaro_base_client.apis.tags.modem_api import ModemApi
from sedaro_base_client.apis.tags.operational_mode_api import OperationalModeApi
from sedaro_base_client.apis.tags.optical_attitude_sensor_api import OpticalAttitudeSensorApi
from sedaro_base_client.apis.tags.orbit_api import OrbitApi
from sedaro_base_client.apis.tags.pid_algorithm_api import PIDAlgorithmApi
from sedaro_base_client.apis.tags.passive_pointing_mode_api import PassivePointingModeApi
from sedaro_base_client.apis.tags.passive_transmit_interface_api import PassiveTransmitInterfaceApi
from sedaro_base_client.apis.tags.position_sensor_api import PositionSensorApi
from sedaro_base_client.apis.tags.power_processor_api import PowerProcessorApi
from sedaro_base_client.apis.tags.reaction_wheel_api import ReactionWheelApi
from sedaro_base_client.apis.tags.receive_interface_api import ReceiveInterfaceApi
from sedaro_base_client.apis.tags.rectangular_field_of_view_api import RectangularFieldOfViewApi
from sedaro_base_client.apis.tags.satellite_api import SatelliteApi
from sedaro_base_client.apis.tags.sliding_mode_algorithm_api import SlidingModeAlgorithmApi
from sedaro_base_client.apis.tags.solar_array_api import SolarArrayApi
from sedaro_base_client.apis.tags.solar_cell_api import SolarCellApi
from sedaro_base_client.apis.tags.solar_panel_api import SolarPanelApi
from sedaro_base_client.apis.tags.space_target_api import SpaceTargetApi
from sedaro_base_client.apis.tags.spherical_fuel_tank_api import SphericalFuelTankApi
from sedaro_base_client.apis.tags.spherocylinder_fuel_tank_api import SpherocylinderFuelTankApi
from sedaro_base_client.apis.tags.static_thrust_control_algorithm_api import StaticThrustControlAlgorithmApi
from sedaro_base_client.apis.tags.subsystem_api import SubsystemApi
from sedaro_base_client.apis.tags.surface_api import SurfaceApi
from sedaro_base_client.apis.tags.surface_material_api import SurfaceMaterialApi
from sedaro_base_client.apis.tags.target_group_api import TargetGroupApi
from sedaro_base_client.apis.tags.target_group_vector_api import TargetGroupVectorApi
from sedaro_base_client.apis.tags.target_vector_api import TargetVectorApi
from sedaro_base_client.apis.tags.temp_controller_state_api import TempControllerStateApi
from sedaro_base_client.apis.tags.thermal_interface_api import ThermalInterfaceApi
from sedaro_base_client.apis.tags.thermal_interface_material_api import ThermalInterfaceMaterialApi
from sedaro_base_client.apis.tags.thruster_api import ThrusterApi
from sedaro_base_client.apis.tags.triad_algorithm_api import TriadAlgorithmApi
from sedaro_base_client.apis.tags.vector_sensor_api import VectorSensorApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.AGENT: AgentApi,
        TagValues.ANGULAR_VELOCITY_SENSOR: AngularVelocitySensorApi,
        TagValues.ANTENNA: AntennaApi,
        TagValues.AVERAGING_ALGORITHM: AveragingAlgorithmApi,
        TagValues.BATTERY: BatteryApi,
        TagValues.BATTERY_CELL: BatteryCellApi,
        TagValues.BATTERY_PACK: BatteryPackApi,
        TagValues.BODY_FRAME_VECTOR: BodyFrameVectorApi,
        TagValues.BUS_REGULATOR: BusRegulatorApi,
        TagValues.CELESTIAL_TARGET: CelestialTargetApi,
        TagValues.CELESTIAL_VECTOR: CelestialVectorApi,
        TagValues.CIRCULAR_FIELD_OF_VIEW: CircularFieldOfViewApi,
        TagValues.CLOCK_CONFIG: ClockConfigApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.CONDITION: ConditionApi,
        TagValues.CONSTANT_LOAD: ConstantLoadApi,
        TagValues.COOLER: CoolerApi,
        TagValues.COOPERATIVE_TRANSMIT_INTERFACE: CooperativeTransmitInterfaceApi,
        TagValues.DATA_BUS: DataBusApi,
        TagValues.DATA_MODE: DataModeApi,
        TagValues.DATA_STORAGE: DataStorageApi,
        TagValues.DATA_TYPE: DataTypeApi,
        TagValues.DIRECTION_SENSOR: DirectionSensorApi,
        TagValues.EKF_ALGORITHM: EKFAlgorithmApi,
        TagValues.FOV_CONSTRAINT: FOVConstraintApi,
        TagValues.FUEL_RESERVOIR: FuelReservoirApi,
        TagValues.GPS_ALGORITHM: GPSAlgorithmApi,
        TagValues.GROUND_TARGET: GroundTargetApi,
        TagValues.GROUP_CONDITION: GroupConditionApi,
        TagValues.HEATER: HeaterApi,
        TagValues.INTERNAL_DATA_INTERFACE: InternalDataInterfaceApi,
        TagValues.JOBS: JobsApi,
        TagValues.LASER_COMM_MODULE: LaserCommModuleApi,
        TagValues.LOAD_STATE: LoadStateApi,
        TagValues.LOCAL_VECTOR: LocalVectorApi,
        TagValues.LOCK_POINTING_MODE: LockPointingModeApi,
        TagValues.MEKF_ALGORITHM: MEKFAlgorithmApi,
        TagValues.MAGNETORQUER: MagnetorquerApi,
        TagValues.MAX_ALIGN_POINTING_MODE: MaxAlignPointingModeApi,
        TagValues.MODEM: ModemApi,
        TagValues.OPERATIONAL_MODE: OperationalModeApi,
        TagValues.OPTICAL_ATTITUDE_SENSOR: OpticalAttitudeSensorApi,
        TagValues.ORBIT: OrbitApi,
        TagValues.PID_ALGORITHM: PIDAlgorithmApi,
        TagValues.PASSIVE_POINTING_MODE: PassivePointingModeApi,
        TagValues.PASSIVE_TRANSMIT_INTERFACE: PassiveTransmitInterfaceApi,
        TagValues.POSITION_SENSOR: PositionSensorApi,
        TagValues.POWER_PROCESSOR: PowerProcessorApi,
        TagValues.REACTION_WHEEL: ReactionWheelApi,
        TagValues.RECEIVE_INTERFACE: ReceiveInterfaceApi,
        TagValues.RECTANGULAR_FIELD_OF_VIEW: RectangularFieldOfViewApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SLIDING_MODE_ALGORITHM: SlidingModeAlgorithmApi,
        TagValues.SOLAR_ARRAY: SolarArrayApi,
        TagValues.SOLAR_CELL: SolarCellApi,
        TagValues.SOLAR_PANEL: SolarPanelApi,
        TagValues.SPACE_TARGET: SpaceTargetApi,
        TagValues.SPHERICAL_FUEL_TANK: SphericalFuelTankApi,
        TagValues.SPHEROCYLINDER_FUEL_TANK: SpherocylinderFuelTankApi,
        TagValues.STATIC_THRUST_CONTROL_ALGORITHM: StaticThrustControlAlgorithmApi,
        TagValues.SUBSYSTEM: SubsystemApi,
        TagValues.SURFACE: SurfaceApi,
        TagValues.SURFACE_MATERIAL: SurfaceMaterialApi,
        TagValues.TARGET_GROUP: TargetGroupApi,
        TagValues.TARGET_GROUP_VECTOR: TargetGroupVectorApi,
        TagValues.TARGET_VECTOR: TargetVectorApi,
        TagValues.TEMP_CONTROLLER_STATE: TempControllerStateApi,
        TagValues.THERMAL_INTERFACE: ThermalInterfaceApi,
        TagValues.THERMAL_INTERFACE_MATERIAL: ThermalInterfaceMaterialApi,
        TagValues.THRUSTER: ThrusterApi,
        TagValues.TRIAD_ALGORITHM: TriadAlgorithmApi,
        TagValues.VECTOR_SENSOR: VectorSensorApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.AGENT: AgentApi,
        TagValues.ANGULAR_VELOCITY_SENSOR: AngularVelocitySensorApi,
        TagValues.ANTENNA: AntennaApi,
        TagValues.AVERAGING_ALGORITHM: AveragingAlgorithmApi,
        TagValues.BATTERY: BatteryApi,
        TagValues.BATTERY_CELL: BatteryCellApi,
        TagValues.BATTERY_PACK: BatteryPackApi,
        TagValues.BODY_FRAME_VECTOR: BodyFrameVectorApi,
        TagValues.BUS_REGULATOR: BusRegulatorApi,
        TagValues.CELESTIAL_TARGET: CelestialTargetApi,
        TagValues.CELESTIAL_VECTOR: CelestialVectorApi,
        TagValues.CIRCULAR_FIELD_OF_VIEW: CircularFieldOfViewApi,
        TagValues.CLOCK_CONFIG: ClockConfigApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.CONDITION: ConditionApi,
        TagValues.CONSTANT_LOAD: ConstantLoadApi,
        TagValues.COOLER: CoolerApi,
        TagValues.COOPERATIVE_TRANSMIT_INTERFACE: CooperativeTransmitInterfaceApi,
        TagValues.DATA_BUS: DataBusApi,
        TagValues.DATA_MODE: DataModeApi,
        TagValues.DATA_STORAGE: DataStorageApi,
        TagValues.DATA_TYPE: DataTypeApi,
        TagValues.DIRECTION_SENSOR: DirectionSensorApi,
        TagValues.EKF_ALGORITHM: EKFAlgorithmApi,
        TagValues.FOV_CONSTRAINT: FOVConstraintApi,
        TagValues.FUEL_RESERVOIR: FuelReservoirApi,
        TagValues.GPS_ALGORITHM: GPSAlgorithmApi,
        TagValues.GROUND_TARGET: GroundTargetApi,
        TagValues.GROUP_CONDITION: GroupConditionApi,
        TagValues.HEATER: HeaterApi,
        TagValues.INTERNAL_DATA_INTERFACE: InternalDataInterfaceApi,
        TagValues.JOBS: JobsApi,
        TagValues.LASER_COMM_MODULE: LaserCommModuleApi,
        TagValues.LOAD_STATE: LoadStateApi,
        TagValues.LOCAL_VECTOR: LocalVectorApi,
        TagValues.LOCK_POINTING_MODE: LockPointingModeApi,
        TagValues.MEKF_ALGORITHM: MEKFAlgorithmApi,
        TagValues.MAGNETORQUER: MagnetorquerApi,
        TagValues.MAX_ALIGN_POINTING_MODE: MaxAlignPointingModeApi,
        TagValues.MODEM: ModemApi,
        TagValues.OPERATIONAL_MODE: OperationalModeApi,
        TagValues.OPTICAL_ATTITUDE_SENSOR: OpticalAttitudeSensorApi,
        TagValues.ORBIT: OrbitApi,
        TagValues.PID_ALGORITHM: PIDAlgorithmApi,
        TagValues.PASSIVE_POINTING_MODE: PassivePointingModeApi,
        TagValues.PASSIVE_TRANSMIT_INTERFACE: PassiveTransmitInterfaceApi,
        TagValues.POSITION_SENSOR: PositionSensorApi,
        TagValues.POWER_PROCESSOR: PowerProcessorApi,
        TagValues.REACTION_WHEEL: ReactionWheelApi,
        TagValues.RECEIVE_INTERFACE: ReceiveInterfaceApi,
        TagValues.RECTANGULAR_FIELD_OF_VIEW: RectangularFieldOfViewApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SLIDING_MODE_ALGORITHM: SlidingModeAlgorithmApi,
        TagValues.SOLAR_ARRAY: SolarArrayApi,
        TagValues.SOLAR_CELL: SolarCellApi,
        TagValues.SOLAR_PANEL: SolarPanelApi,
        TagValues.SPACE_TARGET: SpaceTargetApi,
        TagValues.SPHERICAL_FUEL_TANK: SphericalFuelTankApi,
        TagValues.SPHEROCYLINDER_FUEL_TANK: SpherocylinderFuelTankApi,
        TagValues.STATIC_THRUST_CONTROL_ALGORITHM: StaticThrustControlAlgorithmApi,
        TagValues.SUBSYSTEM: SubsystemApi,
        TagValues.SURFACE: SurfaceApi,
        TagValues.SURFACE_MATERIAL: SurfaceMaterialApi,
        TagValues.TARGET_GROUP: TargetGroupApi,
        TagValues.TARGET_GROUP_VECTOR: TargetGroupVectorApi,
        TagValues.TARGET_VECTOR: TargetVectorApi,
        TagValues.TEMP_CONTROLLER_STATE: TempControllerStateApi,
        TagValues.THERMAL_INTERFACE: ThermalInterfaceApi,
        TagValues.THERMAL_INTERFACE_MATERIAL: ThermalInterfaceMaterialApi,
        TagValues.THRUSTER: ThrusterApi,
        TagValues.TRIAD_ALGORITHM: TriadAlgorithmApi,
        TagValues.VECTOR_SENSOR: VectorSensorApi,
    }
)
