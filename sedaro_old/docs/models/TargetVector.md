# sedaro.model.target_vector.TargetVector

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vectorType** | str,  | str,  |  | must be one of ["TARGET", ] 
**name** | str,  | str,  |  | 
**satellite** | str,  | str,  | Relationship to a &#x60;Satellite&#x60; block. Reverse key: &#x60;Satellite.referenceVectors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**targetPointingDirection** | [**TargetPointingDirections**](TargetPointingDirections.md) | [**TargetPointingDirections**](TargetPointingDirections.md) |  | 
**id** | str,  | str,  |  | [optional] 
**[truth](#truth)** | list, tuple,  | tuple,  |  | [optional] 
**[estimate](#estimate)** | list, tuple,  | tuple,  |  | [optional] 
**[pointingModes_A](#pointingModes_A)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;ActivePointingMode&#x60; blocks. Reverse key: &#x60;ActivePointingMode.lockVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[pointingModes_B](#pointingModes_B)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;MaxAlignPointingMode&#x60; blocks. Reverse key: &#x60;MaxAlignPointingMode.maxAlignVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[FOVConstraints](#FOVConstraints)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;FOVConstraint&#x60; blocks. Reverse key: &#x60;FOVConstraint.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[directionSensors](#directionSensors)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;DirectionSensor&#x60; blocks. Reverse key: &#x60;DirectionSensor.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[vectorSensors](#vectorSensors)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;VectorSensor&#x60; blocks. Reverse key: &#x60;VectorSensor.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**target** | str,  | str,  | Relationship to zero or one &#x60;Target&#x60; blocks. Reverse key: &#x60;Target.targetVectors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**targetGroup** | str,  | str,  | Relationship to zero or one &#x60;TargetGroup&#x60; blocks. Reverse key: &#x60;TargetGroup.targetVectors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# truth

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# estimate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# pointingModes_A

Relationship to one or more `ActivePointingMode` blocks. Reverse key: `ActivePointingMode.lockVector`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;ActivePointingMode&#x60; blocks. Reverse key: &#x60;ActivePointingMode.lockVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# pointingModes_B

Relationship to one or more `MaxAlignPointingMode` blocks. Reverse key: `MaxAlignPointingMode.maxAlignVector`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;MaxAlignPointingMode&#x60; blocks. Reverse key: &#x60;MaxAlignPointingMode.maxAlignVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# FOVConstraints

Relationship to one or more `FOVConstraint` blocks. Reverse key: `FOVConstraint.referenceVector`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;FOVConstraint&#x60; blocks. Reverse key: &#x60;FOVConstraint.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# directionSensors

Relationship to one or more `DirectionSensor` blocks. Reverse key: `DirectionSensor.referenceVector`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;DirectionSensor&#x60; blocks. Reverse key: &#x60;DirectionSensor.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# vectorSensors

Relationship to one or more `VectorSensor` blocks. Reverse key: `VectorSensor.referenceVector`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;VectorSensor&#x60; blocks. Reverse key: &#x60;VectorSensor.referenceVector&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

