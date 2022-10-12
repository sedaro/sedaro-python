<a name="__pageTop"></a>
# sedaro.apis.tags.simulation_clock_configuration_api.SimulationClockConfigurationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_simulation_clock_configuration**](#create_simulation_clock_configuration) | **post** /models/branches/{branchId}/clock-configs/ | Create Simulation Clock Configuration
[**delete_simulation_clock_configuration**](#delete_simulation_clock_configuration) | **delete** /models/branches/{branchId}/clock-configs/{blockId} | Delete Simulation Clock Configuration
[**update_simulation_clock_configuration**](#update_simulation_clock_configuration) | **patch** /models/branches/{branchId}/clock-configs/{blockId} | Update Simulation Clock Configuration

# **create_simulation_clock_configuration**
<a name="create_simulation_clock_configuration"></a>
> ScenarioBlockCreateRes create_simulation_clock_configuration(branch_idclock_config)

Create Simulation Clock Configuration

### Example

```python
import sedaro
from sedaro.apis.tags import simulation_clock_configuration_api
from sedaro.model.scenario_block_create_res import ScenarioBlockCreateRes
from sedaro.model.clock_config import ClockConfig
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
    api_instance = simulation_clock_configuration_api.SimulationClockConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = ClockConfig(
        id="id_example",
        start_time=3.14,
        stop_time=3.14,
        real_time=False,
    )
    try:
        # Create Simulation Clock Configuration
        api_response = api_instance.create_simulation_clock_configuration(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling SimulationClockConfigurationApi->create_simulation_clock_configuration: %s\n" % e)
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
[**ClockConfig**](../../models/ClockConfig.md) |  | 


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
200 | [ApiResponseFor200](#create_simulation_clock_configuration.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_simulation_clock_configuration.ApiResponseFor422) | Validation Error

#### create_simulation_clock_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScenarioBlockCreateRes**](../../models/ScenarioBlockCreateRes.md) |  | 


#### create_simulation_clock_configuration.ApiResponseFor422
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

# **delete_simulation_clock_configuration**
<a name="delete_simulation_clock_configuration"></a>
> ScenarioBlockDeleteRes delete_simulation_clock_configuration(branch_idblock_id)

Delete Simulation Clock Configuration

### Example

```python
import sedaro
from sedaro.apis.tags import simulation_clock_configuration_api
from sedaro.model.scenario_block_delete_res import ScenarioBlockDeleteRes
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
    api_instance = simulation_clock_configuration_api.SimulationClockConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Simulation Clock Configuration
        api_response = api_instance.delete_simulation_clock_configuration(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling SimulationClockConfigurationApi->delete_simulation_clock_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_simulation_clock_configuration.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_simulation_clock_configuration.ApiResponseFor422) | Validation Error

#### delete_simulation_clock_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScenarioBlockDeleteRes**](../../models/ScenarioBlockDeleteRes.md) |  | 


#### delete_simulation_clock_configuration.ApiResponseFor422
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

# **update_simulation_clock_configuration**
<a name="update_simulation_clock_configuration"></a>
> ScenarioBlockUpdateRes update_simulation_clock_configuration(branch_idblock_idclock_config)

Update Simulation Clock Configuration

### Example

```python
import sedaro
from sedaro.apis.tags import simulation_clock_configuration_api
from sedaro.model.scenario_block_update_res import ScenarioBlockUpdateRes
from sedaro.model.clock_config import ClockConfig
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
    api_instance = simulation_clock_configuration_api.SimulationClockConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = ClockConfig(
        id="id_example",
        start_time=3.14,
        stop_time=3.14,
        real_time=False,
    )
    try:
        # Update Simulation Clock Configuration
        api_response = api_instance.update_simulation_clock_configuration(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling SimulationClockConfigurationApi->update_simulation_clock_configuration: %s\n" % e)
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
[**ClockConfig**](../../models/ClockConfig.md) |  | 


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
200 | [ApiResponseFor200](#update_simulation_clock_configuration.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_simulation_clock_configuration.ApiResponseFor422) | Validation Error

#### update_simulation_clock_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ScenarioBlockUpdateRes**](../../models/ScenarioBlockUpdateRes.md) |  | 


#### update_simulation_clock_configuration.ApiResponseFor422
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

