# sedaro_old.model.load_state_create.LoadStateCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**component** | str,  | str,  | Relationship to a &#x60;Component&#x60; block. Reverse key: &#x60;Component.loadStates&#x60;. On delete: &#x60;CASCADE&#x60; (delete this block when referenced block is deleted). | 
**efficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

