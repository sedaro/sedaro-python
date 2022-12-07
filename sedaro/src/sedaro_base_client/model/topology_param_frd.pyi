# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.1
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


class TopologyParamFRD(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "drivenControllerBusVoltage",
            "bcrEfficiency",
            "chargeDiodeDrop",
            "bdrEfficiency",
            "outputPowerRating",
        }
        
        class properties:
            
            
            class bcrEfficiency(
                schemas.NumberSchema
            ):
                pass
            
            
            class outputPowerRating(
                schemas.NumberSchema
            ):
                pass
            
            
            class chargeDiodeDrop(
                schemas.NumberSchema
            ):
                pass
            
            
            class bdrEfficiency(
                schemas.NumberSchema
            ):
                pass
            
            
            class drivenControllerBusVoltage(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "bcrEfficiency": bcrEfficiency,
                "outputPowerRating": outputPowerRating,
                "chargeDiodeDrop": chargeDiodeDrop,
                "bdrEfficiency": bdrEfficiency,
                "drivenControllerBusVoltage": drivenControllerBusVoltage,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    drivenControllerBusVoltage: MetaOapg.properties.drivenControllerBusVoltage
    bcrEfficiency: MetaOapg.properties.bcrEfficiency
    chargeDiodeDrop: MetaOapg.properties.chargeDiodeDrop
    bdrEfficiency: MetaOapg.properties.bdrEfficiency
    outputPowerRating: MetaOapg.properties.outputPowerRating
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["drivenControllerBusVoltage"]) -> MetaOapg.properties.drivenControllerBusVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeDiodeDrop"]) -> MetaOapg.properties.chargeDiodeDrop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bdrEfficiency"]) -> MetaOapg.properties.bdrEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["drivenControllerBusVoltage"], typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeDiodeDrop"], typing_extensions.Literal["bdrEfficiency"], typing_extensions.Literal["outputPowerRating"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["drivenControllerBusVoltage"]) -> MetaOapg.properties.drivenControllerBusVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeDiodeDrop"]) -> MetaOapg.properties.chargeDiodeDrop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bdrEfficiency"]) -> MetaOapg.properties.bdrEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["drivenControllerBusVoltage"], typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeDiodeDrop"], typing_extensions.Literal["bdrEfficiency"], typing_extensions.Literal["outputPowerRating"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        drivenControllerBusVoltage: typing.Union[MetaOapg.properties.drivenControllerBusVoltage, decimal.Decimal, int, float, ],
        bcrEfficiency: typing.Union[MetaOapg.properties.bcrEfficiency, decimal.Decimal, int, float, ],
        chargeDiodeDrop: typing.Union[MetaOapg.properties.chargeDiodeDrop, decimal.Decimal, int, float, ],
        bdrEfficiency: typing.Union[MetaOapg.properties.bdrEfficiency, decimal.Decimal, int, float, ],
        outputPowerRating: typing.Union[MetaOapg.properties.outputPowerRating, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TopologyParamFRD':
        return super().__new__(
            cls,
            *_args,
            drivenControllerBusVoltage=drivenControllerBusVoltage,
            bcrEfficiency=bcrEfficiency,
            chargeDiodeDrop=chargeDiodeDrop,
            bdrEfficiency=bdrEfficiency,
            outputPowerRating=outputPowerRating,
            _configuration=_configuration,
        )
