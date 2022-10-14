<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.target_api.TargetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_celestial_target**](#create_celestial_target) | **post** /models/branches/{branchId}/cdh/conops/celestial-targets/ | Create Celestial Target
[**create_ground_target**](#create_ground_target) | **post** /models/branches/{branchId}/cdh/conops/ground-targets/ | Create Ground Target
[**create_space_target**](#create_space_target) | **post** /models/branches/{branchId}/cdh/conops/space-targets/ | Create Space Target
[**delete_celestial_target**](#delete_celestial_target) | **delete** /models/branches/{branchId}/cdh/conops/celestial-targets/{blockId} | Delete Celestial Target
[**delete_ground_target**](#delete_ground_target) | **delete** /models/branches/{branchId}/cdh/conops/ground-targets/{blockId} | Delete Ground Target
[**delete_space_target**](#delete_space_target) | **delete** /models/branches/{branchId}/cdh/conops/space-targets/{blockId} | Delete Space Target
[**update_celestial_target**](#update_celestial_target) | **patch** /models/branches/{branchId}/cdh/conops/celestial-targets/{blockId} | Update Celestial Target
[**update_ground_target**](#update_ground_target) | **patch** /models/branches/{branchId}/cdh/conops/ground-targets/{blockId} | Update Ground Target
[**update_space_target**](#update_space_target) | **patch** /models/branches/{branchId}/cdh/conops/space-targets/{blockId} | Update Space Target

# **create_celestial_target**
<a name="create_celestial_target"></a>
> VehicleBlockCreateRes create_celestial_target(branch_idcelestial_target_create)

Create Celestial Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_create_res import VehicleBlockCreateRes
from sedaro_base_client.model.celestial_target_create import CelestialTargetCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = CelestialTargetCreate(
        id="id_example",
        name="name_example",
        target_type="CELESTIAL_TARGET",
        polynomial_ephemeris_body=None,
        con_ops="con_ops_example",
    )
    try:
        # Create Celestial Target
        api_response = api_instance.create_celestial_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->create_celestial_target: %s\n" % e)
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
[**CelestialTargetCreate**](../../models/CelestialTargetCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_celestial_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_celestial_target.ApiResponseFor422) | Validation Error

#### create_celestial_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_celestial_target.ApiResponseFor422
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

# **create_ground_target**
<a name="create_ground_target"></a>
> VehicleBlockCreateRes create_ground_target(branch_idground_target_create)

Create Ground Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_create_res import VehicleBlockCreateRes
from sedaro_base_client.model.ground_target_create import GroundTargetCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = GroundTargetCreate(
        id="id_example",
        name="name_example",
        con_ops="con_ops_example",
        target_type="GROUND_TARGET",
    )
    try:
        # Create Ground Target
        api_response = api_instance.create_ground_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->create_ground_target: %s\n" % e)
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
[**GroundTargetCreate**](../../models/GroundTargetCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_ground_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_ground_target.ApiResponseFor422) | Validation Error

#### create_ground_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_ground_target.ApiResponseFor422
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

# **create_space_target**
<a name="create_space_target"></a>
> VehicleBlockCreateRes create_space_target(branch_idspace_target_create)

Create Space Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.space_target_create import SpaceTargetCreate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_create_res import VehicleBlockCreateRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = SpaceTargetCreate(
        id="id_example",
        name="name_example",
        con_ops="con_ops_example",
        target_type="SPACE_TARGET",
    )
    try:
        # Create Space Target
        api_response = api_instance.create_space_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->create_space_target: %s\n" % e)
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
[**SpaceTargetCreate**](../../models/SpaceTargetCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_space_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_space_target.ApiResponseFor422) | Validation Error

#### create_space_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_space_target.ApiResponseFor422
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

# **delete_celestial_target**
<a name="delete_celestial_target"></a>
> VehicleBlockDeleteRes delete_celestial_target(branch_idblock_id)

Delete Celestial Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_delete_res import VehicleBlockDeleteRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Celestial Target
        api_response = api_instance.delete_celestial_target(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->delete_celestial_target: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_celestial_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_celestial_target.ApiResponseFor422) | Validation Error

#### delete_celestial_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_celestial_target.ApiResponseFor422
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

# **delete_ground_target**
<a name="delete_ground_target"></a>
> VehicleBlockDeleteRes delete_ground_target(branch_idblock_id)

Delete Ground Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_delete_res import VehicleBlockDeleteRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Ground Target
        api_response = api_instance.delete_ground_target(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->delete_ground_target: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_ground_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_ground_target.ApiResponseFor422) | Validation Error

#### delete_ground_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_ground_target.ApiResponseFor422
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

# **delete_space_target**
<a name="delete_space_target"></a>
> VehicleBlockDeleteRes delete_space_target(branch_idblock_id)

Delete Space Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_delete_res import VehicleBlockDeleteRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Space Target
        api_response = api_instance.delete_space_target(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->delete_space_target: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_space_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_space_target.ApiResponseFor422) | Validation Error

#### delete_space_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_space_target.ApiResponseFor422
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

# **update_celestial_target**
<a name="update_celestial_target"></a>
> VehicleBlockUpdateRes update_celestial_target(branch_idblock_idcelestial_target_update)

Update Celestial Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.celestial_target_update import CelestialTargetUpdate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_update_res import VehicleBlockUpdateRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = CelestialTargetUpdate(
        id="id_example",
        name="name_example",
        target_type="CELESTIAL_TARGET",
        polynomial_ephemeris_body=None,
    )
    try:
        # Update Celestial Target
        api_response = api_instance.update_celestial_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->update_celestial_target: %s\n" % e)
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
[**CelestialTargetUpdate**](../../models/CelestialTargetUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_celestial_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_celestial_target.ApiResponseFor422) | Validation Error

#### update_celestial_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_celestial_target.ApiResponseFor422
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

# **update_ground_target**
<a name="update_ground_target"></a>
> VehicleBlockUpdateRes update_ground_target(branch_idblock_idground_target_update)

Update Ground Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.ground_target_update import GroundTargetUpdate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_update_res import VehicleBlockUpdateRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = GroundTargetUpdate(
        id="id_example",
        name="name_example",
        target_type="GROUND_TARGET",
    )
    try:
        # Update Ground Target
        api_response = api_instance.update_ground_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->update_ground_target: %s\n" % e)
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
[**GroundTargetUpdate**](../../models/GroundTargetUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_ground_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_ground_target.ApiResponseFor422) | Validation Error

#### update_ground_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_ground_target.ApiResponseFor422
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

# **update_space_target**
<a name="update_space_target"></a>
> VehicleBlockUpdateRes update_space_target(branch_idblock_idspace_target_update)

Update Space Target

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import target_api
from sedaro_base_client.model.space_target_update import SpaceTargetUpdate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_update_res import VehicleBlockUpdateRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = target_api.TargetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = SpaceTargetUpdate(
        id="id_example",
        name="name_example",
        target_type="SPACE_TARGET",
    )
    try:
        # Update Space Target
        api_response = api_instance.update_space_target(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TargetApi->update_space_target: %s\n" % e)
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
[**SpaceTargetUpdate**](../../models/SpaceTargetUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_space_target.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_space_target.ApiResponseFor422) | Validation Error

#### update_space_target.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_space_target.ApiResponseFor422
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

