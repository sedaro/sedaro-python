# sedaro_base_client.model.component_bg.ComponentBG

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**collection** | [**Collection**](Collection.md) | [**Collection**](Collection.md) |  | [optional] 
**[data](#data)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] if omitted the server will use the default value of {}
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# data

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | if omitted the server will use the default value of {}

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Component](Component.md) | [**Component**](Component.md) | [**Component**](Component.md) |  | 
[BatteryPack](BatteryPack.md) | [**BatteryPack**](BatteryPack.md) | [**BatteryPack**](BatteryPack.md) |  | 
[SolarPanel](SolarPanel.md) | [**SolarPanel**](SolarPanel.md) | [**SolarPanel**](SolarPanel.md) |  | 
[QuasiRegDetTopology](QuasiRegDetTopology.md) | [**QuasiRegDetTopology**](QuasiRegDetTopology.md) | [**QuasiRegDetTopology**](QuasiRegDetTopology.md) |  | 
[FullyRegDetTopology](FullyRegDetTopology.md) | [**FullyRegDetTopology**](FullyRegDetTopology.md) | [**FullyRegDetTopology**](FullyRegDetTopology.md) |  | 
[SingleConvHybridTopology](SingleConvHybridTopology.md) | [**SingleConvHybridTopology**](SingleConvHybridTopology.md) | [**SingleConvHybridTopology**](SingleConvHybridTopology.md) |  | 
[TwoConvMpptTopology](TwoConvMpptTopology.md) | [**TwoConvMpptTopology**](TwoConvMpptTopology.md) | [**TwoConvMpptTopology**](TwoConvMpptTopology.md) |  | 
[SingleConvMpptTopology](SingleConvMpptTopology.md) | [**SingleConvMpptTopology**](SingleConvMpptTopology.md) | [**SingleConvMpptTopology**](SingleConvMpptTopology.md) |  | 
[Topology](Topology.md) | [**Topology**](Topology.md) | [**Topology**](Topology.md) |  | 
[ReactionWheel](ReactionWheel.md) | [**ReactionWheel**](ReactionWheel.md) | [**ReactionWheel**](ReactionWheel.md) |  | 
[Magnetorquer](Magnetorquer.md) | [**Magnetorquer**](Magnetorquer.md) | [**Magnetorquer**](Magnetorquer.md) |  | 
[DirectionSensor](DirectionSensor.md) | [**DirectionSensor**](DirectionSensor.md) | [**DirectionSensor**](DirectionSensor.md) |  | 
[OpticalAttitudeSensor](OpticalAttitudeSensor.md) | [**OpticalAttitudeSensor**](OpticalAttitudeSensor.md) | [**OpticalAttitudeSensor**](OpticalAttitudeSensor.md) |  | 
[VectorSensor](VectorSensor.md) | [**VectorSensor**](VectorSensor.md) | [**VectorSensor**](VectorSensor.md) |  | 
[PositionSensor](PositionSensor.md) | [**PositionSensor**](PositionSensor.md) | [**PositionSensor**](PositionSensor.md) |  | 
[AngularVelocitySensor](AngularVelocitySensor.md) | [**AngularVelocitySensor**](AngularVelocitySensor.md) | [**AngularVelocitySensor**](AngularVelocitySensor.md) |  | 
[Cooler](Cooler.md) | [**Cooler**](Cooler.md) | [**Cooler**](Cooler.md) |  | 
[Heater](Heater.md) | [**Heater**](Heater.md) | [**Heater**](Heater.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

