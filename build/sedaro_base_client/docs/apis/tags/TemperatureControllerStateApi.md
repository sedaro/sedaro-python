<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.temperature_controller_state_api.TemperatureControllerStateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_temperature_controller_state**](#create_temperature_controller_state) | **post** /models/branches/{branchId}/thermal/temp-controllers/states/ | Create Temperature Controller State
[**delete_temperature_controller_state**](#delete_temperature_controller_state) | **delete** /models/branches/{branchId}/thermal/temp-controllers/states/{blockId} | Delete Temperature Controller State
[**update_temperature_controller_state**](#update_temperature_controller_state) | **patch** /models/branches/{branchId}/thermal/temp-controllers/states/{blockId} | Update Temperature Controller State

# **create_temperature_controller_state**
<a name="create_temperature_controller_state"></a>
> AgentBlockCreateRes create_temperature_controller_state(branch_idtemp_controller_state_create)

Create Temperature Controller State

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import temperature_controller_state_api
from sedaro_base_client.model.agent_block_create_res import AgentBlockCreateRes
from sedaro_base_client.model.temp_controller_state_create import TempControllerStateCreate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temperature_controller_state_api.TemperatureControllerStateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = TempControllerStateCreate(
        id="id_example",
        name="name_example",
        constant_temperature=3.14,
        temp_controller="temp_controller_example",
        operational_modes=[],
    )
    try:
        # Create Temperature Controller State
        api_response = api_instance.create_temperature_controller_state(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TemperatureControllerStateApi->create_temperature_controller_state: %s\n" % e)
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
[**TempControllerStateCreate**](../../models/TempControllerStateCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_temperature_controller_state.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_temperature_controller_state.ApiResponseFor422) | Validation Error

#### create_temperature_controller_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_temperature_controller_state.ApiResponseFor422
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

# **delete_temperature_controller_state**
<a name="delete_temperature_controller_state"></a>
> AgentBlockDeleteRes delete_temperature_controller_state(branch_idblock_id)

Delete Temperature Controller State

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import temperature_controller_state_api
from sedaro_base_client.model.agent_block_delete_res import AgentBlockDeleteRes
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temperature_controller_state_api.TemperatureControllerStateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Temperature Controller State
        api_response = api_instance.delete_temperature_controller_state(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TemperatureControllerStateApi->delete_temperature_controller_state: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_temperature_controller_state.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_temperature_controller_state.ApiResponseFor422) | Validation Error

#### delete_temperature_controller_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_temperature_controller_state.ApiResponseFor422
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

# **update_temperature_controller_state**
<a name="update_temperature_controller_state"></a>
> AgentBlockUpdateRes update_temperature_controller_state(branch_idblock_idtemp_controller_state_update)

Update Temperature Controller State

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import temperature_controller_state_api
from sedaro_base_client.model.temp_controller_state_update import TempControllerStateUpdate
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.agent_block_update_res import AgentBlockUpdateRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = temperature_controller_state_api.TemperatureControllerStateApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = TempControllerStateUpdate(
        id="id_example",
        name="name_example",
        constant_temperature=3.14,
        temp_controller="temp_controller_example",
        operational_modes=[],
    )
    try:
        # Update Temperature Controller State
        api_response = api_instance.update_temperature_controller_state(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling TemperatureControllerStateApi->update_temperature_controller_state: %s\n" % e)
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
[**TempControllerStateUpdate**](../../models/TempControllerStateUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_temperature_controller_state.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_temperature_controller_state.ApiResponseFor422) | Validation Error

#### update_temperature_controller_state.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_temperature_controller_state.ApiResponseFor422
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

