# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.4
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


class PIDAlgorithm(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited only by `Collection` and `Block`. Adds helper methods that help with
relationship fields.
    """


    class MetaOapg:
        required = {
            "algorithmType",
            "gainI",
            "rate",
            "gainP",
            "name",
            "algorithmSubtype",
            "gainD",
            "gainC",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            rate = schemas.NumberSchema
            
            
            class algorithmType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ATTITUDE_CONTROL": "ATTITUDE_CONTROL",
                    }
                
                @schemas.classproperty
                def ATTITUDE_CONTROL(cls):
                    return cls("ATTITUDE_CONTROL")
            
            
            class algorithmSubtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PID": "PID",
                    }
                
                @schemas.classproperty
                def PID(cls):
                    return cls("PID")
            
            
            class gainP(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class gainI(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class gainD(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class gainC(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            id = schemas.StrSchema
            satellite = schemas.StrSchema
            
            
            class actuators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actuators':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class reactionWheelCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reactionWheelCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class magnetorquerCommands(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'magnetorquerCommands':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class errorIntegral(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'errorIntegral':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "rate": rate,
                "algorithmType": algorithmType,
                "algorithmSubtype": algorithmSubtype,
                "gainP": gainP,
                "gainI": gainI,
                "gainD": gainD,
                "gainC": gainC,
                "id": id,
                "satellite": satellite,
                "actuators": actuators,
                "reactionWheelCommands": reactionWheelCommands,
                "magnetorquerCommands": magnetorquerCommands,
                "errorIntegral": errorIntegral,
            }
    
    algorithmType: MetaOapg.properties.algorithmType
    gainI: MetaOapg.properties.gainI
    rate: MetaOapg.properties.rate
    gainP: MetaOapg.properties.gainP
    name: MetaOapg.properties.name
    algorithmSubtype: MetaOapg.properties.algorithmSubtype
    gainD: MetaOapg.properties.gainD
    gainC: MetaOapg.properties.gainC
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainP"]) -> MetaOapg.properties.gainP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainI"]) -> MetaOapg.properties.gainI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainD"]) -> MetaOapg.properties.gainD: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actuators"]) -> MetaOapg.properties.actuators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> MetaOapg.properties.reactionWheelCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> MetaOapg.properties.magnetorquerCommands: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorIntegral"]) -> MetaOapg.properties.errorIntegral: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "gainP", "gainI", "gainD", "gainC", "id", "satellite", "actuators", "reactionWheelCommands", "magnetorquerCommands", "errorIntegral", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainP"]) -> MetaOapg.properties.gainP: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainI"]) -> MetaOapg.properties.gainI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainD"]) -> MetaOapg.properties.gainD: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actuators"]) -> typing.Union[MetaOapg.properties.actuators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reactionWheelCommands"]) -> typing.Union[MetaOapg.properties.reactionWheelCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["magnetorquerCommands"]) -> typing.Union[MetaOapg.properties.magnetorquerCommands, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorIntegral"]) -> typing.Union[MetaOapg.properties.errorIntegral, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "rate", "algorithmType", "algorithmSubtype", "gainP", "gainI", "gainD", "gainC", "id", "satellite", "actuators", "reactionWheelCommands", "magnetorquerCommands", "errorIntegral", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        algorithmType: typing.Union[MetaOapg.properties.algorithmType, str, ],
        gainI: typing.Union[MetaOapg.properties.gainI, decimal.Decimal, int, float, ],
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, ],
        gainP: typing.Union[MetaOapg.properties.gainP, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        algorithmSubtype: typing.Union[MetaOapg.properties.algorithmSubtype, str, ],
        gainD: typing.Union[MetaOapg.properties.gainD, decimal.Decimal, int, float, ],
        gainC: typing.Union[MetaOapg.properties.gainC, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        actuators: typing.Union[MetaOapg.properties.actuators, list, tuple, schemas.Unset] = schemas.unset,
        reactionWheelCommands: typing.Union[MetaOapg.properties.reactionWheelCommands, list, tuple, schemas.Unset] = schemas.unset,
        magnetorquerCommands: typing.Union[MetaOapg.properties.magnetorquerCommands, list, tuple, schemas.Unset] = schemas.unset,
        errorIntegral: typing.Union[MetaOapg.properties.errorIntegral, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PIDAlgorithm':
        return super().__new__(
            cls,
            *_args,
            algorithmType=algorithmType,
            gainI=gainI,
            rate=rate,
            gainP=gainP,
            name=name,
            algorithmSubtype=algorithmSubtype,
            gainD=gainD,
            gainC=gainC,
            id=id,
            satellite=satellite,
            actuators=actuators,
            reactionWheelCommands=reactionWheelCommands,
            magnetorquerCommands=magnetorquerCommands,
            errorIntegral=errorIntegral,
            _configuration=_configuration,
            **kwargs,
        )
