<a name="__pageTop"></a>
# sedaro.apis.tags.attitude_control_algorithm_api.AttitudeControlAlgorithmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sliding_mode3x3_algorithm**](#create_sliding_mode3x3_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/attitude-control/sliding-mode/ | Create Sliding Mode 3x3 Algorithm
[**delete_sliding_mode3x3_algorithm**](#delete_sliding_mode3x3_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/attitude-control/sliding-mode/{blockId} | Delete Sliding Mode 3x3 Algorithm
[**update_sliding_mode3x3_algorithm**](#update_sliding_mode3x3_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/attitude-control/sliding-mode/{blockId} | Update Sliding Mode 3x3 Algorithm

# **create_sliding_mode3x3_algorithm**
<a name="create_sliding_mode3x3_algorithm"></a>
> AgentBlockCreateRes create_sliding_mode3x3_algorithm(branch_idsliding_mode_algorithm_create)

Create Sliding Mode 3x3 Algorithm

### Example

```python
import sedaro
from sedaro.apis.tags import attitude_control_algorithm_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.sliding_mode_algorithm_create import SlidingModeAlgorithmCreate
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
    api_instance = attitude_control_algorithm_api.AttitudeControlAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = SlidingModeAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_CONTROL",
        algorithm_subtype="SLIDING_MODE",
        actuators=[],
        gain_k=3.14,
        gain_g=3.14,
        gain_c=3.14,
        epsilon=3.14,
    )
    try:
        # Create Sliding Mode 3x3 Algorithm
        api_response = api_instance.create_sliding_mode3x3_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling AttitudeControlAlgorithmApi->create_sliding_mode3x3_algorithm: %s\n" % e)
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
[**SlidingModeAlgorithmCreate**](../../models/SlidingModeAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_sliding_mode3x3_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_sliding_mode3x3_algorithm.ApiResponseFor422) | Validation Error

#### create_sliding_mode3x3_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_sliding_mode3x3_algorithm.ApiResponseFor422
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

# **delete_sliding_mode3x3_algorithm**
<a name="delete_sliding_mode3x3_algorithm"></a>
> AgentBlockDeleteRes delete_sliding_mode3x3_algorithm(branch_idblock_id)

Delete Sliding Mode 3x3 Algorithm

### Example

```python
import sedaro
from sedaro.apis.tags import attitude_control_algorithm_api
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
    api_instance = attitude_control_algorithm_api.AttitudeControlAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Sliding Mode 3x3 Algorithm
        api_response = api_instance.delete_sliding_mode3x3_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling AttitudeControlAlgorithmApi->delete_sliding_mode3x3_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_sliding_mode3x3_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_sliding_mode3x3_algorithm.ApiResponseFor422) | Validation Error

#### delete_sliding_mode3x3_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_sliding_mode3x3_algorithm.ApiResponseFor422
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

# **update_sliding_mode3x3_algorithm**
<a name="update_sliding_mode3x3_algorithm"></a>
> AgentBlockUpdateRes update_sliding_mode3x3_algorithm(branch_idblock_idsliding_mode_algorithm_update)

Update Sliding Mode 3x3 Algorithm

### Example

```python
import sedaro
from sedaro.apis.tags import attitude_control_algorithm_api
from sedaro.model.sliding_mode_algorithm_update import SlidingModeAlgorithmUpdate
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
    api_instance = attitude_control_algorithm_api.AttitudeControlAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = SlidingModeAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_CONTROL",
        algorithm_subtype="SLIDING_MODE",
        actuators=[],
        gain_k=3.14,
        gain_g=3.14,
        gain_c=3.14,
        epsilon=3.14,
    )
    try:
        # Update Sliding Mode 3x3 Algorithm
        api_response = api_instance.update_sliding_mode3x3_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling AttitudeControlAlgorithmApi->update_sliding_mode3x3_algorithm: %s\n" % e)
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
[**SlidingModeAlgorithmUpdate**](../../models/SlidingModeAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_sliding_mode3x3_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_sliding_mode3x3_algorithm.ApiResponseFor422) | Validation Error

#### update_sliding_mode3x3_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_sliding_mode3x3_algorithm.ApiResponseFor422
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

