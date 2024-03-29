# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.7.0
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


class InternalDataInterface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A InternalDataInterface Block
    """


    class MetaOapg:
        required = {
            "onBitRate",
            "name",
            "alwaysActive",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            onBitRate = schemas.NumberSchema
            alwaysActive = schemas.BoolSchema
            id = schemas.StrSchema
            dataType = schemas.StrSchema
            
            
            class opModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'opModes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            source = schemas.StrSchema
            sink = schemas.StrSchema
            
            
            class bitRate(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            isActive = schemas.BoolSchema
            bus = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "InternalDataInterface": "INTERNAL_DATA_INTERFACE",
                    }
                
                @schemas.classproperty
                def INTERNAL_DATA_INTERFACE(cls):
                    return cls("InternalDataInterface")
            __annotations__ = {
                "name": name,
                "onBitRate": onBitRate,
                "alwaysActive": alwaysActive,
                "id": id,
                "dataType": dataType,
                "opModes": opModes,
                "source": source,
                "sink": sink,
                "bitRate": bitRate,
                "isActive": isActive,
                "bus": bus,
                "type": type,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    onBitRate: MetaOapg.properties.onBitRate
    name: MetaOapg.properties.name
    alwaysActive: MetaOapg.properties.alwaysActive
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onBitRate"]) -> MetaOapg.properties.onBitRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alwaysActive"]) -> MetaOapg.properties.alwaysActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataType"]) -> MetaOapg.properties.dataType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["opModes"]) -> MetaOapg.properties.opModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sink"]) -> MetaOapg.properties.sink: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bitRate"]) -> MetaOapg.properties.bitRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bus"]) -> MetaOapg.properties.bus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["onBitRate"], typing_extensions.Literal["name"], typing_extensions.Literal["alwaysActive"], typing_extensions.Literal["id"], typing_extensions.Literal["dataType"], typing_extensions.Literal["opModes"], typing_extensions.Literal["source"], typing_extensions.Literal["sink"], typing_extensions.Literal["bitRate"], typing_extensions.Literal["isActive"], typing_extensions.Literal["bus"], typing_extensions.Literal["type"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onBitRate"]) -> MetaOapg.properties.onBitRate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alwaysActive"]) -> MetaOapg.properties.alwaysActive: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataType"]) -> typing.Union[MetaOapg.properties.dataType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["opModes"]) -> typing.Union[MetaOapg.properties.opModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sink"]) -> typing.Union[MetaOapg.properties.sink, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bitRate"]) -> typing.Union[MetaOapg.properties.bitRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bus"]) -> typing.Union[MetaOapg.properties.bus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["onBitRate"], typing_extensions.Literal["name"], typing_extensions.Literal["alwaysActive"], typing_extensions.Literal["id"], typing_extensions.Literal["dataType"], typing_extensions.Literal["opModes"], typing_extensions.Literal["source"], typing_extensions.Literal["sink"], typing_extensions.Literal["bitRate"], typing_extensions.Literal["isActive"], typing_extensions.Literal["bus"], typing_extensions.Literal["type"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        onBitRate: typing.Union[MetaOapg.properties.onBitRate, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        alwaysActive: typing.Union[MetaOapg.properties.alwaysActive, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        dataType: typing.Union[MetaOapg.properties.dataType, str, schemas.Unset] = schemas.unset,
        opModes: typing.Union[MetaOapg.properties.opModes, list, tuple, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        sink: typing.Union[MetaOapg.properties.sink, str, schemas.Unset] = schemas.unset,
        bitRate: typing.Union[MetaOapg.properties.bitRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        bus: typing.Union[MetaOapg.properties.bus, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'InternalDataInterface':
        return super().__new__(
            cls,
            *_args,
            onBitRate=onBitRate,
            name=name,
            alwaysActive=alwaysActive,
            id=id,
            dataType=dataType,
            opModes=opModes,
            source=source,
            sink=sink,
            bitRate=bitRate,
            isActive=isActive,
            bus=bus,
            type=type,
            _configuration=_configuration,
        )
