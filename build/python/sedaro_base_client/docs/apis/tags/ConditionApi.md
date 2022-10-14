<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.condition_api.ConditionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_condition**](#create_condition) | **post** /models/branches/{branchId}/cdh/conops/conditions/ | Create Condition
[**delete_condition**](#delete_condition) | **delete** /models/branches/{branchId}/cdh/conops/conditions/{blockId} | Delete Condition
[**update_condition**](#update_condition) | **patch** /models/branches/{branchId}/cdh/conops/conditions/{blockId} | Update Condition

# **create_condition**
<a name="create_condition"></a>
> VehicleBlockCreateRes create_condition(branch_idcondition_create)

Create Condition

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import condition_api
from sedaro_base_client.model.condition_create import ConditionCreate
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
    api_instance = condition_api.ConditionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = ConditionCreate(
        id="id_example",
        name="name_example",
        relationship=None,
        param_a_category=None,
        param_b_category=None,
        param_a=None,
        param_b=None,
        scalar=3.14,
        target_a="target_a_example",
        target_b="target_b_example",
        target_group_a="target_group_a_example",
        con_ops="con_ops_example",
    )
    try:
        # Create Condition
        api_response = api_instance.create_condition(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling ConditionApi->create_condition: %s\n" % e)
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
[**ConditionCreate**](../../models/ConditionCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_condition.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_condition.ApiResponseFor422) | Validation Error

#### create_condition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_condition.ApiResponseFor422
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

# **delete_condition**
<a name="delete_condition"></a>
> VehicleBlockDeleteRes delete_condition(branch_idblock_id)

Delete Condition

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import condition_api
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
    api_instance = condition_api.ConditionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Condition
        api_response = api_instance.delete_condition(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling ConditionApi->delete_condition: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_condition.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_condition.ApiResponseFor422) | Validation Error

#### delete_condition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_condition.ApiResponseFor422
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

# **update_condition**
<a name="update_condition"></a>
> VehicleBlockUpdateRes update_condition(branch_idblock_idcondition_update)

Update Condition

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import condition_api
from sedaro_base_client.model.condition_update import ConditionUpdate
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
    api_instance = condition_api.ConditionApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = ConditionUpdate(
        id="id_example",
        name="name_example",
        relationship=None,
        param_a_category=None,
        param_b_category=None,
        param_a=None,
        param_b=None,
        scalar=3.14,
        target_a="target_a_example",
        target_b="target_b_example",
        target_group_a="target_group_a_example",
    )
    try:
        # Update Condition
        api_response = api_instance.update_condition(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling ConditionApi->update_condition: %s\n" % e)
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
[**ConditionUpdate**](../../models/ConditionUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_condition.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_condition.ApiResponseFor422) | Validation Error

#### update_condition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_condition.ApiResponseFor422
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

