<a name="__pageTop"></a>
# sedaro_old.apis.tags.attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_averaging_algorithm**](#create_averaging_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/attitude-determination/averaging/ | Create Averaging Algorithm
[**create_mekf_algorithm**](#create_mekf_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/attitude-determination/mekf/ | Create MEKF Algorithm
[**create_triad_algorithm**](#create_triad_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/attitude-determination/triad/ | Create Triad Algorithm
[**delete_averaging_algorithm**](#delete_averaging_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/attitude-determination/averaging/{blockId} | Delete Averaging Algorithm
[**delete_mekf_algorithm**](#delete_mekf_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/attitude-determination/mekf/{blockId} | Delete MEKF Algorithm
[**delete_triad_algorithm**](#delete_triad_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/attitude-determination/triad/{blockId} | Delete Triad Algorithm
[**update_averaging_algorithm**](#update_averaging_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/attitude-determination/averaging/{blockId} | Update Averaging Algorithm
[**update_mekf_algorithm**](#update_mekf_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/attitude-determination/mekf/{blockId} | Update MEKF Algorithm
[**update_triad_algorithm**](#update_triad_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/attitude-determination/triad/{blockId} | Update Triad Algorithm

# **create_averaging_algorithm**
<a name="create_averaging_algorithm"></a>
> AgentBlockCreateRes create_averaging_algorithm(branch_idaveraging_algorithm_create)

Create Averaging Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.agent_block_create_res import AgentBlockCreateRes
from sedaro_old.model.averaging_algorithm_create import AveragingAlgorithmCreate
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = AveragingAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype="AVERAGING",
        optical_attitude_sensors=[],
        angular_velocity_sensors=[],
    )
    try:
        # Create Averaging Algorithm
        api_response = api_instance.create_averaging_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->create_averaging_algorithm: %s\n" % e)
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
[**AveragingAlgorithmCreate**](../../models/AveragingAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_averaging_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_averaging_algorithm.ApiResponseFor422) | Validation Error

#### create_averaging_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_averaging_algorithm.ApiResponseFor422
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

# **create_mekf_algorithm**
<a name="create_mekf_algorithm"></a>
> AgentBlockCreateRes create_mekf_algorithm(branch_idmekf_algorithm_create)

Create MEKF Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.agent_block_create_res import AgentBlockCreateRes
from sedaro_old.model.mekf_algorithm_create import MEKFAlgorithmCreate
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = MEKFAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype="MEKF",
        covariance=None,
        optical_attitude_sensors=[],
        angular_velocity_sensors=[],
        satellite="satellite_example",
    )
    try:
        # Create MEKF Algorithm
        api_response = api_instance.create_mekf_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->create_mekf_algorithm: %s\n" % e)
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
[**MEKFAlgorithmCreate**](../../models/MEKFAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_mekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_mekf_algorithm.ApiResponseFor422) | Validation Error

#### create_mekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_mekf_algorithm.ApiResponseFor422
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

# **create_triad_algorithm**
<a name="create_triad_algorithm"></a>
> AgentBlockCreateRes create_triad_algorithm(branch_idtriad_algorithm_create)

Create Triad Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.agent_block_create_res import AgentBlockCreateRes
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.triad_algorithm_create import TriadAlgorithmCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = TriadAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype=AttDetTypes("TRIAD"),
    )
    try:
        # Create Triad Algorithm
        api_response = api_instance.create_triad_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->create_triad_algorithm: %s\n" % e)
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
[**TriadAlgorithmCreate**](../../models/TriadAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_triad_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_triad_algorithm.ApiResponseFor422) | Validation Error

#### create_triad_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_triad_algorithm.ApiResponseFor422
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

# **delete_averaging_algorithm**
<a name="delete_averaging_algorithm"></a>
> AgentBlockDeleteRes delete_averaging_algorithm(branch_idblock_id)

Delete Averaging Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Averaging Algorithm
        api_response = api_instance.delete_averaging_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->delete_averaging_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_averaging_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_averaging_algorithm.ApiResponseFor422) | Validation Error

#### delete_averaging_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_averaging_algorithm.ApiResponseFor422
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

# **delete_mekf_algorithm**
<a name="delete_mekf_algorithm"></a>
> AgentBlockDeleteRes delete_mekf_algorithm(branch_idblock_id)

Delete MEKF Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete MEKF Algorithm
        api_response = api_instance.delete_mekf_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->delete_mekf_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_mekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_mekf_algorithm.ApiResponseFor422) | Validation Error

#### delete_mekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_mekf_algorithm.ApiResponseFor422
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

# **delete_triad_algorithm**
<a name="delete_triad_algorithm"></a>
> AgentBlockDeleteRes delete_triad_algorithm(branch_idblock_id)

Delete Triad Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Triad Algorithm
        api_response = api_instance.delete_triad_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->delete_triad_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_triad_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_triad_algorithm.ApiResponseFor422) | Validation Error

#### delete_triad_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_triad_algorithm.ApiResponseFor422
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

# **update_averaging_algorithm**
<a name="update_averaging_algorithm"></a>
> AgentBlockUpdateRes update_averaging_algorithm(branch_idblock_idaveraging_algorithm_update)

Update Averaging Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.averaging_algorithm_update import AveragingAlgorithmUpdate
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = AveragingAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype="AVERAGING",
        optical_attitude_sensors=[],
        angular_velocity_sensors=[],
    )
    try:
        # Update Averaging Algorithm
        api_response = api_instance.update_averaging_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->update_averaging_algorithm: %s\n" % e)
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
[**AveragingAlgorithmUpdate**](../../models/AveragingAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_averaging_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_averaging_algorithm.ApiResponseFor422) | Validation Error

#### update_averaging_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_averaging_algorithm.ApiResponseFor422
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

# **update_mekf_algorithm**
<a name="update_mekf_algorithm"></a>
> AgentBlockUpdateRes update_mekf_algorithm(branch_idblock_idmekf_algorithm_update)

Update MEKF Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.mekf_algorithm_update import MEKFAlgorithmUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = MEKFAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype="MEKF",
        covariance=None,
        optical_attitude_sensors=[],
        angular_velocity_sensors=[],
        satellite="satellite_example",
    )
    try:
        # Update MEKF Algorithm
        api_response = api_instance.update_mekf_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->update_mekf_algorithm: %s\n" % e)
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
[**MEKFAlgorithmUpdate**](../../models/MEKFAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_mekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_mekf_algorithm.ApiResponseFor422) | Validation Error

#### update_mekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_mekf_algorithm.ApiResponseFor422
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

# **update_triad_algorithm**
<a name="update_triad_algorithm"></a>
> AgentBlockUpdateRes update_triad_algorithm(branch_idblock_idtriad_algorithm_update)

Update Triad Algorithm

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import attitude_determination_algorithm_api
from sedaro_old.model.triad_algorithm_update import TriadAlgorithmUpdate
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
    api_instance = attitude_determination_algorithm_api.AttitudeDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = TriadAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ATTITUDE_DETERMINATION",
        algorithm_subtype=AttDetTypes("TRIAD"),
    )
    try:
        # Update Triad Algorithm
        api_response = api_instance.update_triad_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling AttitudeDeterminationAlgorithmApi->update_triad_algorithm: %s\n" % e)
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
[**TriadAlgorithmUpdate**](../../models/TriadAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_triad_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_triad_algorithm.ApiResponseFor422) | Validation Error

#### update_triad_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_triad_algorithm.ApiResponseFor422
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

