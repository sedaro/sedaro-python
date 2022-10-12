# sedaro_old.model.agent.Agent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The unique name of this Agent. | 
**id** | str,  | str,  |  | [optional] 
**peripheral** | bool,  | BoolClass,  | If true, this Agent is considered a Peripheral Agent within the Scenario. | [optional] if omitted the server will use the default value of False
**[targetMapping](#targetMapping)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A mapping from the Target Block IDs of this Agent to the IDs of other Agents in the Scenario. | [optional] if omitted the server will use the default value of {}
**[differentiatingState](#differentiatingState)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | State used to differentiate this Agent from others instantiated from the same Agent Template. This object is merged with the Agent Template model before the simulation begins.  State variable organization must be identical to the Agent Template model in order to successfully overwrite it. | [optional] if omitted the server will use the default value of {}
**templateRef** | str,  | str,  | Relationship to zero or one &#x60;TemplateRef&#x60; blocks. Reverse key: &#x60;TemplateRef.agents&#x60;. On delete: &#x60;SET_NONE&#x60; (set relationship field to &#x60;None&#x60; when referenced block is deleted). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetMapping

A mapping from the Target Block IDs of this Agent to the IDs of other Agents in the Scenario.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A mapping from the Target Block IDs of this Agent to the IDs of other Agents in the Scenario. | if omitted the server will use the default value of {}

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

# differentiatingState

State used to differentiate this Agent from others instantiated from the same Agent Template. This object is merged with the Agent Template model before the simulation begins.  State variable organization must be identical to the Agent Template model in order to successfully overwrite it.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | State used to differentiate this Agent from others instantiated from the same Agent Template. This object is merged with the Agent Template model before the simulation begins.  State variable organization must be identical to the Agent Template model in order to successfully overwrite it. | if omitted the server will use the default value of {}

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

