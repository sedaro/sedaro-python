PACKAGE_NAME = 'sedaro'
BASE_PACKAGE_NAME = f'{PACKAGE_NAME}_base_client'

COMMON_API_KWARGS = {
    'skip_deserialization': True
}
"""To be spread in autogenerated HTTP request methods. Make sure to use in conjunction with `body_from_res`."""


# template
CRUD = 'crud'
'''One of the keys in returned response from a template crud PATCH request'''
BLOCKS = 'blocks'
INDEX = 'index'
RELATIONSHIPS = '_relationships'
VEHICLE_TEMPLATES = {'Spacecraft', 'TerrestrialVehicle'}
SCENARIO_TEMPLATE = 'Scenario'

ROOT = 'root'

# Relationships and Blocks
MANY_SIDE = 'ManySide'
DATA_SIDE = 'DataSide'
ONE_SIDE = 'OneSide'
TYPE = 'type'
ID = 'id'
