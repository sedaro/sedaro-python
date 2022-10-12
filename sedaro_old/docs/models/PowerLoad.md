# sedaro.model.power_load.PowerLoad

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**loadDefParams** | [**ConstantPower**](ConstantPower.md) | [**ConstantPower**](ConstantPower.md) |  | 
**loadState** | str,  | str,  | Relationship to a &#x60;LoadState&#x60; block. Reverse key: &#x60;LoadState.loads&#x60;. On delete: &#x60;CASCADE&#x60; (delete this block when referenced block is deleted). | 
**loadDefType** | str,  | str,  |  | must be one of ["CONSTANT_POWER", ] 
**name** | str,  | str,  |  | 
**[epsOutputType](#epsOutputType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | &#x60;CORE_OUTPUT&#x60; if connected to the regulated/unregulated Power Processor bus.  &#x60;BUS_REGULATOR&#x60; if connected to a constant voltage &#x60;BusRegulator&#x60; output. | 
**id** | str,  | str,  |  | [optional] 
**busRegulator** | str,  | str,  | Relationship to zero or one &#x60;BusRegulator&#x60; blocks. Reverse key: &#x60;BusRegulator.loads&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**topology** | str,  | str,  | Relationship to zero or one &#x60;Topology&#x60; blocks. Reverse key: &#x60;Topology.loads&#x60;. On delete: &#x60;SET_NONE&#x60; (set relationship field to &#x60;None&#x60; when referenced block is deleted). | [optional] 
**dutyCyclePeriod** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**dutyCyclePercentage** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# epsOutputType

`CORE_OUTPUT` if connected to the regulated/unregulated Power Processor bus.  `BUS_REGULATOR` if connected to a constant voltage `BusRegulator` output.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | &#x60;CORE_OUTPUT&#x60; if connected to the regulated/unregulated Power Processor bus.  &#x60;BUS_REGULATOR&#x60; if connected to a constant voltage &#x60;BusRegulator&#x60; output. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[EpsOutputTypes](EpsOutputTypes.md) | [**EpsOutputTypes**](EpsOutputTypes.md) | [**EpsOutputTypes**](EpsOutputTypes.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

