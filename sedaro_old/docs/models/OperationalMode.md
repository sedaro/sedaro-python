# sedaro.model.operational_mode.OperationalMode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pointingMode** | str,  | str,  | Relationship to a &#x60;PointingMode&#x60; block. Reverse key: &#x60;PointingMode.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**name** | str,  | str,  |  | 
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Higher values have higher priority. Default op modes have priorty &#x3D;&#x3D; &#x60;0&#x60;. | 
**conOps** | str,  | str,  | Relationship to a &#x60;ConOps&#x60; block. Reverse key: &#x60;ConOps.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**id** | str,  | str,  |  | [optional] 
**minOccurrenceDuration** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**maxOccurrenceDuration** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**minTimeBetweenOccurrences** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**[conditions](#conditions)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | [optional] 
**[groupConditions](#groupConditions)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | [optional] 
**[tempControllerStates](#tempControllerStates)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;TempControllerState&#x60; blocks. Reverse key: &#x60;TempControllerState.operationalModes&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[loadStates](#loadStates)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;LoadState&#x60; blocks. Reverse key: &#x60;LoadState.operationalModes&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[activeTargetByTargetGroup](#activeTargetByTargetGroup)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**compliance** | bool,  | BoolClass,  |  | [optional] 
**timeSinceActive** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**timeSinceInactive** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**isActive** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

Relationship to one or more `Condition` blocks. Reverse key: `Condition.operationalModes`. On delete: `RESTRICT` (prevent all referenced blocks from being deleted while relationship to this one exists).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# groupConditions

Relationship to one or more `Condition` blocks. Reverse key: `Condition.operationalModes`. On delete: `RESTRICT` (prevent all referenced blocks from being deleted while relationship to this one exists).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.operationalModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# tempControllerStates

Relationship to one or more `TempControllerState` blocks. Reverse key: `TempControllerState.operationalModes`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;TempControllerState&#x60; blocks. Reverse key: &#x60;TempControllerState.operationalModes&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# loadStates

Relationship to one or more `LoadState` blocks. Reverse key: `LoadState.operationalModes`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;LoadState&#x60; blocks. Reverse key: &#x60;LoadState.operationalModes&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# activeTargetByTargetGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

