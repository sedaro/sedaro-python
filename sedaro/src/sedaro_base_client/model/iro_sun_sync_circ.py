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


class IROSunSyncCirc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "initialRefOrbit",
            "nu",
            "alt",
            "mltAscNode",
        }
        
        class properties:
            
            
            class initialRefOrbit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SUN_SYNC_CIRC": "SUN_SYNC_CIRC",
                    }
                
                @schemas.classproperty
                def SUN_SYNC_CIRC(cls):
                    return cls("SUN_SYNC_CIRC")
            mltAscNode = schemas.NumberSchema
            
            
            class nu(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            
            
            class alt(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 100.0
            __annotations__ = {
                "initialRefOrbit": initialRefOrbit,
                "mltAscNode": mltAscNode,
                "nu": nu,
                "alt": alt,
            }
    
    initialRefOrbit: MetaOapg.properties.initialRefOrbit
    nu: MetaOapg.properties.nu
    alt: MetaOapg.properties.alt
    mltAscNode: MetaOapg.properties.mltAscNode
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mltAscNode"]) -> MetaOapg.properties.mltAscNode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "mltAscNode", "nu", "alt", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initialRefOrbit"]) -> MetaOapg.properties.initialRefOrbit: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mltAscNode"]) -> MetaOapg.properties.mltAscNode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nu"]) -> MetaOapg.properties.nu: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["initialRefOrbit", "mltAscNode", "nu", "alt", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        initialRefOrbit: typing.Union[MetaOapg.properties.initialRefOrbit, str, ],
        nu: typing.Union[MetaOapg.properties.nu, decimal.Decimal, int, float, ],
        alt: typing.Union[MetaOapg.properties.alt, decimal.Decimal, int, float, ],
        mltAscNode: typing.Union[MetaOapg.properties.mltAscNode, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IROSunSyncCirc':
        return super().__new__(
            cls,
            *_args,
            initialRefOrbit=initialRefOrbit,
            nu=nu,
            alt=alt,
            mltAscNode=mltAscNode,
            _configuration=_configuration,
            **kwargs,
        )
