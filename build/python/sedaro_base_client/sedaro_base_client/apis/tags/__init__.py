# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sedaro_base_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BRANCHES = "Branches"
    DATA = "Data"
    AGENT_TEMPLATE_REFERENCE = "Agent Template Reference"
    ATTITUDE_CONTROL_ALGORITHM = "Attitude Control Algorithm"
    ATTITUDE_DETERMINATION_ALGORITHM = "Attitude Determination Algorithm"
    BATTERY = "Battery"
    BATTERY_CELL = "Battery Cell"
    BODY_FRAME_VECTOR = "Body Frame Vector"
    BUS_REGULATOR = "Bus Regulator"
    COMPONENT = "Component"
    CONDITION = "Condition"
    FIELD_OF_VIEW_CONSTRAINT = "Field of View Constraint"
    FIELD_OF_VIEW = "FieldOfView"
    JOBS = "Jobs"
    LOAD = "Load"
    LOAD_STATE = "Load State"
    OPERATIONAL_MODE = "Operational Mode"
    ORBIT = "Orbit"
    ORBIT_DETERMINATION_ALGORITHM = "Orbit Determination Algorithm"
    POINTING_MODE = "PointingMode"
    REFERENCE_VECTOR = "ReferenceVector"
    SATELLITE = "Satellite"
    SIMULATED_AGENT = "Simulated Agent"
    SIMULATION_CLOCK_CONFIGURATION = "Simulation Clock Configuration"
    SOLAR_ARRAY = "Solar Array"
    SOLAR_CELL = "Solar Cell"
    SUBSYSTEM = "Subsystem"
    SURFACE = "Surface"
    SURFACE_MATERIAL = "Surface Material"
    TARGET = "Target"
    TARGET_GROUP = "Target Group"
    TEMPERATURE_CONTROLLER = "Temperature Controller"
    TEMPERATURE_CONTROLLER_STATE = "Temperature Controller State"
    THERMAL_INTERFACE = "Thermal Interface"
    THERMAL_INTERFACE_MATERIAL = "Thermal Interface Material"
