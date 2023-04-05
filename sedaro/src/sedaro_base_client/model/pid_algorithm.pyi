# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.7
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

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "algorithmType",
            "gainI",
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
                pass
            
            
            class algorithmType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ATTITUDE_CONTROL(cls):
                    return cls("ATTITUDE_CONTROL")
            
            
            class algorithmSubtype(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PID(cls):
                    return cls("PID")
            
            
            class gainP(
                schemas.NumberSchema
            ):
                pass
            
            
            class gainI(
                schemas.NumberSchema
            ):
                pass
            
            
            class gainD(
                schemas.NumberSchema
            ):
                pass
            
            
            class gainC(
                schemas.NumberSchema
            ):
                pass
            id = schemas.StrSchema
        
            @staticmethod
            def metamodel() -> typing.Type['Metamodel']:
                return Metamodel
            rate = schemas.NumberSchema
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
                "algorithmType": algorithmType,
                "algorithmSubtype": algorithmSubtype,
                "gainP": gainP,
                "gainI": gainI,
                "gainD": gainD,
                "gainC": gainC,
                "id": id,
                "metamodel": metamodel,
                "rate": rate,
                "satellite": satellite,
                "actuators": actuators,
                "reactionWheelCommands": reactionWheelCommands,
                "magnetorquerCommands": magnetorquerCommands,
                "errorIntegral": errorIntegral,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    algorithmType: MetaOapg.properties.algorithmType
    gainI: MetaOapg.properties.gainI
    gainP: MetaOapg.properties.gainP
    name: MetaOapg.properties.name
    algorithmSubtype: MetaOapg.properties.algorithmSubtype
    gainD: MetaOapg.properties.gainD
    gainC: MetaOapg.properties.gainC
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainI"]) -> MetaOapg.properties.gainI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainP"]) -> MetaOapg.properties.gainP: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainD"]) -> MetaOapg.properties.gainD: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metamodel"]) -> 'Metamodel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
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
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["algorithmType"], typing_extensions.Literal["gainI"], typing_extensions.Literal["gainP"], typing_extensions.Literal["name"], typing_extensions.Literal["algorithmSubtype"], typing_extensions.Literal["gainD"], typing_extensions.Literal["gainC"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["rate"], typing_extensions.Literal["satellite"], typing_extensions.Literal["actuators"], typing_extensions.Literal["reactionWheelCommands"], typing_extensions.Literal["magnetorquerCommands"], typing_extensions.Literal["errorIntegral"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmType"]) -> MetaOapg.properties.algorithmType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainI"]) -> MetaOapg.properties.gainI: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainP"]) -> MetaOapg.properties.gainP: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["algorithmSubtype"]) -> MetaOapg.properties.algorithmSubtype: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainD"]) -> MetaOapg.properties.gainD: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gainC"]) -> MetaOapg.properties.gainC: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metamodel"]) -> typing.Union['Metamodel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> typing.Union[MetaOapg.properties.rate, schemas.Unset]: ...
    
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
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["algorithmType"], typing_extensions.Literal["gainI"], typing_extensions.Literal["gainP"], typing_extensions.Literal["name"], typing_extensions.Literal["algorithmSubtype"], typing_extensions.Literal["gainD"], typing_extensions.Literal["gainC"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["rate"], typing_extensions.Literal["satellite"], typing_extensions.Literal["actuators"], typing_extensions.Literal["reactionWheelCommands"], typing_extensions.Literal["magnetorquerCommands"], typing_extensions.Literal["errorIntegral"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        algorithmType: typing.Union[MetaOapg.properties.algorithmType, str, ],
        gainI: typing.Union[MetaOapg.properties.gainI, decimal.Decimal, int, float, ],
        gainP: typing.Union[MetaOapg.properties.gainP, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        algorithmSubtype: typing.Union[MetaOapg.properties.algorithmSubtype, str, ],
        gainD: typing.Union[MetaOapg.properties.gainD, decimal.Decimal, int, float, ],
        gainC: typing.Union[MetaOapg.properties.gainC, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metamodel: typing.Union['Metamodel', schemas.Unset] = schemas.unset,
        rate: typing.Union[MetaOapg.properties.rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        actuators: typing.Union[MetaOapg.properties.actuators, list, tuple, schemas.Unset] = schemas.unset,
        reactionWheelCommands: typing.Union[MetaOapg.properties.reactionWheelCommands, list, tuple, schemas.Unset] = schemas.unset,
        magnetorquerCommands: typing.Union[MetaOapg.properties.magnetorquerCommands, list, tuple, schemas.Unset] = schemas.unset,
        errorIntegral: typing.Union[MetaOapg.properties.errorIntegral, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PIDAlgorithm':
        return super().__new__(
            cls,
            *_args,
            algorithmType=algorithmType,
            gainI=gainI,
            gainP=gainP,
            name=name,
            algorithmSubtype=algorithmSubtype,
            gainD=gainD,
            gainC=gainC,
            id=id,
            metamodel=metamodel,
            rate=rate,
            satellite=satellite,
            actuators=actuators,
            reactionWheelCommands=reactionWheelCommands,
            magnetorquerCommands=magnetorquerCommands,
            errorIntegral=errorIntegral,
            _configuration=_configuration,
        )

from sedaro_base_client.model.metamodel import Metamodel
