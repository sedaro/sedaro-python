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


class SpaceTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            conOps = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class targetType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def SPACE_TARGET(cls):
                    return cls("SPACE_TARGET")
            rel_agentId = schemas.StrSchema
            
            
            class conditions_A(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions_A':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class conditions_B(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions_B':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            targetVector = schemas.StrSchema
            
            
            class targetGroups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetGroups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            shadow = schemas.BoolSchema
            lst = schemas.NumberSchema
            position = schemas.AnyTypeSchema
            
            
            class lat(
                schemas.NumberSchema
            ):
                pass
            
            
            class lon(
                schemas.NumberSchema
            ):
                pass
            
            
            class alt(
                schemas.NumberSchema
            ):
                pass
            range = schemas.NumberSchema
            lineOfSight = schemas.BoolSchema
            
            
            class azimuth(
                schemas.NumberSchema
            ):
                pass
            
            
            class elevation(
                schemas.NumberSchema
            ):
                pass
            
            
            class beta(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "conOps": conOps,
                "id": id,
                "targetType": targetType,
                "rel_agentId": rel_agentId,
                "conditions_A": conditions_A,
                "conditions_B": conditions_B,
                "targetVector": targetVector,
                "targetGroups": targetGroups,
                "shadow": shadow,
                "lst": lst,
                "position": position,
                "lat": lat,
                "lon": lon,
                "alt": alt,
                "range": range,
                "lineOfSight": lineOfSight,
                "azimuth": azimuth,
                "elevation": elevation,
                "beta": beta,
            }
    
    name: MetaOapg.properties.name
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetType"]) -> MetaOapg.properties.targetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rel_agentId"]) -> MetaOapg.properties.rel_agentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions_A"]) -> MetaOapg.properties.conditions_A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions_B"]) -> MetaOapg.properties.conditions_B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetVector"]) -> MetaOapg.properties.targetVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroups"]) -> MetaOapg.properties.targetGroups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shadow"]) -> MetaOapg.properties.shadow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lst"]) -> MetaOapg.properties.lst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat"]) -> MetaOapg.properties.lat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lon"]) -> MetaOapg.properties.lon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lineOfSight"]) -> MetaOapg.properties.lineOfSight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["azimuth"]) -> MetaOapg.properties.azimuth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elevation"]) -> MetaOapg.properties.elevation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["beta"]) -> MetaOapg.properties.beta: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "conOps", "id", "targetType", "rel_agentId", "conditions_A", "conditions_B", "targetVector", "targetGroups", "shadow", "lst", "position", "lat", "lon", "alt", "range", "lineOfSight", "azimuth", "elevation", "beta", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetType"]) -> typing.Union[MetaOapg.properties.targetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rel_agentId"]) -> typing.Union[MetaOapg.properties.rel_agentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions_A"]) -> typing.Union[MetaOapg.properties.conditions_A, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions_B"]) -> typing.Union[MetaOapg.properties.conditions_B, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetVector"]) -> typing.Union[MetaOapg.properties.targetVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroups"]) -> typing.Union[MetaOapg.properties.targetGroups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shadow"]) -> typing.Union[MetaOapg.properties.shadow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lst"]) -> typing.Union[MetaOapg.properties.lst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat"]) -> typing.Union[MetaOapg.properties.lat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lon"]) -> typing.Union[MetaOapg.properties.lon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alt"]) -> typing.Union[MetaOapg.properties.alt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> typing.Union[MetaOapg.properties.range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lineOfSight"]) -> typing.Union[MetaOapg.properties.lineOfSight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["azimuth"]) -> typing.Union[MetaOapg.properties.azimuth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elevation"]) -> typing.Union[MetaOapg.properties.elevation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["beta"]) -> typing.Union[MetaOapg.properties.beta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "conOps", "id", "targetType", "rel_agentId", "conditions_A", "conditions_B", "targetVector", "targetGroups", "shadow", "lst", "position", "lat", "lon", "alt", "range", "lineOfSight", "azimuth", "elevation", "beta", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        targetType: typing.Union[MetaOapg.properties.targetType, str, schemas.Unset] = schemas.unset,
        rel_agentId: typing.Union[MetaOapg.properties.rel_agentId, str, schemas.Unset] = schemas.unset,
        conditions_A: typing.Union[MetaOapg.properties.conditions_A, list, tuple, schemas.Unset] = schemas.unset,
        conditions_B: typing.Union[MetaOapg.properties.conditions_B, list, tuple, schemas.Unset] = schemas.unset,
        targetVector: typing.Union[MetaOapg.properties.targetVector, str, schemas.Unset] = schemas.unset,
        targetGroups: typing.Union[MetaOapg.properties.targetGroups, list, tuple, schemas.Unset] = schemas.unset,
        shadow: typing.Union[MetaOapg.properties.shadow, bool, schemas.Unset] = schemas.unset,
        lst: typing.Union[MetaOapg.properties.lst, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lat: typing.Union[MetaOapg.properties.lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lon: typing.Union[MetaOapg.properties.lon, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        alt: typing.Union[MetaOapg.properties.alt, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        range: typing.Union[MetaOapg.properties.range, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lineOfSight: typing.Union[MetaOapg.properties.lineOfSight, bool, schemas.Unset] = schemas.unset,
        azimuth: typing.Union[MetaOapg.properties.azimuth, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        elevation: typing.Union[MetaOapg.properties.elevation, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        beta: typing.Union[MetaOapg.properties.beta, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SpaceTarget':
        return super().__new__(
            cls,
            *_args,
            name=name,
            conOps=conOps,
            id=id,
            targetType=targetType,
            rel_agentId=rel_agentId,
            conditions_A=conditions_A,
            conditions_B=conditions_B,
            targetVector=targetVector,
            targetGroups=targetGroups,
            shadow=shadow,
            lst=lst,
            position=position,
            lat=lat,
            lon=lon,
            alt=alt,
            range=range,
            lineOfSight=lineOfSight,
            azimuth=azimuth,
            elevation=elevation,
            beta=beta,
            _configuration=_configuration,
            **kwargs,
        )
