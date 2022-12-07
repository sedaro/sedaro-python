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


class Agent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 32
            id = schemas.StrSchema
            peripheral = schemas.BoolSchema
            targetMapping = schemas.DictSchema
            differentiatingState = schemas.DictSchema
            templateRef = schemas.IntSchema
            orbit = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "id": id,
                "peripheral": peripheral,
                "targetMapping": targetMapping,
                "differentiatingState": differentiatingState,
                "templateRef": templateRef,
                "orbit": orbit,
            }
    
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
    def __getitem__(self, name: typing_extensions.Literal["differentiatingState"]) -> MetaOapg.properties.differentiatingState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templateRef"]) -> MetaOapg.properties.templateRef: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orbit"]) -> MetaOapg.properties.orbit: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "id", "peripheral", "targetMapping", "differentiatingState", "templateRef", "orbit", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["differentiatingState"]) -> typing.Union[MetaOapg.properties.differentiatingState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templateRef"]) -> typing.Union[MetaOapg.properties.templateRef, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orbit"]) -> typing.Union[MetaOapg.properties.orbit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "id", "peripheral", "targetMapping", "differentiatingState", "templateRef", "orbit", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        peripheral: typing.Union[MetaOapg.properties.peripheral, bool, schemas.Unset] = schemas.unset,
        targetMapping: typing.Union[MetaOapg.properties.targetMapping, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        differentiatingState: typing.Union[MetaOapg.properties.differentiatingState, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        templateRef: typing.Union[MetaOapg.properties.templateRef, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        orbit: typing.Union[MetaOapg.properties.orbit, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Agent':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            peripheral=peripheral,
            targetMapping=targetMapping,
            differentiatingState=differentiatingState,
            templateRef=templateRef,
            orbit=orbit,
            _configuration=_configuration,
            **kwargs,
        )
