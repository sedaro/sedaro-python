import typing_extensions

from sedaro_base_client.apis.tags import TagValues
from sedaro_base_client.apis.tags.branches_api import BranchesApi
from sedaro_base_client.apis.tags.data_api import DataApi
from sedaro_base_client.apis.tags.agent_template_reference_api import AgentTemplateReferenceApi
from sedaro_base_client.apis.tags.attitude_control_algorithm_api import AttitudeControlAlgorithmApi
from sedaro_base_client.apis.tags.attitude_determination_algorithm_api import AttitudeDeterminationAlgorithmApi
from sedaro_base_client.apis.tags.battery_api import BatteryApi
from sedaro_base_client.apis.tags.battery_cell_api import BatteryCellApi
from sedaro_base_client.apis.tags.body_frame_vector_api import BodyFrameVectorApi
from sedaro_base_client.apis.tags.bus_regulator_api import BusRegulatorApi
from sedaro_base_client.apis.tags.component_api import ComponentApi
from sedaro_base_client.apis.tags.condition_api import ConditionApi
from sedaro_base_client.apis.tags.field_of_view_constraint_api import FieldOfViewConstraintApi
from sedaro_base_client.apis.tags.field_of_view_api import FieldOfViewApi
from sedaro_base_client.apis.tags.jobs_api import JobsApi
from sedaro_base_client.apis.tags.load_api import LoadApi
from sedaro_base_client.apis.tags.load_state_api import LoadStateApi
from sedaro_base_client.apis.tags.operational_mode_api import OperationalModeApi
from sedaro_base_client.apis.tags.orbit_api import OrbitApi
from sedaro_base_client.apis.tags.orbit_determination_algorithm_api import OrbitDeterminationAlgorithmApi
from sedaro_base_client.apis.tags.pointing_mode_api import PointingModeApi
from sedaro_base_client.apis.tags.reference_vector_api import ReferenceVectorApi
from sedaro_base_client.apis.tags.satellite_api import SatelliteApi
from sedaro_base_client.apis.tags.simulated_agent_api import SimulatedAgentApi
from sedaro_base_client.apis.tags.simulation_clock_configuration_api import SimulationClockConfigurationApi
from sedaro_base_client.apis.tags.solar_array_api import SolarArrayApi
from sedaro_base_client.apis.tags.solar_cell_api import SolarCellApi
from sedaro_base_client.apis.tags.subsystem_api import SubsystemApi
from sedaro_base_client.apis.tags.surface_api import SurfaceApi
from sedaro_base_client.apis.tags.surface_material_api import SurfaceMaterialApi
from sedaro_base_client.apis.tags.target_api import TargetApi
from sedaro_base_client.apis.tags.target_group_api import TargetGroupApi
from sedaro_base_client.apis.tags.temperature_controller_api import TemperatureControllerApi
from sedaro_base_client.apis.tags.temperature_controller_state_api import TemperatureControllerStateApi
from sedaro_base_client.apis.tags.thermal_interface_api import ThermalInterfaceApi
from sedaro_base_client.apis.tags.thermal_interface_material_api import ThermalInterfaceMaterialApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.AGENT_TEMPLATE_REFERENCE: AgentTemplateReferenceApi,
        TagValues.ATTITUDE_CONTROL_ALGORITHM: AttitudeControlAlgorithmApi,
        TagValues.ATTITUDE_DETERMINATION_ALGORITHM: AttitudeDeterminationAlgorithmApi,
        TagValues.BATTERY: BatteryApi,
        TagValues.BATTERY_CELL: BatteryCellApi,
        TagValues.BODY_FRAME_VECTOR: BodyFrameVectorApi,
        TagValues.BUS_REGULATOR: BusRegulatorApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.CONDITION: ConditionApi,
        TagValues.FIELD_OF_VIEW_CONSTRAINT: FieldOfViewConstraintApi,
        TagValues.FIELD_OF_VIEW: FieldOfViewApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOAD: LoadApi,
        TagValues.LOAD_STATE: LoadStateApi,
        TagValues.OPERATIONAL_MODE: OperationalModeApi,
        TagValues.ORBIT: OrbitApi,
        TagValues.ORBIT_DETERMINATION_ALGORITHM: OrbitDeterminationAlgorithmApi,
        TagValues.POINTING_MODE: PointingModeApi,
        TagValues.REFERENCE_VECTOR: ReferenceVectorApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SIMULATED_AGENT: SimulatedAgentApi,
        TagValues.SIMULATION_CLOCK_CONFIGURATION: SimulationClockConfigurationApi,
        TagValues.SOLAR_ARRAY: SolarArrayApi,
        TagValues.SOLAR_CELL: SolarCellApi,
        TagValues.SUBSYSTEM: SubsystemApi,
        TagValues.SURFACE: SurfaceApi,
        TagValues.SURFACE_MATERIAL: SurfaceMaterialApi,
        TagValues.TARGET: TargetApi,
        TagValues.TARGET_GROUP: TargetGroupApi,
        TagValues.TEMPERATURE_CONTROLLER: TemperatureControllerApi,
        TagValues.TEMPERATURE_CONTROLLER_STATE: TemperatureControllerStateApi,
        TagValues.THERMAL_INTERFACE: ThermalInterfaceApi,
        TagValues.THERMAL_INTERFACE_MATERIAL: ThermalInterfaceMaterialApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.AGENT_TEMPLATE_REFERENCE: AgentTemplateReferenceApi,
        TagValues.ATTITUDE_CONTROL_ALGORITHM: AttitudeControlAlgorithmApi,
        TagValues.ATTITUDE_DETERMINATION_ALGORITHM: AttitudeDeterminationAlgorithmApi,
        TagValues.BATTERY: BatteryApi,
        TagValues.BATTERY_CELL: BatteryCellApi,
        TagValues.BODY_FRAME_VECTOR: BodyFrameVectorApi,
        TagValues.BUS_REGULATOR: BusRegulatorApi,
        TagValues.COMPONENT: ComponentApi,
        TagValues.CONDITION: ConditionApi,
        TagValues.FIELD_OF_VIEW_CONSTRAINT: FieldOfViewConstraintApi,
        TagValues.FIELD_OF_VIEW: FieldOfViewApi,
        TagValues.JOBS: JobsApi,
        TagValues.LOAD: LoadApi,
        TagValues.LOAD_STATE: LoadStateApi,
        TagValues.OPERATIONAL_MODE: OperationalModeApi,
        TagValues.ORBIT: OrbitApi,
        TagValues.ORBIT_DETERMINATION_ALGORITHM: OrbitDeterminationAlgorithmApi,
        TagValues.POINTING_MODE: PointingModeApi,
        TagValues.REFERENCE_VECTOR: ReferenceVectorApi,
        TagValues.SATELLITE: SatelliteApi,
        TagValues.SIMULATED_AGENT: SimulatedAgentApi,
        TagValues.SIMULATION_CLOCK_CONFIGURATION: SimulationClockConfigurationApi,
        TagValues.SOLAR_ARRAY: SolarArrayApi,
        TagValues.SOLAR_CELL: SolarCellApi,
        TagValues.SUBSYSTEM: SubsystemApi,
        TagValues.SURFACE: SurfaceApi,
        TagValues.SURFACE_MATERIAL: SurfaceMaterialApi,
        TagValues.TARGET: TargetApi,
        TagValues.TARGET_GROUP: TargetGroupApi,
        TagValues.TEMPERATURE_CONTROLLER: TemperatureControllerApi,
        TagValues.TEMPERATURE_CONTROLLER_STATE: TemperatureControllerStateApi,
        TagValues.THERMAL_INTERFACE: ThermalInterfaceApi,
        TagValues.THERMAL_INTERFACE_MATERIAL: ThermalInterfaceMaterialApi,
    }
)
