<a name="__pageTop"></a>
# sedaro_old.apis.tags.surface_material_api.SurfaceMaterialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_surface_material**](#create_surface_material) | **post** /models/branches/{branchId}/system/geometry/surfaces/materials/ | Create Surface Material
[**delete_surface_material**](#delete_surface_material) | **delete** /models/branches/{branchId}/system/geometry/surfaces/materials/{blockId} | Delete Surface Material
[**update_surface_material**](#update_surface_material) | **patch** /models/branches/{branchId}/system/geometry/surfaces/materials/{blockId} | Update Surface Material

# **create_surface_material**
<a name="create_surface_material"></a>
> AgentBlockCreateRes create_surface_material(branch_idsurface_material_create)

Create Surface Material

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import surface_material_api
from sedaro_old.model.agent_block_create_res import AgentBlockCreateRes
from sedaro_old.model.surface_material_create import SurfaceMaterialCreate
from sedaro_old.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = surface_material_api.SurfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = SurfaceMaterialCreate(
        id="id_example",
        part_number="",
        manufacturer="",
        ir_emissivity=0.0,
        solar_absorptivity=0.0,
        diffuse_solar_reflectivity=0.0,
        specular_solar_reflectivity=0.0,
        hot_temp_rating=3.14,
        cold_temp_rating=3.14,
    )
    try:
        # Create Surface Material
        api_response = api_instance.create_surface_material(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling SurfaceMaterialApi->create_surface_material: %s\n" % e)
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
[**SurfaceMaterialCreate**](../../models/SurfaceMaterialCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_surface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_surface_material.ApiResponseFor422) | Validation Error

#### create_surface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_surface_material.ApiResponseFor422
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

# **delete_surface_material**
<a name="delete_surface_material"></a>
> AgentBlockDeleteRes delete_surface_material(branch_idblock_id)

Delete Surface Material

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import surface_material_api
from sedaro_old.model.agent_block_delete_res import AgentBlockDeleteRes
from sedaro_old.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = surface_material_api.SurfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Surface Material
        api_response = api_instance.delete_surface_material(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling SurfaceMaterialApi->delete_surface_material: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_surface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_surface_material.ApiResponseFor422) | Validation Error

#### delete_surface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_surface_material.ApiResponseFor422
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

# **update_surface_material**
<a name="update_surface_material"></a>
> AgentBlockUpdateRes update_surface_material(branch_idblock_idsurface_material_update)

Update Surface Material

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import surface_material_api
from sedaro_old.model.surface_material_update import SurfaceMaterialUpdate
from sedaro_old.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro_old.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = surface_material_api.SurfaceMaterialApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = SurfaceMaterialUpdate(
        id="id_example",
        part_number="",
        manufacturer="",
        ir_emissivity=0.0,
        solar_absorptivity=0.0,
        diffuse_solar_reflectivity=0.0,
        specular_solar_reflectivity=0.0,
        hot_temp_rating=3.14,
        cold_temp_rating=3.14,
    )
    try:
        # Update Surface Material
        api_response = api_instance.update_surface_material(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling SurfaceMaterialApi->update_surface_material: %s\n" % e)
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
[**SurfaceMaterialUpdate**](../../models/SurfaceMaterialUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_surface_material.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_surface_material.ApiResponseFor422) | Validation Error

#### update_surface_material.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_surface_material.ApiResponseFor422
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

