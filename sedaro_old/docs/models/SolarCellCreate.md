# sedaro_old.model.solar_cell_create.SolarCellCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxPowerCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**topology** | str,  | str,  | Relationship to a &#x60;Topology&#x60; block. Reverse key: &#x60;Topology.solarCells&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**shortCircuitCurrent** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**numJunctions** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**maxPowerVoltage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**openCircuitVoltage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | [optional] 
**partNumber** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

