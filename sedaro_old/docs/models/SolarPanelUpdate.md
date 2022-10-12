# sedaro.model.solar_panel_update.SolarPanelUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**numSeries** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**surface** | str,  | str,  | Relationship to a &#x60;Surface&#x60; block. Reverse key: &#x60;Surface.panels&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**name** | str,  | str,  |  | 
**numParallel** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**cell** | str,  | str,  | Relationship to a &#x60;SolarCell&#x60; block. Reverse key: &#x60;SolarCell.panels&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**blockingDiodeDrop** | decimal.Decimal, int, float,  | decimal.Decimal,  | Set to 0 to omit diode. | 
**id** | str,  | str,  |  | [optional] 
**partNumber** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**hotTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**coldTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**thermalCapacitance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1
**temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 273.15
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

