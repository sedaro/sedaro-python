# sedaro.model.circular_field_of_view_create.CircularFieldOfViewCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**boresightBodyFrameVector** | str,  | str,  | Relationship to a &#x60;BodyFrameVector&#x60; block. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**halfAngle** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**name** | str,  | str,  |  | 
**fieldOfViewType** | str,  | str,  |  | must be one of ["CIRC_FIELD_OF_VIEW", ] 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

