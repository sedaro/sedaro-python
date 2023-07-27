# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from sedaro_base_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from sedaro_base_client.model.agent import Agent
from sedaro_base_client.model.agent_group import AgentGroup
from sedaro_base_client.model.angle_base299 import AngleBase299
from sedaro_base_client.model.angle_field_of_view31 import AngleFieldOfView31
from sedaro_base_client.model.angle_field_of_view36 import AngleFieldOfView36
from sedaro_base_client.model.angle_field_of_view37 import AngleFieldOfView37
from sedaro_base_client.model.angle_sensors20 import AngleSensors20
from sedaro_base_client.model.angle_sensors51 import AngleSensors51
from sedaro_base_client.model.angle_sensors56 import AngleSensors56
from sedaro_base_client.model.angular_velocity_base299 import AngularVelocityBase299
from sedaro_base_client.model.angular_velocity_sensor import AngularVelocitySensor
from sedaro_base_client.model.angular_velocity_sensors82 import AngularVelocitySensors82
from sedaro_base_client.model.antenna import Antenna
from sedaro_base_client.model.averaging_algorithm import AveragingAlgorithm
from sedaro_base_client.model.battery import Battery
from sedaro_base_client.model.battery_cell import BatteryCell
from sedaro_base_client.model.battery_pack import BatteryPack
from sedaro_base_client.model.body_frame_vector import BodyFrameVector
from sedaro_base_client.model.body_frame_vector_types import BodyFrameVectorTypes
from sedaro_base_client.model.body_in_fov_condition import BodyInFovCondition
from sedaro_base_client.model.branch_create import BranchCreate
from sedaro_base_client.model.branch_delete_res import BranchDeleteRes
from sedaro_base_client.model.branch_merge import BranchMerge
from sedaro_base_client.model.branch_merge_conflicts_res import BranchMergeConflictsRes
from sedaro_base_client.model.branch_res import BranchRes
from sedaro_base_client.model.branch_scenario_res import BranchScenarioRes
from sedaro_base_client.model.branch_update import BranchUpdate
from sedaro_base_client.model.branch_vehicle_res import BranchVehicleRes
from sedaro_base_client.model.branch_verify_password import BranchVerifyPassword
from sedaro_base_client.model.bus_regulator import BusRegulator
from sedaro_base_client.model.categories import Categories
from sedaro_base_client.model.celestial_pointing_directions import CelestialPointingDirections
from sedaro_base_client.model.celestial_target import CelestialTarget
from sedaro_base_client.model.celestial_vector import CelestialVector
from sedaro_base_client.model.circular_field_of_view import CircularFieldOfView
from sedaro_base_client.model.classical_orbital_elements import ClassicalOrbitalElements
from sedaro_base_client.model.clock_config import ClockConfig
from sedaro_base_client.model.component import Component
from sedaro_base_client.model.component_parameters import ComponentParameters
from sedaro_base_client.model.component_to_scalar_condition import ComponentToScalarCondition
from sedaro_base_client.model.compound_condition import CompoundCondition
from sedaro_base_client.model.compound_operators import CompoundOperators
from sedaro_base_client.model.condition_relationship import ConditionRelationship
from sedaro_base_client.model.configuration_types import ConfigurationTypes
from sedaro_base_client.model.conflicts_obj import ConflictsObj
from sedaro_base_client.model.constant_power_params import ConstantPowerParams
from sedaro_base_client.model.constant_resistance_params import ConstantResistanceParams
from sedaro_base_client.model.cooler import Cooler
from sedaro_base_client.model.cooperative_transmit_interface import CooperativeTransmitInterface
from sedaro_base_client.model.crud_res import CrudRes
from sedaro_base_client.model.data_bus import DataBus
from sedaro_base_client.model.data_interface import DataInterface
from sedaro_base_client.model.data_mode import DataMode
from sedaro_base_client.model.data_service_response import DataServiceResponse
from sedaro_base_client.model.data_set import DataSet
from sedaro_base_client.model.data_storage import DataStorage
from sedaro_base_client.model.data_type import DataType
from sedaro_base_client.model.deleted_entity import DeletedEntity
from sedaro_base_client.model.direction_sensor import DirectionSensor
from sedaro_base_client.model.distance_sensors70 import DistanceSensors70
from sedaro_base_client.model.duration_load70 import DurationLoad70
from sedaro_base_client.model.duration_operational_mode18 import DurationOperationalMode18
from sedaro_base_client.model.duration_operational_mode19 import DurationOperationalMode19
from sedaro_base_client.model.duration_operational_mode20 import DurationOperationalMode20
from sedaro_base_client.model.duration_operational_mode28 import DurationOperationalMode28
from sedaro_base_client.model.duration_operational_mode29 import DurationOperationalMode29
from sedaro_base_client.model.ekf_algorithm import EkfAlgorithm
from sedaro_base_client.model.eps_output_types import EpsOutputTypes
from sedaro_base_client.model.equatorial_circular_reference_orbit import EquatorialCircularReferenceOrbit
from sedaro_base_client.model.external_state_set_request import ExternalStateSetRequest
from sedaro_base_client.model.fixed_surface import FixedSurface
from sedaro_base_client.model.frame_vector_base299 import FrameVectorBase299
from sedaro_base_client.model.fuel_reservoir import FuelReservoir
from sedaro_base_client.model.fully_reg_det_power_processor import FullyRegDetPowerProcessor
from sedaro_base_client.model.fully_reg_det_topology_params import FullyRegDetTopologyParams
from sedaro_base_client.model.geostationary_reference_orbit import GeostationaryReferenceOrbit
from sedaro_base_client.model.geostationary_transfer_reference_orbit import GeostationaryTransferReferenceOrbit
from sedaro_base_client.model.gps_algorithm import GpsAlgorithm
from sedaro_base_client.model.ground_target import GroundTarget
from sedaro_base_client.model.group_rollers import GroupRollers
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.heater import Heater
from sedaro_base_client.model.initial_state_def_type import InitialStateDefType
from sedaro_base_client.model.input_types import InputTypes
from sedaro_base_client.model.internal_data_interface import InternalDataInterface
from sedaro_base_client.model.iss_reference_orbit import IssReferenceOrbit
from sedaro_base_client.model.laser_comm_module import LaserCommModule
from sedaro_base_client.model.load_state import LoadState
from sedaro_base_client.model.local_pointing_directions import LocalPointingDirections
from sedaro_base_client.model.local_vector import LocalVector
from sedaro_base_client.model.lock_pointing_mode import LockPointingMode
from sedaro_base_client.model.magnetorquer import Magnetorquer
from sedaro_base_client.model.max_align_pointing_mode import MaxAlignPointingMode
from sedaro_base_client.model.mekf_algorithm import MekfAlgorithm
from sedaro_base_client.model.message_res import MessageRes
from sedaro_base_client.model.modem import Modem
from sedaro_base_client.model.operational_mode import OperationalMode
from sedaro_base_client.model.optical_attitude_sensor import OpticalAttitudeSensor
from sedaro_base_client.model.orbit import Orbit
from sedaro_base_client.model.orbital_elements_data import OrbitalElementsData
from sedaro_base_client.model.passive_pointing_mode import PassivePointingMode
from sedaro_base_client.model.passive_transmit_interface import PassiveTransmitInterface
from sedaro_base_client.model.per_round_external_state import PerRoundExternalState
from sedaro_base_client.model.pid_algorithm import PidAlgorithm
from sedaro_base_client.model.polar_circular_reference_orbit import PolarCircularReferenceOrbit
from sedaro_base_client.model.polynomial_ephemeris_body import PolynomialEphemerisBody
from sedaro_base_client.model.position_base299 import PositionBase299
from sedaro_base_client.model.position_sensor import PositionSensor
from sedaro_base_client.model.power_load import PowerLoad
from sedaro_base_client.model.power_processor import PowerProcessor
from sedaro_base_client.model.quasi_reg_det_power_processor import QuasiRegDetPowerProcessor
from sedaro_base_client.model.quasi_reg_det_topology_params import QuasiRegDetTopologyParams
from sedaro_base_client.model.quaternion_base299 import QuaternionBase299
from sedaro_base_client.model.reaction_wheel import ReactionWheel
from sedaro_base_client.model.receive_interface import ReceiveInterface
from sedaro_base_client.model.rectangular_field_of_view import RectangularFieldOfView
from sedaro_base_client.model.resistance_load import ResistanceLoad
from sedaro_base_client.model.same_target_multi_condition import SameTargetMultiCondition
from sedaro_base_client.model.satellite import Satellite
from sedaro_base_client.model.satellite_parameters import SatelliteParameters
from sedaro_base_client.model.satellite_to_satellite_condition import SatelliteToSatelliteCondition
from sedaro_base_client.model.satellite_to_scalar_condition import SatelliteToScalarCondition
from sedaro_base_client.model.satellite_to_target_condition import SatelliteToTargetCondition
from sedaro_base_client.model.scenario_template_crud import ScenarioTemplateCrud
from sedaro_base_client.model.scenario_template_res import ScenarioTemplateRes
from sedaro_base_client.model.scenario_template_update import ScenarioTemplateUpdate
from sedaro_base_client.model.side_categories import SideCategories
from sedaro_base_client.model.simulation_job import SimulationJob
from sedaro_base_client.model.single_conv_hybrid_power_processor import SingleConvHybridPowerProcessor
from sedaro_base_client.model.single_conv_hybrid_topology_params import SingleConvHybridTopologyParams
from sedaro_base_client.model.single_conv_mppt_power_processor import SingleConvMpptPowerProcessor
from sedaro_base_client.model.single_conv_mppt_topology_params import SingleConvMpptTopologyParams
from sedaro_base_client.model.sliding_mode_algorithm import SlidingModeAlgorithm
from sedaro_base_client.model.solar_array import SolarArray
from sedaro_base_client.model.solar_cell import SolarCell
from sedaro_base_client.model.solar_panel import SolarPanel
from sedaro_base_client.model.space_target import SpaceTarget
from sedaro_base_client.model.spherical_angles import SphericalAngles
from sedaro_base_client.model.spherical_fuel_tank import SphericalFuelTank
from sedaro_base_client.model.spherocylinder_fuel_tank import SpherocylinderFuelTank
from sedaro_base_client.model.spontaneous_external_state import SpontaneousExternalState
from sedaro_base_client.model.state_vector import StateVector
from sedaro_base_client.model.static_thrust_control_algorithm import StaticThrustControlAlgorithm
from sedaro_base_client.model.statuses import Statuses
from sedaro_base_client.model.subsystem import Subsystem
from sedaro_base_client.model.sun_synchronous_circular_orbit import SunSynchronousCircularOrbit
from sedaro_base_client.model.sun_tracking_surface import SunTrackingSurface
from sedaro_base_client.model.surface_material import SurfaceMaterial
from sedaro_base_client.model.target_group import TargetGroup
from sedaro_base_client.model.target_group_in_fov_condition import TargetGroupInFovCondition
from sedaro_base_client.model.target_group_to_satellite_condition import TargetGroupToSatelliteCondition
from sedaro_base_client.model.target_group_to_scalar_condition import TargetGroupToScalarCondition
from sedaro_base_client.model.target_group_to_target_condition import TargetGroupToTargetCondition
from sedaro_base_client.model.target_group_vector import TargetGroupVector
from sedaro_base_client.model.target_in_fov_condition import TargetInFovCondition
from sedaro_base_client.model.target_parameters import TargetParameters
from sedaro_base_client.model.target_to_scalar_condition import TargetToScalarCondition
from sedaro_base_client.model.target_to_target_condition import TargetToTargetCondition
from sedaro_base_client.model.target_vector import TargetVector
from sedaro_base_client.model.temp_controller_state import TempControllerState
from sedaro_base_client.model.temperature_base299 import TemperatureBase299
from sedaro_base_client.model.template_crud_res import TemplateCrudRes
from sedaro_base_client.model.thermal_interface import ThermalInterface
from sedaro_base_client.model.thermal_interface_material import ThermalInterfaceMaterial
from sedaro_base_client.model.thruster import Thruster
from sedaro_base_client.model.time_condition import TimeCondition
from sedaro_base_client.model.tle import Tle
from sedaro_base_client.model.triad_algorithm import TriadAlgorithm
from sedaro_base_client.model.two_conv_mppt_power_processor import TwoConvMpptPowerProcessor
from sedaro_base_client.model.two_conv_mppt_topology_params import TwoConvMpptTopologyParams
from sedaro_base_client.model.types import Types
from sedaro_base_client.model.validation_error import ValidationError
from sedaro_base_client.model.vector import Vector
from sedaro_base_client.model.vector_in_fov_condition import VectorInFovCondition
from sedaro_base_client.model.vector_sensor import VectorSensor
from sedaro_base_client.model.vector_tracking_surface import VectorTrackingSurface
from sedaro_base_client.model.vehicle_template_crud import VehicleTemplateCrud
from sedaro_base_client.model.vehicle_template_res import VehicleTemplateRes
from sedaro_base_client.model.vehicle_template_update import VehicleTemplateUpdate
