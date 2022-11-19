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


class BatteryUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "maxDischargeCurrentOverride",
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
            __annotations__ = {
                "configurationType": configurationType,
                "initialSoc": initialSoc,
                "maxChargeCurrentOverride": maxChargeCurrentOverride,
                "maxDischargeCurrentOverride": maxDischargeCurrentOverride,
                "minSocOverride": minSocOverride,
            }
    
    maxDischargeCurrentOverride: MetaOapg.properties.maxDischargeCurrentOverride
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["configurationType", "initialSoc", "maxChargeCurrentOverride", "maxDischargeCurrentOverride", "minSocOverride", ], str]):
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["configurationType", "initialSoc", "maxChargeCurrentOverride", "maxDischargeCurrentOverride", "minSocOverride", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxDischargeCurrentOverride: typing.Union[MetaOapg.properties.maxDischargeCurrentOverride, decimal.Decimal, int, float, ],
        initialSoc: typing.Union[MetaOapg.properties.initialSoc, decimal.Decimal, int, float, ],
        minSocOverride: typing.Union[MetaOapg.properties.minSocOverride, decimal.Decimal, int, float, ],
        configurationType: typing.Union[MetaOapg.properties.configurationType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        maxChargeCurrentOverride: typing.Union[MetaOapg.properties.maxChargeCurrentOverride, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatteryUpdate':
        return super().__new__(
            cls,
            *_args,
            maxDischargeCurrentOverride=maxDischargeCurrentOverride,
            initialSoc=initialSoc,
            minSocOverride=minSocOverride,
            configurationType=configurationType,
            maxChargeCurrentOverride=maxChargeCurrentOverride,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.configuration_types import ConfigurationTypes
