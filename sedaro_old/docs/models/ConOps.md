# sedaro.model.con_ops.ConOps

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**[conditions](#conditions)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[targets](#targets)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Target&#x60; blocks. Reverse key: &#x60;Target.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[targetGroups](#targetGroups)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;TargetGroup&#x60; blocks. Reverse key: &#x60;TargetGroup.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[operationalModes](#operationalModes)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[pointingModes](#pointingModes)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**activeOpMode** | str,  | str,  | Relationship to zero or one &#x60;OperationalMode&#x60; blocks. On delete: &#x60;SET_NONE&#x60; (set relationship field to &#x60;None&#x60; when referenced block is deleted). | [optional] 
**[attitude](#attitude)** | list, tuple,  | tuple,  |  | [optional] 
**[attitudeSolution](#attitudeSolution)** | list, tuple,  | tuple,  |  | [optional] 
**angularVelocitySolution** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Relationship to one or more `Condition` blocks. Reverse key: `Condition.conOps`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# targets

Relationship to one or more `Target` blocks. Reverse key: `Target.conOps`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Target&#x60; blocks. Reverse key: &#x60;Target.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# targetGroups

Relationship to one or more `TargetGroup` blocks. Reverse key: `TargetGroup.conOps`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;TargetGroup&#x60; blocks. Reverse key: &#x60;TargetGroup.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# operationalModes

Relationship to one or more `OperationalMode` blocks. Reverse key: `OperationalMode.conOps`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# pointingModes

Relationship to one or more `PointingMode` blocks. Reverse key: `PointingMode.conOps`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.conOps&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# attitude

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# attitudeSolution

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

