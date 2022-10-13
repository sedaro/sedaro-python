# sedaro_base_client.model.thermal_interface_update.ThermalInterfaceUpdate

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**area** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**material** | str,  | str,  | Relationship to a &#x60;ThermalInterfaceMaterial&#x60; block. Reverse key: &#x60;ThermalInterfaceMaterial.thermalInterface&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | 
**name** | str,  | str,  |  | 
**sideB** | [**SideCategories**](SideCategories.md) | [**SideCategories**](SideCategories.md) |  | 
**sideA** | [**SideCategories**](SideCategories.md) | [**SideCategories**](SideCategories.md) |  | 
**componentA** | str,  | str,  | Relationship to zero or one &#x60;Component&#x60; blocks. Reverse key: &#x60;Component.thermal_interface_A&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**componentB** | str,  | str,  | Relationship to zero or one &#x60;Component&#x60; blocks. Reverse key: &#x60;Component.thermal_interface_B&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**surfaceA** | str,  | str,  | Relationship to zero or one &#x60;Surface&#x60; blocks. Reverse key: &#x60;Surface.thermal_interface_A&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**surfaceB** | str,  | str,  | Relationship to zero or one &#x60;Surface&#x60; blocks. Reverse key: &#x60;Surface.thermal_interface_B&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**coolerA** | str,  | str,  | Relationship to zero or one &#x60;Cooler&#x60; blocks. Reverse key: &#x60;Cooler.thermal_interface_cooler_A&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**coolerB** | str,  | str,  | Relationship to zero or one &#x60;Cooler&#x60; blocks. Reverse key: &#x60;Cooler.thermal_interface_cooler_B&#x60;. On delete: &#x60;RESTRICT&#x60; (prevent referenced block from being deleted while relationship to this one exists). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

