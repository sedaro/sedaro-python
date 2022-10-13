# sedaro_base_client.model.topology.Topology

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**componentType** | str,  | str,  |  | must be one of ["POWER_PROCESSOR", ] 
**[topologyType](#topologyType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be &#x60;&#x27;&#x27;&#x60; initially.  It is required on first update. | 
**name** | str,  | str,  |  | 
**subsystem** | str,  | str,  | Relationship to a &#x60;Subsystem&#x60; block. Reverse key: &#x60;Subsystem.components&#x60;. On delete: &#x60;CASCADE&#x60; (delete this block when referenced block is deleted). | 
**battery** | str,  | str,  | Relationship to a &#x60;Battery&#x60; block. Reverse key: &#x60;Battery.topology&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
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
**[topologyParams](#topologyParams)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be undefined initially.  It is required on first update. | [optional] 
**[loads](#loads)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Load&#x60; blocks. Reverse key: &#x60;Load.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[batteryCells](#batteryCells)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;BatteryCell&#x60; blocks. Reverse key: &#x60;BatteryCell.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[busRegulators](#busRegulators)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;BusRegulator&#x60; blocks. Reverse key: &#x60;BusRegulator.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[solarArrays](#solarArrays)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarArray&#x60; blocks. Reverse key: &#x60;SolarArray.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[solarCells](#solarCells)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarCell&#x60; blocks. Reverse key: &#x60;SolarCell.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# topologyType

This field may only be `''` initially.  It is required on first update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be &#x60;&#x27;&#x27;&#x60; initially.  It is required on first update. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["", ] 
[TopologyTypes](TopologyTypes.md) | [**TopologyTypes**](TopologyTypes.md) | [**TopologyTypes**](TopologyTypes.md) |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["", ] 

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

# topologyParams

This field may only be undefined initially.  It is required on first update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be undefined initially.  It is required on first update. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TopologyParamFRD](TopologyParamFRD.md) | [**TopologyParamFRD**](TopologyParamFRD.md) | [**TopologyParamFRD**](TopologyParamFRD.md) |  | 
[TopologyParamSCH](TopologyParamSCH.md) | [**TopologyParamSCH**](TopologyParamSCH.md) | [**TopologyParamSCH**](TopologyParamSCH.md) |  | 
[TopologyParamQRD](TopologyParamQRD.md) | [**TopologyParamQRD**](TopologyParamQRD.md) | [**TopologyParamQRD**](TopologyParamQRD.md) |  | 
[TopologyParamTCM](TopologyParamTCM.md) | [**TopologyParamTCM**](TopologyParamTCM.md) | [**TopologyParamTCM**](TopologyParamTCM.md) |  | 
[TopologyParamSCM](TopologyParamSCM.md) | [**TopologyParamSCM**](TopologyParamSCM.md) | [**TopologyParamSCM**](TopologyParamSCM.md) |  | 

# loads

Relationship to one or more `Load` blocks. Reverse key: `Load.topology`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Load&#x60; blocks. Reverse key: &#x60;Load.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# batteryCells

Relationship to one or more `BatteryCell` blocks. Reverse key: `BatteryCell.topology`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;BatteryCell&#x60; blocks. Reverse key: &#x60;BatteryCell.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# busRegulators

Relationship to one or more `BusRegulator` blocks. Reverse key: `BusRegulator.topology`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;BusRegulator&#x60; blocks. Reverse key: &#x60;BusRegulator.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# solarArrays

Relationship to one or more `SolarArray` blocks. Reverse key: `SolarArray.topology`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarArray&#x60; blocks. Reverse key: &#x60;SolarArray.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# solarCells

Relationship to one or more `SolarCell` blocks. Reverse key: `SolarCell.topology`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;SolarCell&#x60; blocks. Reverse key: &#x60;SolarCell.topology&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

