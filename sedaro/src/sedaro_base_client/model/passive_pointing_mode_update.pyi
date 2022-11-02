# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).   # noqa: E501

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


class PassivePointingModeUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "pointingModeType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class pointingModeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PASSIVE(cls):
                    return cls("PASSIVE")
            id = schemas.StrSchema
            
            
            class operationalModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'operationalModes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            odAlgorithm = schemas.StrSchema
            adAlgorithm = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "pointingModeType": pointingModeType,
                "id": id,
                "operationalModes": operationalModes,
                "odAlgorithm": odAlgorithm,
                "adAlgorithm": adAlgorithm,
            }
    
    name: MetaOapg.properties.name
    pointingModeType: MetaOapg.properties.pointingModeType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalModes"]) -> MetaOapg.properties.operationalModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["odAlgorithm"]) -> MetaOapg.properties.odAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adAlgorithm"]) -> MetaOapg.properties.adAlgorithm: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "id", "operationalModes", "odAlgorithm", "adAlgorithm", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingModeType"]) -> MetaOapg.properties.pointingModeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalModes"]) -> typing.Union[MetaOapg.properties.operationalModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["odAlgorithm"]) -> typing.Union[MetaOapg.properties.odAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adAlgorithm"]) -> typing.Union[MetaOapg.properties.adAlgorithm, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "pointingModeType", "id", "operationalModes", "odAlgorithm", "adAlgorithm", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        pointingModeType: typing.Union[MetaOapg.properties.pointingModeType, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        operationalModes: typing.Union[MetaOapg.properties.operationalModes, list, tuple, schemas.Unset] = schemas.unset,
        odAlgorithm: typing.Union[MetaOapg.properties.odAlgorithm, str, schemas.Unset] = schemas.unset,
        adAlgorithm: typing.Union[MetaOapg.properties.adAlgorithm, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PassivePointingModeUpdate':
        return super().__new__(
            cls,
            *args,
            name=name,
            pointingModeType=pointingModeType,
            id=id,
            operationalModes=operationalModes,
            odAlgorithm=odAlgorithm,
            adAlgorithm=adAlgorithm,
            _configuration=_configuration,
            **kwargs,
        )
