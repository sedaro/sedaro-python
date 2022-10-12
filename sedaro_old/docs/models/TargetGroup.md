# sedaro.model.target_group.TargetGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | 
**[targetType](#targetType)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**conOps** | str,  | str,  | Relationship to a &#x60;ConOps&#x60; block. Reverse key: &#x60;ConOps.targetGroups&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**id** | str,  | str,  |  | [optional] 
**[targetAssociations](#targetAssociations)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Relationship with data to one or more &#x60;Target&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | [optional] if omitted the server will use the default value of {}
**[targetVectors](#targetVectors)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;TargetVector&#x60; blocks. Reverse key: &#x60;TargetVector.targetGroup&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[groupConditions_A](#groupConditions_A)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.targetGroupA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[groupPointingModes_A](#groupPointingModes_A)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.targetGroupA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**[groupPointingModes_B](#groupPointingModes_B)** | list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.targetGroupB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# targetType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Types](Types.md) | [**Types**](Types.md) | [**Types**](Types.md) |  | 

# targetAssociations

Relationship with data to one or more `Target` blocks. On delete: `RESTRICT` (prevent all referenced blocks from being deleted while relationship to this one exists).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Relationship with data to one or more &#x60;Target&#x60; blocks. On delete: &#x60;RESTRICT&#x60; (prevent all referenced blocks from being deleted while relationship to this one exists). | if omitted the server will use the default value of {}

# targetVectors

Relationship to one or more `TargetVector` blocks. Reverse key: `TargetVector.targetGroup`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;TargetVector&#x60; blocks. Reverse key: &#x60;TargetVector.targetGroup&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# groupConditions_A

Relationship to one or more `Condition` blocks. Reverse key: `Condition.targetGroupA`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;Condition&#x60; blocks. Reverse key: &#x60;Condition.targetGroupA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# groupPointingModes_A

Relationship to one or more `PointingMode` blocks. Reverse key: `PointingMode.targetGroupA`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.targetGroupA&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# groupPointingModes_B

Relationship to one or more `PointingMode` blocks. Reverse key: `PointingMode.targetGroupB`. On delete: `SET_NONE` (remove ID of referenced block from this relationship field).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relationship to one or more &#x60;PointingMode&#x60; blocks. Reverse key: &#x60;PointingMode.targetGroupB&#x60;. On delete: &#x60;SET_NONE&#x60; (remove ID of referenced block from this relationship field). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

