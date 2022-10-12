<a name="__pageTop"></a>
# sedaro.apis.tags.pointing_mode_api.PointingModeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_direction_lock_pointing_mode**](#create_direction_lock_pointing_mode) | **post** /models/branches/{branchId}/gnc/pointing-modes/lock/ | Create Direction Lock Pointing Mode
[**create_max_secondary_alignment_pointing_mode**](#create_max_secondary_alignment_pointing_mode) | **post** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/ | Create Max Secondary Alignment Pointing Mode
[**create_passive_pointing_mode**](#create_passive_pointing_mode) | **post** /models/branches/{branchId}/gnc/pointing-modes/passive/ | Create Passive Pointing Mode
[**delete_direction_lock_pointing_mode**](#delete_direction_lock_pointing_mode) | **delete** /models/branches/{branchId}/gnc/pointing-modes/lock/{blockId} | Delete Direction Lock Pointing Mode
[**delete_max_secondary_alignment_pointing_mode**](#delete_max_secondary_alignment_pointing_mode) | **delete** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/{blockId} | Delete Max Secondary Alignment Pointing Mode
[**delete_passive_pointing_mode**](#delete_passive_pointing_mode) | **delete** /models/branches/{branchId}/gnc/pointing-modes/passive/{blockId} | Delete Passive Pointing Mode
[**update_direction_lock_pointing_mode**](#update_direction_lock_pointing_mode) | **patch** /models/branches/{branchId}/gnc/pointing-modes/lock/{blockId} | Update Direction Lock Pointing Mode
[**update_max_secondary_alignment_pointing_mode**](#update_max_secondary_alignment_pointing_mode) | **patch** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/{blockId} | Update Max Secondary Alignment Pointing Mode
[**update_passive_pointing_mode**](#update_passive_pointing_mode) | **patch** /models/branches/{branchId}/gnc/pointing-modes/passive/{blockId} | Update Passive Pointing Mode

# **create_direction_lock_pointing_mode**
<a name="create_direction_lock_pointing_mode"></a>
> AgentBlockCreateRes create_direction_lock_pointing_mode(branch_idlock_pointing_mode_create)

Create Direction Lock Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.lock_pointing_mode_create import LockPointingModeCreate
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = LockPointingModeCreate(
        id="id_example",
        name="name_example",
        pointing_mode_type="LOCK",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
        con_ops="con_ops_example",
        lock_vector="lock_vector_example",
        lock_body_frame_vector="lock_body_frame_vector_example",
        ac_algorithm="ac_algorithm_example",
        spin_rate=3.14,
    )
    try:
        # Create Direction Lock Pointing Mode
        api_response = api_instance.create_direction_lock_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->create_direction_lock_pointing_mode: %s\n" % e)
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
[**LockPointingModeCreate**](../../models/LockPointingModeCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_direction_lock_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_direction_lock_pointing_mode.ApiResponseFor422) | Validation Error

#### create_direction_lock_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_direction_lock_pointing_mode.ApiResponseFor422
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

# **create_max_secondary_alignment_pointing_mode**
<a name="create_max_secondary_alignment_pointing_mode"></a>
> AgentBlockCreateRes create_max_secondary_alignment_pointing_mode(branch_idmax_align_pointing_mode_create)

Create Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.max_align_pointing_mode_create import MaxAlignPointingModeCreate
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = MaxAlignPointingModeCreate(
        id="id_example",
        name="name_example",
        pointing_mode_type="MAX_SECONDARY_ALIGN",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
        con_ops="con_ops_example",
        lock_vector="lock_vector_example",
        lock_body_frame_vector="lock_body_frame_vector_example",
        ac_algorithm="ac_algorithm_example",
        max_align_vector="max_align_vector_example",
        max_align_body_frame_vector="max_align_body_frame_vector_example",
    )
    try:
        # Create Max Secondary Alignment Pointing Mode
        api_response = api_instance.create_max_secondary_alignment_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->create_max_secondary_alignment_pointing_mode: %s\n" % e)
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
[**MaxAlignPointingModeCreate**](../../models/MaxAlignPointingModeCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_max_secondary_alignment_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_max_secondary_alignment_pointing_mode.ApiResponseFor422) | Validation Error

#### create_max_secondary_alignment_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_max_secondary_alignment_pointing_mode.ApiResponseFor422
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

# **create_passive_pointing_mode**
<a name="create_passive_pointing_mode"></a>
> AgentBlockCreateRes create_passive_pointing_mode(branch_idpassive_pointing_mode_create)

Create Passive Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.http_validation_error import HTTPValidationError
from sedaro.model.passive_pointing_mode_create import PassivePointingModeCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = PassivePointingModeCreate(
        id="id_example",
        name="name_example",
        pointing_mode_type="PASSIVE",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
        con_ops="con_ops_example",
    )
    try:
        # Create Passive Pointing Mode
        api_response = api_instance.create_passive_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->create_passive_pointing_mode: %s\n" % e)
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
[**PassivePointingModeCreate**](../../models/PassivePointingModeCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_passive_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_passive_pointing_mode.ApiResponseFor422) | Validation Error

#### create_passive_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_passive_pointing_mode.ApiResponseFor422
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

# **delete_direction_lock_pointing_mode**
<a name="delete_direction_lock_pointing_mode"></a>
> AgentBlockDeleteRes delete_direction_lock_pointing_mode(branch_idblock_id)

Delete Direction Lock Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Direction Lock Pointing Mode
        api_response = api_instance.delete_direction_lock_pointing_mode(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->delete_direction_lock_pointing_mode: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_direction_lock_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_direction_lock_pointing_mode.ApiResponseFor422) | Validation Error

#### delete_direction_lock_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_direction_lock_pointing_mode.ApiResponseFor422
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

# **delete_max_secondary_alignment_pointing_mode**
<a name="delete_max_secondary_alignment_pointing_mode"></a>
> AgentBlockDeleteRes delete_max_secondary_alignment_pointing_mode(branch_idblock_id)

Delete Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Max Secondary Alignment Pointing Mode
        api_response = api_instance.delete_max_secondary_alignment_pointing_mode(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->delete_max_secondary_alignment_pointing_mode: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_max_secondary_alignment_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_max_secondary_alignment_pointing_mode.ApiResponseFor422) | Validation Error

#### delete_max_secondary_alignment_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_max_secondary_alignment_pointing_mode.ApiResponseFor422
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

# **delete_passive_pointing_mode**
<a name="delete_passive_pointing_mode"></a>
> AgentBlockDeleteRes delete_passive_pointing_mode(branch_idblock_id)

Delete Passive Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Passive Pointing Mode
        api_response = api_instance.delete_passive_pointing_mode(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->delete_passive_pointing_mode: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_passive_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_passive_pointing_mode.ApiResponseFor422) | Validation Error

#### delete_passive_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_passive_pointing_mode.ApiResponseFor422
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

# **update_direction_lock_pointing_mode**
<a name="update_direction_lock_pointing_mode"></a>
> AgentBlockUpdateRes update_direction_lock_pointing_mode(branch_idblock_idlock_pointing_mode_update)

Update Direction Lock Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.lock_pointing_mode_update import LockPointingModeUpdate
from sedaro.model.agent_block_update_res import AgentBlockUpdateRes
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = LockPointingModeUpdate(
        id="id_example",
        name="name_example",
        pointing_mode_type="LOCK",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
        lock_vector="lock_vector_example",
        lock_body_frame_vector="lock_body_frame_vector_example",
        ac_algorithm="ac_algorithm_example",
        spin_rate=3.14,
    )
    try:
        # Update Direction Lock Pointing Mode
        api_response = api_instance.update_direction_lock_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->update_direction_lock_pointing_mode: %s\n" % e)
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
[**LockPointingModeUpdate**](../../models/LockPointingModeUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_direction_lock_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_direction_lock_pointing_mode.ApiResponseFor422) | Validation Error

#### update_direction_lock_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_direction_lock_pointing_mode.ApiResponseFor422
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

# **update_max_secondary_alignment_pointing_mode**
<a name="update_max_secondary_alignment_pointing_mode"></a>
> AgentBlockUpdateRes update_max_secondary_alignment_pointing_mode(branch_idblock_idmax_align_pointing_mode_update)

Update Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro.model.max_align_pointing_mode_update import MaxAlignPointingModeUpdate
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = MaxAlignPointingModeUpdate(
        id="id_example",
        name="name_example",
        pointing_mode_type="MAX_SECONDARY_ALIGN",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
        lock_vector="lock_vector_example",
        lock_body_frame_vector="lock_body_frame_vector_example",
        ac_algorithm="ac_algorithm_example",
        max_align_vector="max_align_vector_example",
        max_align_body_frame_vector="max_align_body_frame_vector_example",
    )
    try:
        # Update Max Secondary Alignment Pointing Mode
        api_response = api_instance.update_max_secondary_alignment_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->update_max_secondary_alignment_pointing_mode: %s\n" % e)
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
[**MaxAlignPointingModeUpdate**](../../models/MaxAlignPointingModeUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_max_secondary_alignment_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_max_secondary_alignment_pointing_mode.ApiResponseFor422) | Validation Error

#### update_max_secondary_alignment_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_max_secondary_alignment_pointing_mode.ApiResponseFor422
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

# **update_passive_pointing_mode**
<a name="update_passive_pointing_mode"></a>
> AgentBlockUpdateRes update_passive_pointing_mode(branch_idblock_idpassive_pointing_mode_update)

Update Passive Pointing Mode

### Example

```python
import sedaro
from sedaro.apis.tags import pointing_mode_api
from sedaro.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro.model.passive_pointing_mode_update import PassivePointingModeUpdate
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
    api_instance = pointing_mode_api.PointingModeApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = PassivePointingModeUpdate(
        id="id_example",
        name="name_example",
        pointing_mode_type="PASSIVE",
        od_algorithm="od_algorithm_example",
        ad_algorithm="ad_algorithm_example",
    )
    try:
        # Update Passive Pointing Mode
        api_response = api_instance.update_passive_pointing_mode(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling PointingModeApi->update_passive_pointing_mode: %s\n" % e)
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
[**PassivePointingModeUpdate**](../../models/PassivePointingModeUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_passive_pointing_mode.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_passive_pointing_mode.ApiResponseFor422) | Validation Error

#### update_passive_pointing_mode.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_passive_pointing_mode.ApiResponseFor422
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

