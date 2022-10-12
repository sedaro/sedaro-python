# sedaro.model.surface_material.SurfaceMaterial

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**hotTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**diffuseSolarReflectivity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**specularSolarReflectivity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**solarAbsorptivity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**coldTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**irEmissivity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | [optional] 
**partNumber** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**[surfaces](#surfaces)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Surface&#x60; blocks. Reverse key: &#x60;Surface.surfaceMaterial&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# surfaces

Relationship to one or more `Surface` blocks. Reverse key: `Surface.surfaceMaterial`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Surface&#x60; blocks. Reverse key: &#x60;Surface.surfaceMaterial&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

