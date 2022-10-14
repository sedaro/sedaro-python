<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ekf_algorithm**](#create_ekf_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/orbit-determination/ekf/ | Create EKF Algorithm
[**create_gps_algorithm**](#create_gps_algorithm) | **post** /models/branches/{branchId}/gnc/algorithms/orbit-determination/gps/ | Create GPS Algorithm
[**delete_ekf_algorithm**](#delete_ekf_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/orbit-determination/ekf/{blockId} | Delete EKF Algorithm
[**delete_gps_algorithm**](#delete_gps_algorithm) | **delete** /models/branches/{branchId}/gnc/algorithms/orbit-determination/gps/{blockId} | Delete GPS Algorithm
[**update_ekf_algorithm**](#update_ekf_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/orbit-determination/ekf/{blockId} | Update EKF Algorithm
[**update_gps_algorithm**](#update_gps_algorithm) | **patch** /models/branches/{branchId}/gnc/algorithms/orbit-determination/gps/{blockId} | Update GPS Algorithm

# **create_ekf_algorithm**
<a name="create_ekf_algorithm"></a>
> VehicleBlockCreateRes create_ekf_algorithm(branch_idekf_algorithm_create)

Create EKF Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_create_res import VehicleBlockCreateRes
from sedaro_base_client.model.ekf_algorithm_create import EKFAlgorithmCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = EKFAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ORBIT_DETERMINATION",
        algorithm_subtype="EKF",
        position_solution=[
            3.14
        ],
        velocity_solution=[
            3.14
        ],
        covariance=[
            [
                3.14
            ]
        ],
        position_covariance=[
            [
                3.14
            ]
        ],
        velocity_covariance=[],
        position_sensors=[],
    )
    try:
        # Create EKF Algorithm
        api_response = api_instance.create_ekf_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->create_ekf_algorithm: %s\n" % e)
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
[**EKFAlgorithmCreate**](../../models/EKFAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_ekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_ekf_algorithm.ApiResponseFor422) | Validation Error

#### create_ekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_ekf_algorithm.ApiResponseFor422
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

# **create_gps_algorithm**
<a name="create_gps_algorithm"></a>
> VehicleBlockCreateRes create_gps_algorithm(branch_idgps_algorithm_create)

Create GPS Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
from sedaro_base_client.model.gps_algorithm_create import GPSAlgorithmCreate
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
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = GPSAlgorithmCreate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ORBIT_DETERMINATION",
        algorithm_subtype="GPS",
        position_solution=[
            3.14
        ],
        velocity_solution=[
            3.14
        ],
        covariance=[
            [
                3.14
            ]
        ],
        position_covariance=[
            [
                3.14
            ]
        ],
        velocity_covariance=[],
        position_sensors=[],
    )
    try:
        # Create GPS Algorithm
        api_response = api_instance.create_gps_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->create_gps_algorithm: %s\n" % e)
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
[**GPSAlgorithmCreate**](../../models/GPSAlgorithmCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_gps_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_gps_algorithm.ApiResponseFor422) | Validation Error

#### create_gps_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_gps_algorithm.ApiResponseFor422
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

# **delete_ekf_algorithm**
<a name="delete_ekf_algorithm"></a>
> VehicleBlockDeleteRes delete_ekf_algorithm(branch_idblock_id)

Delete EKF Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
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
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete EKF Algorithm
        api_response = api_instance.delete_ekf_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->delete_ekf_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_ekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_ekf_algorithm.ApiResponseFor422) | Validation Error

#### delete_ekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_ekf_algorithm.ApiResponseFor422
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

# **delete_gps_algorithm**
<a name="delete_gps_algorithm"></a>
> VehicleBlockDeleteRes delete_gps_algorithm(branch_idblock_id)

Delete GPS Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
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
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete GPS Algorithm
        api_response = api_instance.delete_gps_algorithm(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->delete_gps_algorithm: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_gps_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_gps_algorithm.ApiResponseFor422) | Validation Error

#### delete_gps_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_gps_algorithm.ApiResponseFor422
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

# **update_ekf_algorithm**
<a name="update_ekf_algorithm"></a>
> VehicleBlockUpdateRes update_ekf_algorithm(branch_idblock_idekf_algorithm_update)

Update EKF Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
from sedaro_base_client.model.ekf_algorithm_update import EKFAlgorithmUpdate
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
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = EKFAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ORBIT_DETERMINATION",
        algorithm_subtype="EKF",
        position_solution=[
            3.14
        ],
        velocity_solution=[
            3.14
        ],
        covariance=[
            [
                3.14
            ]
        ],
        position_covariance=[
            [
                3.14
            ]
        ],
        velocity_covariance=[],
        position_sensors=[],
    )
    try:
        # Update EKF Algorithm
        api_response = api_instance.update_ekf_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->update_ekf_algorithm: %s\n" % e)
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
[**EKFAlgorithmUpdate**](../../models/EKFAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_ekf_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_ekf_algorithm.ApiResponseFor422) | Validation Error

#### update_ekf_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_ekf_algorithm.ApiResponseFor422
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

# **update_gps_algorithm**
<a name="update_gps_algorithm"></a>
> VehicleBlockUpdateRes update_gps_algorithm(branch_idblock_idgps_algorithm_update)

Update GPS Algorithm

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import orbit_determination_algorithm_api
from sedaro_base_client.model.gps_algorithm_update import GPSAlgorithmUpdate
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
    api_instance = orbit_determination_algorithm_api.OrbitDeterminationAlgorithmApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = GPSAlgorithmUpdate(
        id="id_example",
        name="name_example",
        rate=3.14,
        algorithm_type="ORBIT_DETERMINATION",
        algorithm_subtype="GPS",
        position_solution=[
            3.14
        ],
        velocity_solution=[
            3.14
        ],
        covariance=[
            [
                3.14
            ]
        ],
        position_covariance=[
            [
                3.14
            ]
        ],
        velocity_covariance=[],
        position_sensors=[],
    )
    try:
        # Update GPS Algorithm
        api_response = api_instance.update_gps_algorithm(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling OrbitDeterminationAlgorithmApi->update_gps_algorithm: %s\n" % e)
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
[**GPSAlgorithmUpdate**](../../models/GPSAlgorithmUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_gps_algorithm.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_gps_algorithm.ApiResponseFor422) | Validation Error

#### update_gps_algorithm.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_gps_algorithm.ApiResponseFor422
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

