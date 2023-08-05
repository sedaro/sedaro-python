# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.5.2
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

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "configurationType",
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
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "": "EMPTY",
                            }
                        
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
            id = schemas.StrSchema
            
            
            class initialSoc(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            
            
            class maxChargeCurrentOverride(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class maxDischargeCurrentOverride(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class minSocOverride(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            powerProcessor = schemas.StrSchema
            
            
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
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            
            
            class curve(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 2
                    min_items = 2
                    
                    @staticmethod
                    def items() -> typing.Type['Items']:
                        return Items
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Items'], typing.List['Items']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'curve':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Items':
                    return super().__getitem__(i)
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
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
                    inclusive_minimum = 0.0
            voc = schemas.NumberSchema
            __annotations__ = {
                "configurationType": configurationType,
                "id": id,
                "initialSoc": initialSoc,
                "maxChargeCurrentOverride": maxChargeCurrentOverride,
                "maxDischargeCurrentOverride": maxDischargeCurrentOverride,
                "minSocOverride": minSocOverride,
                "powerProcessor": powerProcessor,
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
        additional_properties = schemas.NotAnyTypeSchema
    
    configurationType: MetaOapg.properties.configurationType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configurationType"]) -> MetaOapg.properties.configurationType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialSoc"]) -> MetaOapg.properties.initialSoc: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxChargeCurrentOverride"]) -> MetaOapg.properties.maxChargeCurrentOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxDischargeCurrentOverride"]) -> MetaOapg.properties.maxDischargeCurrentOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minSocOverride"]) -> MetaOapg.properties.minSocOverride: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerProcessor"]) -> MetaOapg.properties.powerProcessor: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurationType"], typing_extensions.Literal["id"], typing_extensions.Literal["initialSoc"], typing_extensions.Literal["maxChargeCurrentOverride"], typing_extensions.Literal["maxDischargeCurrentOverride"], typing_extensions.Literal["minSocOverride"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["packs"], typing_extensions.Literal["current"], typing_extensions.Literal["voltage"], typing_extensions.Literal["power"], typing_extensions.Literal["soc"], typing_extensions.Literal["curve"], typing_extensions.Literal["idealMaxChargeCurrent"], typing_extensions.Literal["maxChargeCurrent"], typing_extensions.Literal["maxChargeVoltage"], typing_extensions.Literal["maxChargePower"], typing_extensions.Literal["idealMaxDischargeCurrent"], typing_extensions.Literal["esr"], typing_extensions.Literal["capacity"], typing_extensions.Literal["minSoc"], typing_extensions.Literal["voc"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configurationType"]) -> MetaOapg.properties.configurationType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialSoc"]) -> typing.Union[MetaOapg.properties.initialSoc, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxChargeCurrentOverride"]) -> typing.Union[MetaOapg.properties.maxChargeCurrentOverride, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxDischargeCurrentOverride"]) -> typing.Union[MetaOapg.properties.maxDischargeCurrentOverride, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minSocOverride"]) -> typing.Union[MetaOapg.properties.minSocOverride, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerProcessor"]) -> typing.Union[MetaOapg.properties.powerProcessor, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurationType"], typing_extensions.Literal["id"], typing_extensions.Literal["initialSoc"], typing_extensions.Literal["maxChargeCurrentOverride"], typing_extensions.Literal["maxDischargeCurrentOverride"], typing_extensions.Literal["minSocOverride"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["packs"], typing_extensions.Literal["current"], typing_extensions.Literal["voltage"], typing_extensions.Literal["power"], typing_extensions.Literal["soc"], typing_extensions.Literal["curve"], typing_extensions.Literal["idealMaxChargeCurrent"], typing_extensions.Literal["maxChargeCurrent"], typing_extensions.Literal["maxChargeVoltage"], typing_extensions.Literal["maxChargePower"], typing_extensions.Literal["idealMaxDischargeCurrent"], typing_extensions.Literal["esr"], typing_extensions.Literal["capacity"], typing_extensions.Literal["minSoc"], typing_extensions.Literal["voc"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        configurationType: typing.Union[MetaOapg.properties.configurationType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        initialSoc: typing.Union[MetaOapg.properties.initialSoc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxChargeCurrentOverride: typing.Union[MetaOapg.properties.maxChargeCurrentOverride, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxDischargeCurrentOverride: typing.Union[MetaOapg.properties.maxDischargeCurrentOverride, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minSocOverride: typing.Union[MetaOapg.properties.minSocOverride, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        powerProcessor: typing.Union[MetaOapg.properties.powerProcessor, str, schemas.Unset] = schemas.unset,
        packs: typing.Union[MetaOapg.properties.packs, list, tuple, schemas.Unset] = schemas.unset,
        current: typing.Union[MetaOapg.properties.current, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        voltage: typing.Union[MetaOapg.properties.voltage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        power: typing.Union[MetaOapg.properties.power, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        soc: typing.Union[MetaOapg.properties.soc, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        curve: typing.Union[MetaOapg.properties.curve, list, tuple, schemas.Unset] = schemas.unset,
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
    ) -> 'Battery':
        return super().__new__(
            cls,
            *_args,
            configurationType=configurationType,
            id=id,
            initialSoc=initialSoc,
            maxChargeCurrentOverride=maxChargeCurrentOverride,
            maxDischargeCurrentOverride=maxDischargeCurrentOverride,
            minSocOverride=minSocOverride,
            powerProcessor=powerProcessor,
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
        )

from sedaro_base_client.model.configuration_types import ConfigurationTypes
from sedaro_base_client.model.items import Items
