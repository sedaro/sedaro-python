<a name="__pageTop"></a>
# sedaro_base_client.apis.tags.satellite_api.SatelliteApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_satellite**](#update_satellite) | **patch** /models/branches/{branchId}/system/satellite/{blockId} | Update Satellite

# **update_satellite**
<a name="update_satellite"></a>
> AgentBlockUpdateRes update_satellite(branch_idblock_idsatellite_update)

Update Satellite

### Example

```python
import sedaro_base_client
from sedaro_base_client.apis.tags import satellite_api
from sedaro_base_client.model.http_validation_error import HTTPValidationError
from sedaro_base_client.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro_base_client.model.satellite_update import SatelliteUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_base_client.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_base_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = satellite_api.SatelliteApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = SatelliteUpdate(
        id="id_example",
        mass=3.14,
        inertia=None,
        earthshine_irradiance=3.14,
        albedo=0.0,
        drag_torque=[
            3.14
        ],
        gravity_gradient_torque=[
            3.14
        ],
    )
    try:
        # Update Satellite
        api_response = api_instance.update_satellite(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_base_client.ApiException as e:
        print("Exception when calling SatelliteApi->update_satellite: %s\n" % e)
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
[**SatelliteUpdate**](../../models/SatelliteUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_satellite.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_satellite.ApiResponseFor422) | Validation Error

#### update_satellite.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_satellite.ApiResponseFor422
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

