# sedaro_base_client.model.scenario_block_delete_res.ScenarioBlockDeleteRes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**action** | str,  | str,  |  | must be one of ["DELETE", ] 
**block** | [**GroupAndId**](GroupAndId.md) | [**GroupAndId**](GroupAndId.md) |  | 
**branch** | [**PostgresBranchScenarioRes**](PostgresBranchScenarioRes.md) | [**PostgresBranchScenarioRes**](PostgresBranchScenarioRes.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

