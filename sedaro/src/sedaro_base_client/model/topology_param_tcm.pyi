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


class TopologyParamTCM(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "pptEfficiency",
            "bcrEfficiency",
            "chargeControllerBusVoltage",
            "dischargeDiodeDrop",
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
            
            
            class dischargeDiodeDrop(
                schemas.NumberSchema
            ):
                pass
            
            
            class chargeControllerBusVoltage(
                schemas.NumberSchema
            ):
                pass
            
            
            class pptEfficiency(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "bcrEfficiency": bcrEfficiency,
                "outputPowerRating": outputPowerRating,
                "dischargeDiodeDrop": dischargeDiodeDrop,
                "chargeControllerBusVoltage": chargeControllerBusVoltage,
                "pptEfficiency": pptEfficiency,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    pptEfficiency: MetaOapg.properties.pptEfficiency
    bcrEfficiency: MetaOapg.properties.bcrEfficiency
    chargeControllerBusVoltage: MetaOapg.properties.chargeControllerBusVoltage
    dischargeDiodeDrop: MetaOapg.properties.dischargeDiodeDrop
    outputPowerRating: MetaOapg.properties.outputPowerRating
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pptEfficiency"]) -> MetaOapg.properties.pptEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chargeControllerBusVoltage"]) -> MetaOapg.properties.chargeControllerBusVoltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dischargeDiodeDrop"]) -> MetaOapg.properties.dischargeDiodeDrop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pptEfficiency"], typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeControllerBusVoltage"], typing_extensions.Literal["dischargeDiodeDrop"], typing_extensions.Literal["outputPowerRating"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pptEfficiency"]) -> MetaOapg.properties.pptEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bcrEfficiency"]) -> MetaOapg.properties.bcrEfficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chargeControllerBusVoltage"]) -> MetaOapg.properties.chargeControllerBusVoltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dischargeDiodeDrop"]) -> MetaOapg.properties.dischargeDiodeDrop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputPowerRating"]) -> MetaOapg.properties.outputPowerRating: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pptEfficiency"], typing_extensions.Literal["bcrEfficiency"], typing_extensions.Literal["chargeControllerBusVoltage"], typing_extensions.Literal["dischargeDiodeDrop"], typing_extensions.Literal["outputPowerRating"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pptEfficiency: typing.Union[MetaOapg.properties.pptEfficiency, decimal.Decimal, int, float, ],
        bcrEfficiency: typing.Union[MetaOapg.properties.bcrEfficiency, decimal.Decimal, int, float, ],
        chargeControllerBusVoltage: typing.Union[MetaOapg.properties.chargeControllerBusVoltage, decimal.Decimal, int, float, ],
        dischargeDiodeDrop: typing.Union[MetaOapg.properties.dischargeDiodeDrop, decimal.Decimal, int, float, ],
        outputPowerRating: typing.Union[MetaOapg.properties.outputPowerRating, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TopologyParamTCM':
        return super().__new__(
            cls,
            *_args,
            pptEfficiency=pptEfficiency,
            bcrEfficiency=bcrEfficiency,
            chargeControllerBusVoltage=chargeControllerBusVoltage,
            dischargeDiodeDrop=dischargeDiodeDrop,
            outputPowerRating=outputPowerRating,
            _configuration=_configuration,
        )
