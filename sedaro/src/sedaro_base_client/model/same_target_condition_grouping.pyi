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


class SameTargetConditionGrouping(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "operationalMode",
            "targetGroup",
            "name",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            conOps = schemas.StrSchema
            operationalMode = schemas.StrSchema
            targetGroup = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class targetGroupConditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetGroupConditions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            compliance = schemas.BoolSchema
            
            
            class targetCompliance(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.BoolSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, bool, ],
                ) -> 'targetCompliance':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "conOps": conOps,
                "operationalMode": operationalMode,
                "targetGroup": targetGroup,
                "id": id,
                "targetGroupConditions": targetGroupConditions,
                "compliance": compliance,
                "targetCompliance": targetCompliance,
            }
    
    operationalMode: MetaOapg.properties.operationalMode
    targetGroup: MetaOapg.properties.targetGroup
    name: MetaOapg.properties.name
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operationalMode"]) -> MetaOapg.properties.operationalMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroup"]) -> MetaOapg.properties.targetGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroupConditions"]) -> MetaOapg.properties.targetGroupConditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compliance"]) -> MetaOapg.properties.compliance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetCompliance"]) -> MetaOapg.properties.targetCompliance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "conOps", "operationalMode", "targetGroup", "id", "targetGroupConditions", "compliance", "targetCompliance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operationalMode"]) -> MetaOapg.properties.operationalMode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroup"]) -> MetaOapg.properties.targetGroup: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroupConditions"]) -> typing.Union[MetaOapg.properties.targetGroupConditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compliance"]) -> typing.Union[MetaOapg.properties.compliance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetCompliance"]) -> typing.Union[MetaOapg.properties.targetCompliance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "conOps", "operationalMode", "targetGroup", "id", "targetGroupConditions", "compliance", "targetCompliance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        operationalMode: typing.Union[MetaOapg.properties.operationalMode, str, ],
        targetGroup: typing.Union[MetaOapg.properties.targetGroup, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        targetGroupConditions: typing.Union[MetaOapg.properties.targetGroupConditions, list, tuple, schemas.Unset] = schemas.unset,
        compliance: typing.Union[MetaOapg.properties.compliance, bool, schemas.Unset] = schemas.unset,
        targetCompliance: typing.Union[MetaOapg.properties.targetCompliance, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SameTargetConditionGrouping':
        return super().__new__(
            cls,
            *_args,
            operationalMode=operationalMode,
            targetGroup=targetGroup,
            name=name,
            conOps=conOps,
            id=id,
            targetGroupConditions=targetGroupConditions,
            compliance=compliance,
            targetCompliance=targetCompliance,
            _configuration=_configuration,
            **kwargs,
        )
