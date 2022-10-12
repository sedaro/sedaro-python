# sedaro.model.passive_pointing_mode_update.PassivePointingModeUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**pointingModeType** | str,  | str,  |  | must be one of ["PASSIVE", ] 
**id** | str,  | str,  |  | [optional] 
**odAlgorithm** | str,  | str,  | Relationship to zero or one &#x60;OrbitDeterminationAlgorithm&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**adAlgorithm** | str,  | str,  | Relationship to zero or one &#x60;AttitudeDeterminationAlgorithm&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

