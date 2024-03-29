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


class Agent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A Agent Block
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            id = schemas.StrSchema
            peripheral = schemas.BoolSchema
            targetMapping = schemas.DictSchema
            targetGroupMapping = schemas.DictSchema
            differentiatingState = schemas.DictSchema
            templateRef = schemas.StrSchema
            orbit = schemas.StrSchema
            path = schemas.StrSchema
            
            
            class externalState(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'externalState':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AGENT(cls):
                    return cls("Agent")
            __annotations__ = {
                "name": name,
                "id": id,
                "peripheral": peripheral,
                "targetMapping": targetMapping,
                "targetGroupMapping": targetGroupMapping,
                "differentiatingState": differentiatingState,
                "templateRef": templateRef,
                "orbit": orbit,
                "path": path,
                "externalState": externalState,
                "type": type,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["peripheral"]) -> MetaOapg.properties.peripheral: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetMapping"]) -> MetaOapg.properties.targetMapping: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroupMapping"]) -> MetaOapg.properties.targetGroupMapping: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["differentiatingState"]) -> MetaOapg.properties.differentiatingState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateRef"]) -> MetaOapg.properties.templateRef: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orbit"]) -> MetaOapg.properties.orbit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["externalState"]) -> MetaOapg.properties.externalState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["peripheral"], typing_extensions.Literal["targetMapping"], typing_extensions.Literal["targetGroupMapping"], typing_extensions.Literal["differentiatingState"], typing_extensions.Literal["templateRef"], typing_extensions.Literal["orbit"], typing_extensions.Literal["path"], typing_extensions.Literal["externalState"], typing_extensions.Literal["type"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["peripheral"]) -> typing.Union[MetaOapg.properties.peripheral, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetMapping"]) -> typing.Union[MetaOapg.properties.targetMapping, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroupMapping"]) -> typing.Union[MetaOapg.properties.targetGroupMapping, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["differentiatingState"]) -> typing.Union[MetaOapg.properties.differentiatingState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateRef"]) -> typing.Union[MetaOapg.properties.templateRef, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orbit"]) -> typing.Union[MetaOapg.properties.orbit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["externalState"]) -> typing.Union[MetaOapg.properties.externalState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["peripheral"], typing_extensions.Literal["targetMapping"], typing_extensions.Literal["targetGroupMapping"], typing_extensions.Literal["differentiatingState"], typing_extensions.Literal["templateRef"], typing_extensions.Literal["orbit"], typing_extensions.Literal["path"], typing_extensions.Literal["externalState"], typing_extensions.Literal["type"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        peripheral: typing.Union[MetaOapg.properties.peripheral, bool, schemas.Unset] = schemas.unset,
        targetMapping: typing.Union[MetaOapg.properties.targetMapping, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        targetGroupMapping: typing.Union[MetaOapg.properties.targetGroupMapping, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        differentiatingState: typing.Union[MetaOapg.properties.differentiatingState, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        templateRef: typing.Union[MetaOapg.properties.templateRef, str, schemas.Unset] = schemas.unset,
        orbit: typing.Union[MetaOapg.properties.orbit, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        externalState: typing.Union[MetaOapg.properties.externalState, list, tuple, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Agent':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            peripheral=peripheral,
            targetMapping=targetMapping,
            targetGroupMapping=targetGroupMapping,
            differentiatingState=differentiatingState,
            templateRef=templateRef,
            orbit=orbit,
            path=path,
            externalState=externalState,
            type=type,
            _configuration=_configuration,
        )
