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


class Battery(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "maxDischargeCurrentOverride",
            "topology",
            "initialSoc",
            "minSocOverride",
            "configurationType",
            "maxChargeCurrentOverride",
        }
        
        class properties:
            
            
            class configurationType(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def EMPTY(cls):
                            return cls("")
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            ConfigurationTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'configurationType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class initialSoc(
                schemas.NumberSchema
            ):
                pass
            
            
            class maxChargeCurrentOverride(
                schemas.NumberSchema
            ):
                pass
            
            
            class maxDischargeCurrentOverride(
                schemas.NumberSchema
            ):
                pass
            
            
            class minSocOverride(
                schemas.NumberSchema
            ):
                pass
            topology = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class packs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'packs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            current = schemas.NumberSchema
            voltage = schemas.NumberSchema
            power = schemas.NumberSchema
            
            
            class soc(
                schemas.NumberSchema
            ):
                pass
            curve = schemas.AnyTypeSchema
            idealMaxChargeCurrent = schemas.NumberSchema
            maxChargeCurrent = schemas.NumberSchema
            maxChargeVoltage = schemas.NumberSchema
            maxChargePower = schemas.NumberSchema
            idealMaxDischargeCurrent = schemas.NumberSchema
            esr = schemas.NumberSchema
            capacity = schemas.NumberSchema
            
            
            class minSoc(
                schemas.NumberSchema
            ):
                pass
            voc = schemas.NumberSchema
            __annotations__ = {
                "configurationType": configurationType,
                "initialSoc": initialSoc,
                "maxChargeCurrentOverride": maxChargeCurrentOverride,
                "maxDischargeCurrentOverride": maxDischargeCurrentOverride,
                "minSocOverride": minSocOverride,
                "topology": topology,
                "id": id,
                "packs": packs,
                "current": current,
                "voltage": voltage,
                "power": power,
                "soc": soc,
                "curve": curve,
                "idealMaxChargeCurrent": idealMaxChargeCurrent,
                "maxChargeCurrent": maxChargeCurrent,
                "maxChargeVoltage": maxChargeVoltage,
                "maxChargePower": maxChargePower,
                "idealMaxDischargeCurrent": idealMaxDischargeCurrent,
                "esr": esr,
                "capacity": capacity,
                "minSoc": minSoc,
                "voc": voc,
            }
    
    maxDischargeCurrentOverride: MetaOapg.properties.maxDischargeCurrentOverride
    topology: MetaOapg.properties.topology
    initialSoc: MetaOapg.properties.initialSoc
    minSocOverride: MetaOapg.properties.minSocOverride
    configurationType: MetaOapg.properties.configurationType
    maxChargeCurrentOverride: MetaOapg.properties.maxChargeCurrentOverride
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurationType"]) -> MetaOapg.properties.configurationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialSoc"]) -> MetaOapg.properties.initialSoc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargeCurrentOverride"]) -> MetaOapg.properties.maxChargeCurrentOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDischargeCurrentOverride"]) -> MetaOapg.properties.maxDischargeCurrentOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minSocOverride"]) -> MetaOapg.properties.minSocOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["packs"]) -> MetaOapg.properties.packs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current"]) -> MetaOapg.properties.current: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voltage"]) -> MetaOapg.properties.voltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["power"]) -> MetaOapg.properties.power: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["soc"]) -> MetaOapg.properties.soc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["curve"]) -> MetaOapg.properties.curve: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idealMaxChargeCurrent"]) -> MetaOapg.properties.idealMaxChargeCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargeCurrent"]) -> MetaOapg.properties.maxChargeCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargeVoltage"]) -> MetaOapg.properties.maxChargeVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargePower"]) -> MetaOapg.properties.maxChargePower: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idealMaxDischargeCurrent"]) -> MetaOapg.properties.idealMaxDischargeCurrent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["esr"]) -> MetaOapg.properties.esr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capacity"]) -> MetaOapg.properties.capacity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minSoc"]) -> MetaOapg.properties.minSoc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voc"]) -> MetaOapg.properties.voc: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurationType", "initialSoc", "maxChargeCurrentOverride", "maxDischargeCurrentOverride", "minSocOverride", "topology", "id", "packs", "current", "voltage", "power", "soc", "curve", "idealMaxChargeCurrent", "maxChargeCurrent", "maxChargeVoltage", "maxChargePower", "idealMaxDischargeCurrent", "esr", "capacity", "minSoc", "voc", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurationType"]) -> MetaOapg.properties.configurationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialSoc"]) -> MetaOapg.properties.initialSoc: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargeCurrentOverride"]) -> MetaOapg.properties.maxChargeCurrentOverride: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDischargeCurrentOverride"]) -> MetaOapg.properties.maxDischargeCurrentOverride: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minSocOverride"]) -> MetaOapg.properties.minSocOverride: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["packs"]) -> typing.Union[MetaOapg.properties.packs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current"]) -> typing.Union[MetaOapg.properties.current, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voltage"]) -> typing.Union[MetaOapg.properties.voltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["power"]) -> typing.Union[MetaOapg.properties.power, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["soc"]) -> typing.Union[MetaOapg.properties.soc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["curve"]) -> typing.Union[MetaOapg.properties.curve, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idealMaxChargeCurrent"]) -> typing.Union[MetaOapg.properties.idealMaxChargeCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargeCurrent"]) -> typing.Union[MetaOapg.properties.maxChargeCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargeVoltage"]) -> typing.Union[MetaOapg.properties.maxChargeVoltage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargePower"]) -> typing.Union[MetaOapg.properties.maxChargePower, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idealMaxDischargeCurrent"]) -> typing.Union[MetaOapg.properties.idealMaxDischargeCurrent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["esr"]) -> typing.Union[MetaOapg.properties.esr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capacity"]) -> typing.Union[MetaOapg.properties.capacity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minSoc"]) -> typing.Union[MetaOapg.properties.minSoc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voc"]) -> typing.Union[MetaOapg.properties.voc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurationType", "initialSoc", "maxChargeCurrentOverride", "maxDischargeCurrentOverride", "minSocOverride", "topology", "id", "packs", "current", "voltage", "power", "soc", "curve", "idealMaxChargeCurrent", "maxChargeCurrent", "maxChargeVoltage", "maxChargePower", "idealMaxDischargeCurrent", "esr", "capacity", "minSoc", "voc", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxDischargeCurrentOverride: typing.Union[MetaOapg.properties.maxDischargeCurrentOverride, decimal.Decimal, int, float, ],
        topology: typing.Union[MetaOapg.properties.topology, str, ],
        initialSoc: typing.Union[MetaOapg.properties.initialSoc, decimal.Decimal, int, float, ],
        minSocOverride: typing.Union[MetaOapg.properties.minSocOverride, decimal.Decimal, int, float, ],
        configurationType: typing.Union[MetaOapg.properties.configurationType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        maxChargeCurrentOverride: typing.Union[MetaOapg.properties.maxChargeCurrentOverride, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        packs: typing.Union[MetaOapg.properties.packs, list, tuple, schemas.Unset] = schemas.unset,
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        voltage: typing.Union[MetaOapg.properties.voltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        power: typing.Union[MetaOapg.properties.power, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        soc: typing.Union[MetaOapg.properties.soc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        curve: typing.Union[MetaOapg.properties.curve, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        idealMaxChargeCurrent: typing.Union[MetaOapg.properties.idealMaxChargeCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxChargeCurrent: typing.Union[MetaOapg.properties.maxChargeCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxChargeVoltage: typing.Union[MetaOapg.properties.maxChargeVoltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxChargePower: typing.Union[MetaOapg.properties.maxChargePower, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        idealMaxDischargeCurrent: typing.Union[MetaOapg.properties.idealMaxDischargeCurrent, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        esr: typing.Union[MetaOapg.properties.esr, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        capacity: typing.Union[MetaOapg.properties.capacity, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minSoc: typing.Union[MetaOapg.properties.minSoc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        voc: typing.Union[MetaOapg.properties.voc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Battery':
        return super().__new__(
            cls,
            *_args,
            maxDischargeCurrentOverride=maxDischargeCurrentOverride,
            topology=topology,
            initialSoc=initialSoc,
            minSocOverride=minSocOverride,
            configurationType=configurationType,
            maxChargeCurrentOverride=maxChargeCurrentOverride,
            id=id,
            packs=packs,
            current=current,
            voltage=voltage,
            power=power,
            soc=soc,
            curve=curve,
            idealMaxChargeCurrent=idealMaxChargeCurrent,
            maxChargeCurrent=maxChargeCurrent,
            maxChargeVoltage=maxChargeVoltage,
            maxChargePower=maxChargePower,
            idealMaxDischargeCurrent=idealMaxDischargeCurrent,
            esr=esr,
            capacity=capacity,
            minSoc=minSoc,
            voc=voc,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.configuration_types import ConfigurationTypes
