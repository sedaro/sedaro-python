# sedaro.model.load_state_update.LoadStateUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**efficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**[operationalModes](#operationalModes)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.loadStates&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operationalModes

Relationship to one or more `OperationalMode` blocks. Reverse key: `OperationalMode.loadStates`. On delete: `RESTRICT` (prevent all referenced blocks from being deleted while relationship to this one exists).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.loadStates&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

