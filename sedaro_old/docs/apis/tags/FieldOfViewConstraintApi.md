<a name="__pageTop"></a>
# sedaro.apis.tags.field_of_view_constraint_api.FieldOfViewConstraintApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field_of_view_constraint**](#create_field_of_view_constraint) | **post** /models/branches/{branchId}/gnc/sensors/fields-of-view/constraints/ | Create Field of View Constraint
[**delete_field_of_view_constraint**](#delete_field_of_view_constraint) | **delete** /models/branches/{branchId}/gnc/sensors/fields-of-view/constraints/{blockId} | Delete Field of View Constraint
[**update_field_of_view_constraint**](#update_field_of_view_constraint) | **patch** /models/branches/{branchId}/gnc/sensors/fields-of-view/constraints/{blockId} | Update Field of View Constraint

# **create_field_of_view_constraint**
<a name="create_field_of_view_constraint"></a>
> AgentBlockCreateRes create_field_of_view_constraint(branch_idfov_constraint_create)

Create Field of View Constraint

### Example

```python
import sedaro
from sedaro.apis.tags import field_of_view_constraint_api
from sedaro.model.agent_block_create_res import AgentBlockCreateRes
from sedaro.model.fov_constraint_create import FOVConstraintCreate
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
    api_instance = field_of_view_constraint_api.FieldOfViewConstraintApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = FOVConstraintCreate(
        id="id_example",
        name="name_example",
        keepout=True,
        destructive=True,
        reference_vector="reference_vector_example",
        field_of_view="field_of_view_example",
    )
    try:
        # Create Field of View Constraint
        api_response = api_instance.create_field_of_view_constraint(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling FieldOfViewConstraintApi->create_field_of_view_constraint: %s\n" % e)
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
[**FOVConstraintCreate**](../../models/FOVConstraintCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_field_of_view_constraint.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_field_of_view_constraint.ApiResponseFor422) | Validation Error

#### create_field_of_view_constraint.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockCreateRes**](../../models/AgentBlockCreateRes.md) |  | 


#### create_field_of_view_constraint.ApiResponseFor422
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

# **delete_field_of_view_constraint**
<a name="delete_field_of_view_constraint"></a>
> AgentBlockDeleteRes delete_field_of_view_constraint(branch_idblock_id)

Delete Field of View Constraint

### Example

```python
import sedaro
from sedaro.apis.tags import field_of_view_constraint_api
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
    api_instance = field_of_view_constraint_api.FieldOfViewConstraintApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Field of View Constraint
        api_response = api_instance.delete_field_of_view_constraint(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling FieldOfViewConstraintApi->delete_field_of_view_constraint: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_field_of_view_constraint.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_field_of_view_constraint.ApiResponseFor422) | Validation Error

#### delete_field_of_view_constraint.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockDeleteRes**](../../models/AgentBlockDeleteRes.md) |  | 


#### delete_field_of_view_constraint.ApiResponseFor422
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

# **update_field_of_view_constraint**
<a name="update_field_of_view_constraint"></a>
> AgentBlockUpdateRes update_field_of_view_constraint(branch_idblock_idfov_constraint_update)

Update Field of View Constraint

### Example

```python
import sedaro
from sedaro.apis.tags import field_of_view_constraint_api
from sedaro.model.fov_constraint_update import FOVConstraintUpdate
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
    api_instance = field_of_view_constraint_api.FieldOfViewConstraintApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = FOVConstraintUpdate(
        id="id_example",
        name="name_example",
        keepout=True,
        destructive=True,
        reference_vector="reference_vector_example",
        field_of_view="field_of_view_example",
    )
    try:
        # Update Field of View Constraint
        api_response = api_instance.update_field_of_view_constraint(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro.ApiException as e:
        print("Exception when calling FieldOfViewConstraintApi->update_field_of_view_constraint: %s\n" % e)
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
[**FOVConstraintUpdate**](../../models/FOVConstraintUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_field_of_view_constraint.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_field_of_view_constraint.ApiResponseFor422) | Validation Error

#### update_field_of_view_constraint.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_field_of_view_constraint.ApiResponseFor422
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

