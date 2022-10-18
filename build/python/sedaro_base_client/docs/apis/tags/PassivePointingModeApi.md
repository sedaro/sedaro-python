<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.passive_pointing_mode_api.PassivePointingModeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_passive_pointing_mode**](#create_passive_pointing_mode) | **post** /models/branches/{branchId}/gnc/pointing-modes/passive/ | Create Passive Pointing Mode
[**delete_passive_pointing_mode**](#delete_passive_pointing_mode) | **delete** /models/branches/{branchId}/gnc/pointing-modes/passive/{blockId} | Delete Passive Pointing Mode
[**update_passive_pointing_mode**](#update_passive_pointing_mode) | **patch** /models/branches/{branchId}/gnc/pointing-modes/passive/{blockId} | Update Passive Pointing Mode

# **create_passive_pointing_mode**
<a name="create_passive_pointing_mode"></a>
> VehicleBlockCreateRes create_passive_pointing_mode(branch_idpassive_pointing_mode_create)

Create Passive Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import passive_pointing_mode_api
from sedaro_base_client.model.passive_pointing_mode_create import PassivePointingModeCreate
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
    api_instance = passive_pointing_mode_api.PassivePointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling PassivePointingModeApi->create_passive_pointing_mode: %s\n" % e)
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
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


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

# **delete_passive_pointing_mode**
<a name="delete_passive_pointing_mode"></a>
> VehicleBlockDeleteRes delete_passive_pointing_mode(branch_idblock_id)

Delete Passive Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import passive_pointing_mode_api
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
    api_instance = passive_pointing_mode_api.PassivePointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling PassivePointingModeApi->delete_passive_pointing_mode: %s\n" % e)
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
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


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

# **update_passive_pointing_mode**
<a name="update_passive_pointing_mode"></a>
> VehicleBlockUpdateRes update_passive_pointing_mode(branch_idblock_idpassive_pointing_mode_update)

Update Passive Pointing Mode

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import passive_pointing_mode_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.passive_pointing_mode_update import PassivePointingModeUpdate
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
    api_instance = passive_pointing_mode_api.PassivePointingModeApi(api_client)

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
    except sedaro_base_client.ApiException as e:
        print("Exception when calling PassivePointingModeApi->update_passive_pointing_mode: %s\n" % e)
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
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


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

