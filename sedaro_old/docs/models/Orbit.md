# sedaro.model.orbit.Orbit

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**[initialStateDefType](#initialStateDefType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[initialStateDefParams](#initialStateDefParams)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | May only be null initially. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# initialStateDefType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[InitialStateDefType](InitialStateDefType.md) | [**InitialStateDefType**](InitialStateDefType.md) | [**InitialStateDefType**](InitialStateDefType.md) |  | 

# initialStateDefParams

May only be null initially.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | May only be null initially. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ISDPOrbitalElements](ISDPOrbitalElements.md) | [**ISDPOrbitalElements**](ISDPOrbitalElements.md) | [**ISDPOrbitalElements**](ISDPOrbitalElements.md) |  | 
[ISDPTle](ISDPTle.md) | [**ISDPTle**](ISDPTle.md) | [**ISDPTle**](ISDPTle.md) |  | 
[ISDPEci](ISDPEci.md) | [**ISDPEci**](ISDPEci.md) | [**ISDPEci**](ISDPEci.md) |  | 
[IROIss](IROIss.md) | [**IROIss**](IROIss.md) | [**IROIss**](IROIss.md) |  | 
[IROGeostat](IROGeostat.md) | [**IROGeostat**](IROGeostat.md) | [**IROGeostat**](IROGeostat.md) |  | 
[IROGeostatTransfer](IROGeostatTransfer.md) | [**IROGeostatTransfer**](IROGeostatTransfer.md) | [**IROGeostatTransfer**](IROGeostatTransfer.md) |  | 
[IROPolarCirc](IROPolarCirc.md) | [**IROPolarCirc**](IROPolarCirc.md) | [**IROPolarCirc**](IROPolarCirc.md) |  | 
[IROEquatorialCirc](IROEquatorialCirc.md) | [**IROEquatorialCirc**](IROEquatorialCirc.md) | [**IROEquatorialCirc**](IROEquatorialCirc.md) |  | 
[IROSunSyncCirc](IROSunSyncCirc.md) | [**IROSunSyncCirc**](IROSunSyncCirc.md) | [**IROSunSyncCirc**](IROSunSyncCirc.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

