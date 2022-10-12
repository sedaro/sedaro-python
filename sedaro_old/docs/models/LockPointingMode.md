# sedaro.model.lock_pointing_mode.LockPointingMode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**spinRate** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**lockBodyFrameVector** | str,  | str,  | Relationship to a &#x60;BodyFrameVector&#x60; block. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**name** | str,  | str,  |  | 
**pointingModeType** | str,  | str,  |  | must be one of ["LOCK", ] 
**lockVector** | str,  | str,  | Relationship to a &#x60;ReferenceVector&#x60; block. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**acAlgorithm** | str,  | str,  | Relationship to a &#x60;AttitudeControlAlgorithm&#x60; block. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**conOps** | str,  | str,  | Relationship to a &#x60;ConOps&#x60; block. Reverse key: &#x60;ConOps.pointingModes&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**id** | str,  | str,  |  | [optional] 
**odAlgorithm** | str,  | str,  | Relationship to zero or one &#x60;OrbitDeterminationAlgorithm&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**adAlgorithm** | str,  | str,  | Relationship to zero or one &#x60;AttitudeDeterminationAlgorithm&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**[operationalModes](#operationalModes)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.pointingMode&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operationalModes

Relationship to one or more `OperationalMode` blocks. Reverse key: `OperationalMode.pointingMode`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;OperationalMode&#x60; blocks. Reverse key: &#x60;OperationalMode.pointingMode&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

