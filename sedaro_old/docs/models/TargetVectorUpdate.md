# sedaro.model.target_vector_update.TargetVectorUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**vectorType** | str,  | str,  |  | must be one of ["TARGET", ] 
**name** | str,  | str,  |  | 
**targetPointingDirection** | [**TargetPointingDirections**](TargetPointingDirections.md) | [**TargetPointingDirections**](TargetPointingDirections.md) |  | 
**id** | str,  | str,  |  | [optional] 
**target** | str,  | str,  | Relationship to zero or one &#x60;Target&#x60; blocks. Reverse key: &#x60;Target.targetVectors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**targetGroup** | str,  | str,  | Relationship to zero or one &#x60;TargetGroup&#x60; blocks. Reverse key: &#x60;TargetGroup.targetVectors&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

