# sedaro.model.battery_cell.BatteryCell

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[curve](#curve)** | list, tuple,  | tuple,  | Cell state of charge vs. open-circuit voltage curve. The first list should contain all SoC values in increasing order and the second should contain all Voc values [V].  Each Voc value must be greater than or equal to the prior value. | 
**esr** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**topology** | str,  | str,  | Relationship to a &#x60;Topology&#x60; block. Reverse key: &#x60;Topology.batteryCells&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**partNumber** | str,  | str,  |  | 
**maxChargeCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**maxDischargeCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**minSoc** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**capacity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | [optional] 
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**[packs](#packs)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;BatteryPack&#x60; blocks. Reverse key: &#x60;BatteryPack.cell&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
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

# packs

Relationship to one or more `BatteryPack` blocks. Reverse key: `BatteryPack.cell`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;BatteryPack&#x60; blocks. Reverse key: &#x60;BatteryPack.cell&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

