<a name="__pageTop"></a>
# sedaro_old.apis.tags.branches_api.BranchesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_to_branch**](#commit_to_branch) | **post** /models/branches/{branchId}commits/ | Commit changes to a branch
[**create_branch**](#create_branch) | **post** /models/branches/{branchId} | Branch off existing branch
[**delete_branch**](#delete_branch) | **delete** /models/branches/{branchId} | Delete a branch
[**get_branch**](#get_branch) | **get** /models/branches/{branchId} | Get a branch
[**get_committed_branch_data**](#get_committed_branch_data) | **get** /models/branches/{branchId}committed/ | Get saved branch data
[**get_saved_branch_data**](#get_saved_branch_data) | **get** /models/branches/{branchId}saved/ | Get committed branch data
[**merge_branches**](#merge_branches) | **post** /models/branches/{currentBranchId}/merge/{incomingBranchId} | Merge branch into another branch
[**update_branch**](#update_branch) | **patch** /models/branches/{branchId} | Update a branch
[**verify_branch_password**](#verify_branch_password) | **post** /models/branches/{branchId}share-auth/ | Verify branch bassword

# **commit_to_branch**
<a name="commit_to_branch"></a>
> MessageRes commit_to_branch(branch_idcommit_message)

Commit changes to a branch

Takes all changes to the blocks on the branch with the provided `id` and commits them to the corresponding version-controlled branch.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.message_res import MessageRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    query_params = {
        'commitMessage': "commitMessage_example",
    }
    try:
        # Commit changes to a branch
        api_response = api_instance.commit_to_branch(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->commit_to_branch: %s\n" % e)
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
commitMessage | CommitMessageSchema | | 


# CommitMessageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#commit_to_branch.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#commit_to_branch.ApiResponseFor422) | Validation Error

#### commit_to_branch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageRes**](../../models/MessageRes.md) |  | 


#### commit_to_branch.ApiResponseFor422
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

# **create_branch**
<a name="create_branch"></a>
> bool, date, datetime, dict, float, int, list, str, none_type create_branch(branch_idbranch_create)

Branch off existing branch

Creates a new branch based on and in the same repository as the branch associated with the provided `id`.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.postgres_branch_scenario import PostgresBranchScenario
from sedaro_old.model.postgres_branch_vehicle import PostgresBranchVehicle
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.branch_create import BranchCreate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = BranchCreate(
        name="name_example",
        description="description_example",
    )
    try:
        # Branch off existing branch
        api_response = api_instance.create_branch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->create_branch: %s\n" % e)
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
[**BranchCreate**](../../models/BranchCreate.md) |  | 


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
200 | [ApiResponseFor200](#create_branch.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#create_branch.ApiResponseFor422) | Validation Error

#### create_branch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PostgresBranchVehicle]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) |  | 
[PostgresBranchScenario]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) |  | 

#### create_branch.ApiResponseFor422
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

# **delete_branch**
<a name="delete_branch"></a>
> BranchDeleteRes delete_branch(branch_id)

Delete a branch

Deletes the branch with the provided `id`.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.branch_delete_res import BranchDeleteRes
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
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    try:
        # Delete a branch
        api_response = api_instance.delete_branch(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->delete_branch: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_branch.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#delete_branch.ApiResponseFor422) | Validation Error

#### delete_branch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BranchDeleteRes**](../../models/BranchDeleteRes.md) |  | 


#### delete_branch.ApiResponseFor422
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

# **get_branch**
<a name="get_branch"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_branch(branch_id)

Get a branch

Retrieves the branch with the provided `id`.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.postgres_branch_scenario import PostgresBranchScenario
from sedaro_old.model.postgres_branch_vehicle import PostgresBranchVehicle
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
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    try:
        # Get a branch
        api_response = api_instance.get_branch(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->get_branch: %s\n" % e)
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
200 | [ApiResponseFor200](#get_branch.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_branch.ApiResponseFor422) | Validation Error

#### get_branch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PostgresBranchVehicle]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) |  | 
[PostgresBranchScenario]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) |  | 

#### get_branch.ApiResponseFor422
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

# **get_committed_branch_data**
<a name="get_committed_branch_data"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_committed_branch_data(branch_id)

Get saved branch data

Retrieves all **committed** branch `data` (object with all the blocks) from the branch with the given `id`.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.scenario_template import ScenarioTemplate
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.vehicle_template import VehicleTemplate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    try:
        # Get saved branch data
        api_response = api_instance.get_committed_branch_data(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->get_committed_branch_data: %s\n" % e)
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
200 | [ApiResponseFor200](#get_committed_branch_data.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_committed_branch_data.ApiResponseFor422) | Validation Error

#### get_committed_branch_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[VehicleTemplate]({{complexTypePrefix}}VehicleTemplate.md) | [**VehicleTemplate**]({{complexTypePrefix}}VehicleTemplate.md) | [**VehicleTemplate**]({{complexTypePrefix}}VehicleTemplate.md) |  | 
[ScenarioTemplate]({{complexTypePrefix}}ScenarioTemplate.md) | [**ScenarioTemplate**]({{complexTypePrefix}}ScenarioTemplate.md) | [**ScenarioTemplate**]({{complexTypePrefix}}ScenarioTemplate.md) |  | 

#### get_committed_branch_data.ApiResponseFor422
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

# **get_saved_branch_data**
<a name="get_saved_branch_data"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_saved_branch_data(branch_id)

Get committed branch data

Retrieves all **saved** branch `data` (object with all the blocks) from the branch with the given `id`.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.scenario_template import ScenarioTemplate
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.vehicle_template import VehicleTemplate
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    try:
        # Get committed branch data
        api_response = api_instance.get_saved_branch_data(
            path_params=path_params,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->get_saved_branch_data: %s\n" % e)
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
200 | [ApiResponseFor200](#get_saved_branch_data.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_saved_branch_data.ApiResponseFor422) | Validation Error

#### get_saved_branch_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[VehicleTemplate]({{complexTypePrefix}}VehicleTemplate.md) | [**VehicleTemplate**]({{complexTypePrefix}}VehicleTemplate.md) | [**VehicleTemplate**]({{complexTypePrefix}}VehicleTemplate.md) |  | 
[ScenarioTemplate]({{complexTypePrefix}}ScenarioTemplate.md) | [**ScenarioTemplate**]({{complexTypePrefix}}ScenarioTemplate.md) | [**ScenarioTemplate**]({{complexTypePrefix}}ScenarioTemplate.md) |  | 

#### get_saved_branch_data.ApiResponseFor422
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

# **merge_branches**
<a name="merge_branches"></a>
> bool, date, datetime, dict, float, int, list, str, none_type merge_branches(current_branch_idincoming_branch_idbranch_merge)

Merge branch into another branch

Merges branch with `incomingBranchId` into branch with `currentBranchId`. This route has two functions: - To initiate the merge, send the request with no body. If there are no conflicts, it will successfully complete the merge and send back the resulting branch. - If there are conflicts, the response body will have a key of `conflicts` with a list of conflict objects outlining the \"current\" and \"incoming\" changes. Review the list, and send a second request to the same route including a list of resulutions (see optional `resultions` param in the request body schema below) indicating where you would like to keep the \"current\" or \"incoming\" changes. The indices in the `resultions` list should correspond with the indices of the `conflicts` list.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.branch_vehicle_template_res import BranchVehicleTemplateRes
from sedaro_old.model.branch_merge_conflicts_res import BranchMergeConflictsRes
from sedaro_old.model.branch_merge import BranchMerge
from sedaro_old.model.branch_scenario_template_res import BranchScenarioTemplateRes
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
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'currentBranchId': 1,
        'incomingBranchId': 1,
    }
    body = BranchMerge(
        resolutions=[
            "current"
        ],
    )
    try:
        # Merge branch into another branch
        api_response = api_instance.merge_branches(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->merge_branches: %s\n" % e)
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
[**BranchMerge**](../../models/BranchMerge.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
currentBranchId | CurrentBranchIdSchema | | 
incomingBranchId | IncomingBranchIdSchema | | 

# CurrentBranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# IncomingBranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#merge_branches.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#merge_branches.ApiResponseFor422) | Validation Error

#### merge_branches.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BranchVehicleTemplateRes]({{complexTypePrefix}}BranchVehicleTemplateRes.md) | [**BranchVehicleTemplateRes**]({{complexTypePrefix}}BranchVehicleTemplateRes.md) | [**BranchVehicleTemplateRes**]({{complexTypePrefix}}BranchVehicleTemplateRes.md) |  | 
[BranchScenarioTemplateRes]({{complexTypePrefix}}BranchScenarioTemplateRes.md) | [**BranchScenarioTemplateRes**]({{complexTypePrefix}}BranchScenarioTemplateRes.md) | [**BranchScenarioTemplateRes**]({{complexTypePrefix}}BranchScenarioTemplateRes.md) |  | 
[BranchMergeConflictsRes]({{complexTypePrefix}}BranchMergeConflictsRes.md) | [**BranchMergeConflictsRes**]({{complexTypePrefix}}BranchMergeConflictsRes.md) | [**BranchMergeConflictsRes**]({{complexTypePrefix}}BranchMergeConflictsRes.md) |  | 

#### merge_branches.ApiResponseFor422
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

# **update_branch**
<a name="update_branch"></a>
> bool, date, datetime, dict, float, int, list, str, none_type update_branch(branch_idbranch_update)

Update a branch

Updates updateable fields on the branch with the provided `id`. Note: - `shareable` indicates whether shareable links are valid for this branch. - `password` indicates whether the shareable link requires a password.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.branch_update import BranchUpdate
from sedaro_old.model.postgres_branch_scenario import PostgresBranchScenario
from sedaro_old.model.postgres_branch_vehicle import PostgresBranchVehicle
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
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = BranchUpdate(
        name="name_example",
        description="description_example",
        shareable=True,
        password="password_example",
    )
    try:
        # Update a branch
        api_response = api_instance.update_branch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->update_branch: %s\n" % e)
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
[**BranchUpdate**](../../models/BranchUpdate.md) |  | 


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
200 | [ApiResponseFor200](#update_branch.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_branch.ApiResponseFor422) | Validation Error

#### update_branch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PostgresBranchVehicle]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) | [**PostgresBranchVehicle**]({{complexTypePrefix}}PostgresBranchVehicle.md) |  | 
[PostgresBranchScenario]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) | [**PostgresBranchScenario**]({{complexTypePrefix}}PostgresBranchScenario.md) |  | 

#### update_branch.ApiResponseFor422
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

# **verify_branch_password**
<a name="verify_branch_password"></a>
> MessageRes verify_branch_password(branch_idbranch_verify_password)

Verify branch bassword

Route to verify password when a user tries to access a branch with the provided `id` via a password protected shareable link. If successful, returns a success message with a set-cookie. The cookie stores a `jwt` that allows for non-owner collaborators to send `GET` requests to the corresponding branch.

### Example

```python
import sedaro_old
from sedaro_old.apis.tags import branches_api
from sedaro_old.model.http_validation_error import HTTPValidationError
from sedaro_old.model.branch_verify_password import BranchVerifyPassword
from sedaro_old.model.message_res import MessageRes
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = sedaro_old.Configuration(
    host = "http://localhost"
)

# Enter a context with an instance of the API client
with sedaro_old.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = branches_api.BranchesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'branchId': 1,
    }
    body = BranchVerifyPassword(
        password="password_example",
    )
    try:
        # Verify branch bassword
        api_response = api_instance.verify_branch_password(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except sedaro_old.ApiException as e:
        print("Exception when calling BranchesApi->verify_branch_password: %s\n" % e)
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
[**BranchVerifyPassword**](../../models/BranchVerifyPassword.md) |  | 


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
200 | [ApiResponseFor200](#verify_branch_password.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#verify_branch_password.ApiResponseFor422) | Validation Error

#### verify_branch_password.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageRes**](../../models/MessageRes.md) |  | 


#### verify_branch_password.ApiResponseFor422
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

