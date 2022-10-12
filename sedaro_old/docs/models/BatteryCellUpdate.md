# sedaro_old.model.battery_cell_update.BatteryCellUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[curve](#curve)** | list, tuple,  | tuple,  | Cell state of charge vs. open-circuit voltage curve. The first list should contain all SoC values in increasing order and the second should contain all Voc values [V].  Each Voc value must be greater than or equal to the prior value. | 
**esr** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**partNumber** | str,  | str,  |  | 
**maxChargeCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**maxDischargeCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**minSoc** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**capacity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | [optional] 
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# curve

Cell state of charge vs. open-circuit voltage curve. The first list should contain all SoC values in increasing order and the second should contain all Voc values [V].  Each Voc value must be greater than or equal to the prior value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Cell state of charge vs. open-circuit voltage curve. The first list should contain all SoC values in increasing order and the second should contain all Voc values [V].  Each Voc value must be greater than or equal to the prior value. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

