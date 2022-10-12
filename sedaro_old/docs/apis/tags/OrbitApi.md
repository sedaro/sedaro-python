<a name="__pageTop"></a>
# sedaro_old.apis.tags.orbit_api.OrbitApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_orbit**](#update_orbit) | **patch** /models/branches/{branchId}/gnc/orbits/{blockId} | Update Orbit

# **update_orbit**
<a name="update_orbit"></a>
> AgentBlockUpdateRes update_orbit(branch_idblock_idorbit_update)

Update Orbit

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import orbit_api
from sedaro_old.model.agent_block_update_res import AgentBlockUpdateRes
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.orbit_update import OrbitUpdate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = orbit_api.OrbitApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
        'blockId': 1,
    }
    body = OrbitUpdate(
        id="id_example",
        initial_state_def_type=None,
        initial_state_def_params=None,
    )
    try:
        # Update Orbit
        api_response = api_instance.update_orbit(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling OrbitApi->update_orbit: %s\n" % e)
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
[**OrbitUpdate**](../../models/OrbitUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_orbit.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_orbit.ApiResponseFor422) | Validation Error

#### update_orbit.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AgentBlockUpdateRes**](../../models/AgentBlockUpdateRes.md) |  | 


#### update_orbit.ApiResponseFor422
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

