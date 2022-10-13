# sedaro_base_client.model.bus_regulator_create.BusRegulatorCreate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**efficiency** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**topology** | str,  | str,  | Relationship to a &#x60;Topology&#x60; block. Reverse key: &#x60;Topology.busRegulators&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**name** | str,  | str,  |  | 
**[inputType](#inputType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The input source to the regulator. If &#x60;BUS_REGULATOR&#x60;, &#x60;inRegulator&#x60; must be defined. | 
**maxOutputPower** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**voltage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**id** | str,  | str,  |  | [optional] 
**inRegulator** | str,  | str,  | Relationship to zero or one &#x60;BusRegulator&#x60; blocks. Reverse key: &#x60;BusRegulator.outRegulators&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# inputType

The input source to the regulator. If `BUS_REGULATOR`, `inRegulator` must be defined.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The input source to the regulator. If &#x60;BUS_REGULATOR&#x60;, &#x60;inRegulator&#x60; must be defined. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[InputTypes](InputTypes.md) | [**InputTypes**](InputTypes.md) | [**InputTypes**](InputTypes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

