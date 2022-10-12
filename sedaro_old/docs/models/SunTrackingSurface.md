# sedaro_old.model.sun_tracking_surface.SunTrackingSurface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**area** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**bodyFrameVector** | str,  | str,  | Relationship to a &#x60;BodyFrameVector&#x60; block. Reverse key: &#x60;BodyFrameVector.surfaces&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**[surfaceCentroid](#surfaceCentroid)** | list, tuple,  | tuple,  |  | 
**motionType** | str,  | str,  |  | must be one of ["SUN_TRACKING", ] 
**name** | str,  | str,  |  | 
**satellite** | str,  | str,  | Relationship to a &#x60;Satellite&#x60; block. Reverse key: &#x60;Satellite.surfaces&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**surfaceMaterial** | str,  | str,  | Relationship to a &#x60;SurfaceMaterial&#x60; block. Reverse key: &#x60;SurfaceMaterial.surfaces&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**id** | str,  | str,  |  | [optional] 
**[panels](#panels)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarPanel&#x60; blocks. Reverse key: &#x60;SolarPanel.surface&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[thermal_interface_A](#thermal_interface_A)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.surfaceA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[thermal_interface_B](#thermal_interface_B)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.surfaceB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**heliocenterAngle** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**geocenterAngle** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**earthAlbedoViewFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**earthIrViewFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**solarViewFactor** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**surfaceNormalVector** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[sat2Sun](#sat2Sun)** | list, tuple,  | tuple,  |  | [optional] 
**earthIrHeatFlowRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**earthAlbedoHeatFlowRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**solarHeatFlowRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**spaceHeatFlowRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**heatFlowRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**hotMargin** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**coldMargin** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**articulationAngle** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# surfaceCentroid

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# panels

Relationship to one or more `SolarPanel` blocks. Reverse key: `SolarPanel.surface`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarPanel&#x60; blocks. Reverse key: &#x60;SolarPanel.surface&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# thermal_interface_A

Relationship to one or more `ThermalInterface` blocks. Reverse key: `ThermalInterface.surfaceA`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.surfaceA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# thermal_interface_B

Relationship to one or more `ThermalInterface` blocks. Reverse key: `ThermalInterface.surfaceB`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.surfaceB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# sat2Sun

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

