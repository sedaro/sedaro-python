<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.rectangular_field_of_view_api.RectangularFieldOfViewApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rectangular_field_of_view**](#create_rectangular_field_of_view) | **post** /models/branches/{branchId}/gnc/sensors/fields-of-view/rect-fields-of-view/ | Create Rectangular Field of View
[**delete_rectangular_field_of_view**](#delete_rectangular_field_of_view) | **delete** /models/branches/{branchId}/gnc/sensors/fields-of-view/rect-fields-of-view/{blockId} | Delete Rectangular Field of View
[**update_rectangular_field_of_view**](#update_rectangular_field_of_view) | **patch** /models/branches/{branchId}/gnc/sensors/fields-of-view/rect-fields-of-view/{blockId} | Update Rectangular Field of View

# **create_rectangular_field_of_view**
<a name="create_rectangular_field_of_view"></a>
> VehicleBlockCreateRes create_rectangular_field_of_view(branch_idrectangular_field_of_view_create)

Create Rectangular Field of View

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import rectangular_field_of_view_api
from sedaro_base_client.model.rectangular_field_of_view_create import RectangularFieldOfViewCreate
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
    api_instance = rectangular_field_of_view_api.RectangularFieldOfViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = RectangularFieldOfViewCreate(
        id="id_example",
        name="name_example",
        field_of_view_type="RECT_FIELD_OF_VIEW",
        boresight_body_frame_vector="boresight_body_frame_vector_example",
        height_half_angle=0.0,
        width_half_angle=0.0,
        height_body_frame_vector="height_body_frame_vector_example",
    )
    try:
        # Create Rectangular Field of View
        api_response = api_instance.create_rectangular_field_of_view(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling RectangularFieldOfViewApi->create_rectangular_field_of_view: %s\n" % e)
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
[**RectangularFieldOfViewCreate**](../../models/RectangularFieldOfViewCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_rectangular_field_of_view.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_rectangular_field_of_view.ApiResponseFor422) | Validation Error

#### create_rectangular_field_of_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockCreateRes**](../../models/VehicleBlockCreateRes.md) |  | 


#### create_rectangular_field_of_view.ApiResponseFor422
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

# **delete_rectangular_field_of_view**
<a name="delete_rectangular_field_of_view"></a>
> VehicleBlockDeleteRes delete_rectangular_field_of_view(branch_idblock_id)

Delete Rectangular Field of View

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import rectangular_field_of_view_api
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
    api_instance = rectangular_field_of_view_api.RectangularFieldOfViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    try:
        # Delete Rectangular Field of View
        api_response = api_instance.delete_rectangular_field_of_view(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling RectangularFieldOfViewApi->delete_rectangular_field_of_view: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_rectangular_field_of_view.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_rectangular_field_of_view.ApiResponseFor422) | Validation Error

#### delete_rectangular_field_of_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockDeleteRes**](../../models/VehicleBlockDeleteRes.md) |  | 


#### delete_rectangular_field_of_view.ApiResponseFor422
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

# **update_rectangular_field_of_view**
<a name="update_rectangular_field_of_view"></a>
> VehicleBlockUpdateRes update_rectangular_field_of_view(branch_idblock_idrectangular_field_of_view_update)

Update Rectangular Field of View

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import rectangular_field_of_view_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.vehicle_block_update_res import VehicleBlockUpdateRes
from sedaro_base_client.model.rectangular_field_of_view_update import RectangularFieldOfViewUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rectangular_field_of_view_api.RectangularFieldOfViewApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = RectangularFieldOfViewUpdate(
        id="id_example",
        name="name_example",
        field_of_view_type="RECT_FIELD_OF_VIEW",
        boresight_body_frame_vector="boresight_body_frame_vector_example",
        height_half_angle=0.0,
        width_half_angle=0.0,
        height_body_frame_vector="height_body_frame_vector_example",
    )
    try:
        # Update Rectangular Field of View
        api_response = api_instance.update_rectangular_field_of_view(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling RectangularFieldOfViewApi->update_rectangular_field_of_view: %s\n" % e)
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
[**RectangularFieldOfViewUpdate**](../../models/RectangularFieldOfViewUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_rectangular_field_of_view.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_rectangular_field_of_view.ApiResponseFor422) | Validation Error

#### update_rectangular_field_of_view.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**VehicleBlockUpdateRes**](../../models/VehicleBlockUpdateRes.md) |  | 


#### update_rectangular_field_of_view.ApiResponseFor422
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

