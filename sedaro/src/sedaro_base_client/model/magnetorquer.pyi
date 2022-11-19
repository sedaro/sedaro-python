# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com   # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sedaro_base_client import schemas  # noqa: F401


class Magnetorquer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bodyFrameVector",
            "componentType",
            "ratedMagneticMoment",
            "name",
            "subsystem",
            "powerAtRatedMagneticMoment",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            subsystem = schemas.StrSchema
            
            
            class componentType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def MAGNETORQUER(cls):
                    return cls("MAGNETORQUER")
            bodyFrameVector = schemas.StrSchema
            
            
            class ratedMagneticMoment(
                schemas.NumberSchema
            ):
                pass
            powerAtRatedMagneticMoment = schemas.NumberSchema
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
                pass
            
            
            class manufacturer(
                schemas.StrSchema
            ):
                pass
            hotTempRating = schemas.NumberSchema
            coldTempRating = schemas.NumberSchema
            
            
            class thermalCapacitance(
                schemas.NumberSchema
            ):
                pass
            
            
            class cotsTemplate(
                schemas.StrSchema
            ):
                pass
            
            
            class loadStates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loadStates':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            satellite = schemas.StrSchema
            
            
            class thermal_interface_A(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_A':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class thermal_interface_B(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_B':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            powerConsumed = schemas.NumberSchema
            
            
            class dissipations(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.NumberSchema
                    ):
                        pass
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, float, ],
                ) -> 'dissipations':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            hotMargin = schemas.NumberSchema
            coldMargin = schemas.NumberSchema
            
            
            class tempControllers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tempControllers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class temperature(
                schemas.NumberSchema
            ):
                pass
            busRegulator = schemas.StrSchema
            topology = schemas.StrSchema
            torque = schemas.AnyTypeSchema
            
            
            class maxTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maxTorque':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            commandedTorqueMagnitude = schemas.NumberSchema
            
            
            class estimatedMagneticFieldVector(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'estimatedMagneticFieldVector':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class pwmDutyCycle(
                schemas.NumberSchema
            ):
                pass
            magneticMoment = schemas.NumberSchema
            magneticMomentMargin = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "subsystem": subsystem,
                "componentType": componentType,
                "bodyFrameVector": bodyFrameVector,
                "ratedMagneticMoment": ratedMagneticMoment,
                "powerAtRatedMagneticMoment": powerAtRatedMagneticMoment,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
                "cotsTemplate": cotsTemplate,
                "loadStates": loadStates,
                "satellite": satellite,
                "thermal_interface_A": thermal_interface_A,
                "thermal_interface_B": thermal_interface_B,
                "powerConsumed": powerConsumed,
                "dissipations": dissipations,
                "hotMargin": hotMargin,
                "coldMargin": coldMargin,
                "tempControllers": tempControllers,
                "temperature": temperature,
                "busRegulator": busRegulator,
                "topology": topology,
                "torque": torque,
                "maxTorque": maxTorque,
                "commandedTorqueMagnitude": commandedTorqueMagnitude,
                "estimatedMagneticFieldVector": estimatedMagneticFieldVector,
                "pwmDutyCycle": pwmDutyCycle,
                "magneticMoment": magneticMoment,
                "magneticMomentMargin": magneticMomentMargin,
            }
    
    bodyFrameVector: MetaOapg.properties.bodyFrameVector
    componentType: MetaOapg.properties.componentType
    ratedMagneticMoment: MetaOapg.properties.ratedMagneticMoment
    name: MetaOapg.properties.name
    subsystem: MetaOapg.properties.subsystem
    powerAtRatedMagneticMoment: MetaOapg.properties.powerAtRatedMagneticMoment
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratedMagneticMoment"]) -> MetaOapg.properties.ratedMagneticMoment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerAtRatedMagneticMoment"]) -> MetaOapg.properties.powerAtRatedMagneticMoment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotTempRating"]) -> MetaOapg.properties.hotTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldTempRating"]) -> MetaOapg.properties.coldTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermalCapacitance"]) -> MetaOapg.properties.thermalCapacitance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cotsTemplate"]) -> MetaOapg.properties.cotsTemplate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadStates"]) -> MetaOapg.properties.loadStates: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_A"]) -> MetaOapg.properties.thermal_interface_A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_B"]) -> MetaOapg.properties.thermal_interface_B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerConsumed"]) -> MetaOapg.properties.powerConsumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dissipations"]) -> MetaOapg.properties.dissipations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotMargin"]) -> MetaOapg.properties.hotMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldMargin"]) -> MetaOapg.properties.coldMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempControllers"]) -> MetaOapg.properties.tempControllers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busRegulator"]) -> MetaOapg.properties.busRegulator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["torque"]) -> MetaOapg.properties.torque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxTorque"]) -> MetaOapg.properties.maxTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedTorqueMagnitude"]) -> MetaOapg.properties.commandedTorqueMagnitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["estimatedMagneticFieldVector"]) -> MetaOapg.properties.estimatedMagneticFieldVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pwmDutyCycle"]) -> MetaOapg.properties.pwmDutyCycle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magneticMoment"]) -> MetaOapg.properties.magneticMoment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magneticMomentMargin"]) -> MetaOapg.properties.magneticMomentMargin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "bodyFrameVector", "ratedMagneticMoment", "powerAtRatedMagneticMoment", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "powerConsumed", "dissipations", "hotMargin", "coldMargin", "tempControllers", "temperature", "busRegulator", "topology", "torque", "maxTorque", "commandedTorqueMagnitude", "estimatedMagneticFieldVector", "pwmDutyCycle", "magneticMoment", "magneticMomentMargin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subsystem"]) -> MetaOapg.properties.subsystem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentType"]) -> MetaOapg.properties.componentType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratedMagneticMoment"]) -> MetaOapg.properties.ratedMagneticMoment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerAtRatedMagneticMoment"]) -> MetaOapg.properties.powerAtRatedMagneticMoment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotTempRating"]) -> typing.Union[MetaOapg.properties.hotTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldTempRating"]) -> typing.Union[MetaOapg.properties.coldTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermalCapacitance"]) -> typing.Union[MetaOapg.properties.thermalCapacitance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cotsTemplate"]) -> typing.Union[MetaOapg.properties.cotsTemplate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadStates"]) -> typing.Union[MetaOapg.properties.loadStates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_A"]) -> typing.Union[MetaOapg.properties.thermal_interface_A, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_B"]) -> typing.Union[MetaOapg.properties.thermal_interface_B, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerConsumed"]) -> typing.Union[MetaOapg.properties.powerConsumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dissipations"]) -> typing.Union[MetaOapg.properties.dissipations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotMargin"]) -> typing.Union[MetaOapg.properties.hotMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldMargin"]) -> typing.Union[MetaOapg.properties.coldMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempControllers"]) -> typing.Union[MetaOapg.properties.tempControllers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busRegulator"]) -> typing.Union[MetaOapg.properties.busRegulator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> typing.Union[MetaOapg.properties.topology, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["torque"]) -> typing.Union[MetaOapg.properties.torque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxTorque"]) -> typing.Union[MetaOapg.properties.maxTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedTorqueMagnitude"]) -> typing.Union[MetaOapg.properties.commandedTorqueMagnitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["estimatedMagneticFieldVector"]) -> typing.Union[MetaOapg.properties.estimatedMagneticFieldVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pwmDutyCycle"]) -> typing.Union[MetaOapg.properties.pwmDutyCycle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magneticMoment"]) -> typing.Union[MetaOapg.properties.magneticMoment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magneticMomentMargin"]) -> typing.Union[MetaOapg.properties.magneticMomentMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "subsystem", "componentType", "bodyFrameVector", "ratedMagneticMoment", "powerAtRatedMagneticMoment", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "cotsTemplate", "loadStates", "satellite", "thermal_interface_A", "thermal_interface_B", "powerConsumed", "dissipations", "hotMargin", "coldMargin", "tempControllers", "temperature", "busRegulator", "topology", "torque", "maxTorque", "commandedTorqueMagnitude", "estimatedMagneticFieldVector", "pwmDutyCycle", "magneticMoment", "magneticMomentMargin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, ],
        componentType: typing.Union[MetaOapg.properties.componentType, str, ],
        ratedMagneticMoment: typing.Union[MetaOapg.properties.ratedMagneticMoment, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        subsystem: typing.Union[MetaOapg.properties.subsystem, str, ],
        powerAtRatedMagneticMoment: typing.Union[MetaOapg.properties.powerAtRatedMagneticMoment, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        cotsTemplate: typing.Union[MetaOapg.properties.cotsTemplate, str, schemas.Unset] = schemas.unset,
        loadStates: typing.Union[MetaOapg.properties.loadStates, list, tuple, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        thermal_interface_A: typing.Union[MetaOapg.properties.thermal_interface_A, list, tuple, schemas.Unset] = schemas.unset,
        thermal_interface_B: typing.Union[MetaOapg.properties.thermal_interface_B, list, tuple, schemas.Unset] = schemas.unset,
        powerConsumed: typing.Union[MetaOapg.properties.powerConsumed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dissipations: typing.Union[MetaOapg.properties.dissipations, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempControllers: typing.Union[MetaOapg.properties.tempControllers, list, tuple, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        busRegulator: typing.Union[MetaOapg.properties.busRegulator, str, schemas.Unset] = schemas.unset,
        topology: typing.Union[MetaOapg.properties.topology, str, schemas.Unset] = schemas.unset,
        torque: typing.Union[MetaOapg.properties.torque, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        maxTorque: typing.Union[MetaOapg.properties.maxTorque, list, tuple, schemas.Unset] = schemas.unset,
        commandedTorqueMagnitude: typing.Union[MetaOapg.properties.commandedTorqueMagnitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        estimatedMagneticFieldVector: typing.Union[MetaOapg.properties.estimatedMagneticFieldVector, list, tuple, schemas.Unset] = schemas.unset,
        pwmDutyCycle: typing.Union[MetaOapg.properties.pwmDutyCycle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        magneticMoment: typing.Union[MetaOapg.properties.magneticMoment, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        magneticMomentMargin: typing.Union[MetaOapg.properties.magneticMomentMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Magnetorquer':
        return super().__new__(
            cls,
            *_args,
            bodyFrameVector=bodyFrameVector,
            componentType=componentType,
            ratedMagneticMoment=ratedMagneticMoment,
            name=name,
            subsystem=subsystem,
            powerAtRatedMagneticMoment=powerAtRatedMagneticMoment,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            cotsTemplate=cotsTemplate,
            loadStates=loadStates,
            satellite=satellite,
            thermal_interface_A=thermal_interface_A,
            thermal_interface_B=thermal_interface_B,
            powerConsumed=powerConsumed,
            dissipations=dissipations,
            hotMargin=hotMargin,
            coldMargin=coldMargin,
            tempControllers=tempControllers,
            temperature=temperature,
            busRegulator=busRegulator,
            topology=topology,
            torque=torque,
            maxTorque=maxTorque,
            commandedTorqueMagnitude=commandedTorqueMagnitude,
            estimatedMagneticFieldVector=estimatedMagneticFieldVector,
            pwmDutyCycle=pwmDutyCycle,
            magneticMoment=magneticMoment,
            magneticMomentMargin=magneticMomentMargin,
            _configuration=_configuration,
            **kwargs,
        )
