# sedaro.model.topology_update.TopologyUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[topologyType](#topologyType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be &#x60;&#x27;&#x27;&#x60; initially.  It is required on first update. | 
**name** | str,  | str,  |  | 
**id** | str,  | str,  |  | [optional] 
**partNumber** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**manufacturer** | str,  | str,  |  | [optional] if omitted the server will use the default value of ""
**hotTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**coldTempRating** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**thermalCapacitance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 1
**temperature** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 273.15
**[topologyParams](#topologyParams)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be undefined initially.  It is required on first update. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# topologyType

This field may only be `''` initially.  It is required on first update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be &#x60;&#x27;&#x27;&#x60; initially.  It is required on first update. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["", ] 
[TopologyTypes](TopologyTypes.md) | [**TopologyTypes**](TopologyTypes.md) | [**TopologyTypes**](TopologyTypes.md) |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["", ] 

# topologyParams

This field may only be undefined initially.  It is required on first update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This field may only be undefined initially.  It is required on first update. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TopologyParamFRD](TopologyParamFRD.md) | [**TopologyParamFRD**](TopologyParamFRD.md) | [**TopologyParamFRD**](TopologyParamFRD.md) |  | 
[TopologyParamSCH](TopologyParamSCH.md) | [**TopologyParamSCH**](TopologyParamSCH.md) | [**TopologyParamSCH**](TopologyParamSCH.md) |  | 
[TopologyParamQRD](TopologyParamQRD.md) | [**TopologyParamQRD**](TopologyParamQRD.md) | [**TopologyParamQRD**](TopologyParamQRD.md) |  | 
[TopologyParamTCM](TopologyParamTCM.md) | [**TopologyParamTCM**](TopologyParamTCM.md) | [**TopologyParamTCM**](TopologyParamTCM.md) |  | 
[TopologyParamSCM](TopologyParamSCM.md) | [**TopologyParamSCM**](TopologyParamSCM.md) | [**TopologyParamSCM**](TopologyParamSCM.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

