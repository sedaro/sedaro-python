<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.max_align_pointing_mode_api.MaxAlignPointingModeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_max_secondary_alignment_pointing_mode**](#create_max_secondary_alignment_pointing_mode) | **post** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/ | Create Max Secondary Alignment Pointing Mode
[**delete_max_secondary_alignment_pointing_mode**](#delete_max_secondary_alignment_pointing_mode) | **delete** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/{blockId} | Delete Max Secondary Alignment Pointing Mode
[**update_max_secondary_alignment_pointing_mode**](#update_max_secondary_alignment_pointing_mode) | **patch** /models/branches/{branchId}/gnc/pointing-modes/max-secondary-align/{blockId} | Update Max Secondary Alignment Pointing Mode

# **create_max_secondary_alignment_pointing_mode**
<a name="create_max_secondary_alignment_pointing_mode"></a>
> VehicleBlockCreateRes create_max_secondary_alignment_pointing_mode(branch_idmax_align_pointing_mode_create)

Create Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import max_align_pointing_mode_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_create_res import VehicleBlockCreateRes
from sedaro_base_client.model.max_align_pointing_mode_create import MaxAlignPointingModeCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = max_align_pointing_mode_api.MaxAlignPointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling MaxAlignPointingModeApi->create_max_secondary_alignment_pointing_mode: %s\n" % e)
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
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


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

# **delete_max_secondary_alignment_pointing_mode**
<a name="delete_max_secondary_alignment_pointing_mode"></a>
> VehicleBlockDeleteRes delete_max_secondary_alignment_pointing_mode(branch_idblock_id)

Delete Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import max_align_pointing_mode_api
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
    api_instance = max_align_pointing_mode_api.MaxAlignPointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling MaxAlignPointingModeApi->delete_max_secondary_alignment_pointing_mode: %s\n" % e)
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
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


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

# **update_max_secondary_alignment_pointing_mode**
<a name="update_max_secondary_alignment_pointing_mode"></a>
> VehicleBlockUpdateRes update_max_secondary_alignment_pointing_mode(branch_idblock_idmax_align_pointing_mode_update)

Update Max Secondary Alignment Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import max_align_pointing_mode_api
from sedaro_base_client.model.max_align_pointing_mode_update import MaxAlignPointingModeUpdate
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
    api_instance = max_align_pointing_mode_api.MaxAlignPointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling MaxAlignPointingModeApi->update_max_secondary_alignment_pointing_mode: %s\n" % e)
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
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


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

