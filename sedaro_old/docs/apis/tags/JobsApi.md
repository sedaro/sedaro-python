<a name="__pageTop"></a>
# sedaro_old.apis.tags.jobs_api.JobsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_simulation_status**](#get_simulation_status) | **get** /simulation/branches/{branchId}/control/{jobId} | Get simulation status
[**pause_resume_simulation**](#pause_resume_simulation) | **patch** /simulation/branches/{branchId}/control/{jobId} | [NOT FUNCTIONAL] Pause/resume running simulation
[**start_simulation**](#start_simulation) | **post** /simulation/branches/{branchId}/control/ | Start a simulation
[**terminate_simulation**](#terminate_simulation) | **delete** /simulation/branches/{branchId}/control/{jobId} | Terminate a running simulation

# **get_simulation_status**
<a name="get_simulation_status"></a>
> JobGet get_simulation_status(branch_idjob_id)

Get simulation status

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import jobs_api
from sedaro_old.model.job_get import JobGet
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
    api_instance = jobs_api.JobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'jobId': 1,
    }
    query_params = {
    }
    try:
        # Get simulation status
        api_response = api_instance.get_simulation_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling JobsApi->get_simulation_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'branchId': 1,
        'jobId': 1,
    }
    query_params = {
        'latest': False,
    }
    try:
        # Get simulation status
        api_response = api_instance.get_simulation_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling JobsApi->get_simulation_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
latest | LatestSchema | | optional


# LatestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | 
jobId | JobIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_simulation_status.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_simulation_status.ApiResponseFor422) | Validation Error

#### get_simulation_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobGet**](../../models/JobGet.md) |  | 


#### get_simulation_status.ApiResponseFor422
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

# **pause_resume_simulation**
<a name="pause_resume_simulation"></a>
> Job pause_resume_simulation(branch_idjob_idaction)

[NOT FUNCTIONAL] Pause/resume running simulation

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import jobs_api
from sedaro_old.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'jobId': 1,
    }
    query_params = {
        'action': "PAUSE",
    }
    try:
        # [NOT FUNCTIONAL] Pause/resume running simulation
        api_response = api_instance.pause_resume_simulation(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling JobsApi->pause_resume_simulation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
action | ActionSchema | | 


# ActionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["PAUSE", "RESUME", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | 
jobId | JobIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#pause_resume_simulation.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#pause_resume_simulation.ApiResponseFor422) | Validation Error

#### pause_resume_simulation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Job**](../../models/Job.md) |  | 


#### pause_resume_simulation.ApiResponseFor422
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

# **start_simulation**
<a name="start_simulation"></a>
> Job start_simulation(branch_id)

Start a simulation

`branchId` is the ID of the Scenario Template Branch to simulate.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import jobs_api
from sedaro_old.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    try:
        # Start a simulation
        api_response = api_instance.start_simulation(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling JobsApi->start_simulation: %s\n" % e)
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

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#start_simulation.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#start_simulation.ApiResponseFor422) | Validation Error

#### start_simulation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Job**](../../models/Job.md) |  | 


#### start_simulation.ApiResponseFor422
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

# **terminate_simulation**
<a name="terminate_simulation"></a>
> Job terminate_simulation(branch_idjob_id)

Terminate a running simulation

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import jobs_api
from sedaro_old.model.job import Job
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
    api_instance = jobs_api.JobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'jobId': 1,
    }
    try:
        # Terminate a running simulation
        api_response = api_instance.terminate_simulation(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling JobsApi->terminate_simulation: %s\n" % e)
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
jobId | JobIdSchema | | 

# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# JobIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#terminate_simulation.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#terminate_simulation.ApiResponseFor422) | Validation Error

#### terminate_simulation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Job**](../../models/Job.md) |  | 


#### terminate_simulation.ApiResponseFor422
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

