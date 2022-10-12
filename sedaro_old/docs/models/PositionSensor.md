# sedaro_old.model.position_sensor.PositionSensor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**componentType** | str,  | str,  |  | must be one of ["POSITION_SENSOR", ] 
**oneSigmaDistanceError** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**subsystem** | str,  | str,  | Relationship to a &#x60;Subsystem&#x60; block. Reverse key: &#x60;Subsystem.components&#x60;. On delete: &#x60;CASCADE&#x60; (delete this block when referenced block is deleted). | 
**id** | str,  | str,  |  | [optional] 
**partNumber** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**hotTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**coldTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**thermalCapacitance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1
**temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 273.15
**cotsTemplate** | str,  | str,  | Read-only | [optional] if omitted the server will use the default value of ""
**[loadStates](#loadStates)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;LoadState&#x60; blocks. Reverse key: &#x60;LoadState.component&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**satellite** | str,  | str,  | Relationship to zero or one &#x60;Satellite&#x60; blocks. Reverse key: &#x60;Satellite.components&#x60;. On delete: &#x60;SET_NONE&#x60; (set relationship field to &#x60;None&#x60; when referenced block is deleted). | [optional] 
**[thermal_interface_A](#thermal_interface_A)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.componentA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[thermal_interface_B](#thermal_interface_B)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.componentB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[dissipations](#dissipations)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**hotMargin** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**coldMargin** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[tempControllers](#tempControllers)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;TempController&#x60; blocks. Reverse key: &#x60;TempController.controlledComponent&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**fieldOfView** | str,  | str,  | Relationship to zero or one &#x60;FieldOfView&#x60; blocks. Reverse key: &#x60;FieldOfView.sensors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**[measurement](#measurement)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# loadStates

Relationship to one or more `LoadState` blocks. Reverse key: `LoadState.component`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;LoadState&#x60; blocks. Reverse key: &#x60;LoadState.component&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# thermal_interface_A

Relationship to one or more `ThermalInterface` blocks. Reverse key: `ThermalInterface.componentA`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.componentA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# thermal_interface_B

Relationship to one or more `ThermalInterface` blocks. Reverse key: `ThermalInterface.componentB`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;ThermalInterface&#x60; blocks. Reverse key: &#x60;ThermalInterface.componentB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# dissipations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int, float,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

# tempControllers

Relationship to one or more `TempController` blocks. Reverse key: `TempController.controlledComponent`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;TempController&#x60; blocks. Reverse key: &#x60;TempController.controlledComponent&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# measurement

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

