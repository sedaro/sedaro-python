# sedaro_base_client.model.postgres_branch_vehicle_res.PostgresBranchVehicleRes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**shareable** | bool,  | BoolClass,  |  | 
**[dataSchema](#dataSchema)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**simulationRequired** | bool,  | BoolClass,  |  | 
**[blockIdToTypeMap](#blockIdToTypeMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**data** | [**VehicleTemplate**](VehicleTemplate.md) | [**VehicleTemplate**](VehicleTemplate.md) |  | 
**sharePwRqd** | bool,  | BoolClass,  |  | 
**description** | str,  | str,  |  | 
**dateModified** | str,  | str,  |  | 
**[repository](#repository)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**uuid** | str,  | str,  |  | 
**mission** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**dateCreated** | str,  | str,  |  | 
**name** | str,  | str,  |  | 
**numSimulations** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[user](#user)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**[blockClassToBlockGroupMap](#blockClassToBlockGroupMap)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# repository

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# dataSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# blockIdToTypeMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# blockClassToBlockGroupMap

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

