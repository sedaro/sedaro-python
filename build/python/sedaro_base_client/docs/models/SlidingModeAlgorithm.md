# sedaro_base_client.model.sliding_mode_algorithm.SlidingModeAlgorithm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**epsilon** | decimal.Decimal, int, float,  | decimal.Decimal,  | The sliding mode boundary layer. Higher values may produce more error, but less chattering. | 
**gainG** | decimal.Decimal, int, float,  | decimal.Decimal,  | Scales the overall speed of convergence. | 
**algorithmType** | str,  | str,  |  | must be one of ["ATTITUDE_CONTROL", ] 
**gainK** | decimal.Decimal, int, float,  | decimal.Decimal,  | Alters the relative weighting between angular rate error. | 
**rate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**algorithmSubtype** | str,  | str,  |  | must be one of ["SLIDING_MODE", ] 
**gainC** | decimal.Decimal, int, float,  | decimal.Decimal,  | Dictates the strength of the magnetorquer desaturation torques. | 
**id** | str,  | str,  |  | [optional] 
**[actuators](#actuators)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Actuator&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | [optional] 
**[reactionWheelCommands](#reactionWheelCommands)** | list, tuple,  | tuple,  |  | [optional] 
**[magnetorquerCommands](#magnetorquerCommands)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actuators

Relationship to one or more `Actuator` blocks. On delete: `RESTRICT` (prevent all referenced blocks from being deleted while relationship to this one exists).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Actuator&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# reactionWheelCommands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# magnetorquerCommands

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

