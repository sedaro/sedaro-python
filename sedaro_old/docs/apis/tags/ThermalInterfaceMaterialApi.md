<a name="__pageTop"></a>
# sedaro.apis.tags.thermal_interface_material_api.ThermalInterfaceMaterialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_thermal_interface_material**](#create_thermal_interface_material) | **post** /models/branches/{branchId}/thermal/thermal-interface-materials/ | Create Thermal Interface Material
[**delete_thermal_interface_material**](#delete_thermal_interface_material) | **delete** /models/branches/{branchId}/thermal/thermal-interface-materials/{blockId} | Delete Thermal Interface Material
[**update_thermal_interface_material**](#update_thermal_interface_material) | **patch** /models/branches/{branchId}/thermal/thermal-interface-materials/{blockId} | Update Thermal Interface Material

# **create_thermal_interface_material**
<a name="create_thermal_interface_material"></a>
> AgentBlockCreateRes create_thermal_interface_material(branch_idthermal_interface_material_create)

Create Thermal Interface Material

### Example

```python
import sedaro
from sedaro.apis.tags import thermal_interface_material_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.thermal_interface_material_create import ThermalInterfaceMaterialCreate
from sedaro.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thermal_interface_material_api.ThermalInterfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = ThermalInterfaceMaterialCreate(
        id="id_example",
        part_number="",
        manufacturer="",
        resistivity=3.14,
        thickness=3.14,
        hot_temp_rating=3.14,
        cold_temp_rating=3.14,
    )
    try:
        # Create Thermal Interface Material
        api_response = api_instance.create_thermal_interface_material(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling ThermalInterfaceMaterialApi->create_thermal_interface_material: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ThermalInterfaceMaterialCreate**](../../models/ThermalInterfaceMaterialCreate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_thermal_interface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_thermal_interface_material.ApiResponseFor422) | Validation Error

#### create_thermal_interface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_thermal_interface_material.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_thermal_interface_material**
<a name="delete_thermal_interface_material"></a>
> AgentBlockDeleteRes delete_thermal_interface_material(branch_idblock_id)

Delete Thermal Interface Material

### Example

```python
import sedaro
from sedaro.apis.tags import thermal_interface_material_api
from sedaro.model.agent_block_delete_res import AgentBlockDeleteRes
from sedaro.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thermal_interface_material_api.ThermalInterfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Thermal Interface Material
        api_response = api_instance.delete_thermal_interface_material(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling ThermalInterfaceMaterialApi->delete_thermal_interface_material: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | 
blockId | BlockIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_thermal_interface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_thermal_interface_material.ApiResponseFor422) | Validation Error

#### delete_thermal_interface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_thermal_interface_material.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_thermal_interface_material**
<a name="update_thermal_interface_material"></a>
> AgentBlockUpdateRes update_thermal_interface_material(branch_idblock_idthermal_interface_material_update)

Update Thermal Interface Material

### Example

```python
import sedaro
from sedaro.apis.tags import thermal_interface_material_api
from sedaro.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro.model.thermal_interface_material_update import ThermalInterfaceMaterialUpdate
from sedaro.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = thermal_interface_material_api.ThermalInterfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = ThermalInterfaceMaterialUpdate(
        id="id_example",
        part_number="",
        manufacturer="",
        resistivity=3.14,
        thickness=3.14,
        hot_temp_rating=3.14,
        cold_temp_rating=3.14,
    )
    try:
        # Update Thermal Interface Material
        api_response = api_instance.update_thermal_interface_material(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling ThermalInterfaceMaterialApi->update_thermal_interface_material: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ThermalInterfaceMaterialUpdate**](../../models/ThermalInterfaceMaterialUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | 
blockId | BlockIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# BlockIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_thermal_interface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_thermal_interface_material.ApiResponseFor422) | Validation Error

#### update_thermal_interface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_thermal_interface_material.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

