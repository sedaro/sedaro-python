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


class OperationalModeCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "pointingMode",
            "name",
            "priority",
            "conOps",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class priority(
                schemas.IntSchema
            ):
                pass
            pointingMode = schemas.StrSchema
            conOps = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class minOccurrenceDuration(
                schemas.NumberSchema
            ):
                pass
            
            
            class maxOccurrenceDuration(
                schemas.NumberSchema
            ):
                pass
            
            
            class minTimeBetweenOccurrences(
                schemas.NumberSchema
            ):
                pass
            
            
            class conditions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'conditions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dataGenerationModes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dataGenerationModes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class activeDataInterfaces(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'activeDataInterfaces':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sameTargetConditionGroupings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sameTargetConditionGroupings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "priority": priority,
                "pointingMode": pointingMode,
                "conOps": conOps,
                "id": id,
                "minOccurrenceDuration": minOccurrenceDuration,
                "maxOccurrenceDuration": maxOccurrenceDuration,
                "minTimeBetweenOccurrences": minTimeBetweenOccurrences,
                "conditions": conditions,
                "dataGenerationModes": dataGenerationModes,
                "activeDataInterfaces": activeDataInterfaces,
                "sameTargetConditionGroupings": sameTargetConditionGroupings,
            }
    
    pointingMode: MetaOapg.properties.pointingMode
    name: MetaOapg.properties.name
    priority: MetaOapg.properties.priority
    conOps: MetaOapg.properties.conOps
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pointingMode"]) -> MetaOapg.properties.pointingMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minOccurrenceDuration"]) -> MetaOapg.properties.minOccurrenceDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxOccurrenceDuration"]) -> MetaOapg.properties.maxOccurrenceDuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minTimeBetweenOccurrences"]) -> MetaOapg.properties.minTimeBetweenOccurrences: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conditions"]) -> MetaOapg.properties.conditions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataGenerationModes"]) -> MetaOapg.properties.dataGenerationModes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeDataInterfaces"]) -> MetaOapg.properties.activeDataInterfaces: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sameTargetConditionGroupings"]) -> MetaOapg.properties.sameTargetConditionGroupings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "priority", "pointingMode", "conOps", "id", "minOccurrenceDuration", "maxOccurrenceDuration", "minTimeBetweenOccurrences", "conditions", "dataGenerationModes", "activeDataInterfaces", "sameTargetConditionGroupings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pointingMode"]) -> MetaOapg.properties.pointingMode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minOccurrenceDuration"]) -> typing.Union[MetaOapg.properties.minOccurrenceDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxOccurrenceDuration"]) -> typing.Union[MetaOapg.properties.maxOccurrenceDuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minTimeBetweenOccurrences"]) -> typing.Union[MetaOapg.properties.minTimeBetweenOccurrences, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conditions"]) -> typing.Union[MetaOapg.properties.conditions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataGenerationModes"]) -> typing.Union[MetaOapg.properties.dataGenerationModes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeDataInterfaces"]) -> typing.Union[MetaOapg.properties.activeDataInterfaces, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sameTargetConditionGroupings"]) -> typing.Union[MetaOapg.properties.sameTargetConditionGroupings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "priority", "pointingMode", "conOps", "id", "minOccurrenceDuration", "maxOccurrenceDuration", "minTimeBetweenOccurrences", "conditions", "dataGenerationModes", "activeDataInterfaces", "sameTargetConditionGroupings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pointingMode: typing.Union[MetaOapg.properties.pointingMode, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, ],
        conOps: typing.Union[MetaOapg.properties.conOps, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        minOccurrenceDuration: typing.Union[MetaOapg.properties.minOccurrenceDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maxOccurrenceDuration: typing.Union[MetaOapg.properties.maxOccurrenceDuration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minTimeBetweenOccurrences: typing.Union[MetaOapg.properties.minTimeBetweenOccurrences, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        conditions: typing.Union[MetaOapg.properties.conditions, list, tuple, schemas.Unset] = schemas.unset,
        dataGenerationModes: typing.Union[MetaOapg.properties.dataGenerationModes, list, tuple, schemas.Unset] = schemas.unset,
        activeDataInterfaces: typing.Union[MetaOapg.properties.activeDataInterfaces, list, tuple, schemas.Unset] = schemas.unset,
        sameTargetConditionGroupings: typing.Union[MetaOapg.properties.sameTargetConditionGroupings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OperationalModeCreate':
        return super().__new__(
            cls,
            *_args,
            pointingMode=pointingMode,
            name=name,
            priority=priority,
            conOps=conOps,
            id=id,
            minOccurrenceDuration=minOccurrenceDuration,
            maxOccurrenceDuration=maxOccurrenceDuration,
            minTimeBetweenOccurrences=minTimeBetweenOccurrences,
            conditions=conditions,
            dataGenerationModes=dataGenerationModes,
            activeDataInterfaces=activeDataInterfaces,
            sameTargetConditionGroupings=sameTargetConditionGroupings,
            _configuration=_configuration,
            **kwargs,
        )
