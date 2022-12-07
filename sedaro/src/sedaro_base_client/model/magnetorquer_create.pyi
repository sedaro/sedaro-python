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


class MagnetorquerCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "bodyFrameVector",
            "ratedMagneticMoment",
            "name",
            "powerAtRatedMagneticMoment",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            bodyFrameVector = schemas.StrSchema
            
            
            class ratedMagneticMoment(
                schemas.NumberSchema
            ):
                pass
            powerAtRatedMagneticMoment = schemas.NumberSchema
            id = schemas.StrSchema
            
            
            class partNumber(
                schemas.StrSchema
            ):
                pass
            
            
            class manufacturer(
                schemas.StrSchema
            ):
                pass
            hotTempRating = schemas.NumberSchema
            coldTempRating = schemas.NumberSchema
            
            
            class thermalCapacitance(
                schemas.NumberSchema
            ):
                pass
            busRegulator = schemas.StrSchema
            topology = schemas.StrSchema
            torque = schemas.AnyTypeSchema
            
            
            class maxTorque(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'maxTorque':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            commandedTorqueMagnitude = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "bodyFrameVector": bodyFrameVector,
                "ratedMagneticMoment": ratedMagneticMoment,
                "powerAtRatedMagneticMoment": powerAtRatedMagneticMoment,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
                "busRegulator": busRegulator,
                "topology": topology,
                "torque": torque,
                "maxTorque": maxTorque,
                "commandedTorqueMagnitude": commandedTorqueMagnitude,
            }
    
    bodyFrameVector: MetaOapg.properties.bodyFrameVector
    ratedMagneticMoment: MetaOapg.properties.ratedMagneticMoment
    name: MetaOapg.properties.name
    powerAtRatedMagneticMoment: MetaOapg.properties.powerAtRatedMagneticMoment
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ratedMagneticMoment"]) -> MetaOapg.properties.ratedMagneticMoment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerAtRatedMagneticMoment"]) -> MetaOapg.properties.powerAtRatedMagneticMoment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partNumber"]) -> MetaOapg.properties.partNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["manufacturer"]) -> MetaOapg.properties.manufacturer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotTempRating"]) -> MetaOapg.properties.hotTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldTempRating"]) -> MetaOapg.properties.coldTempRating: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermalCapacitance"]) -> MetaOapg.properties.thermalCapacitance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busRegulator"]) -> MetaOapg.properties.busRegulator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topology"]) -> MetaOapg.properties.topology: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["torque"]) -> MetaOapg.properties.torque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxTorque"]) -> MetaOapg.properties.maxTorque: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commandedTorqueMagnitude"]) -> MetaOapg.properties.commandedTorqueMagnitude: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "bodyFrameVector", "ratedMagneticMoment", "powerAtRatedMagneticMoment", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "busRegulator", "topology", "torque", "maxTorque", "commandedTorqueMagnitude", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ratedMagneticMoment"]) -> MetaOapg.properties.ratedMagneticMoment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerAtRatedMagneticMoment"]) -> MetaOapg.properties.powerAtRatedMagneticMoment: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partNumber"]) -> typing.Union[MetaOapg.properties.partNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["manufacturer"]) -> typing.Union[MetaOapg.properties.manufacturer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotTempRating"]) -> typing.Union[MetaOapg.properties.hotTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldTempRating"]) -> typing.Union[MetaOapg.properties.coldTempRating, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermalCapacitance"]) -> typing.Union[MetaOapg.properties.thermalCapacitance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busRegulator"]) -> typing.Union[MetaOapg.properties.busRegulator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topology"]) -> typing.Union[MetaOapg.properties.topology, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["torque"]) -> typing.Union[MetaOapg.properties.torque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxTorque"]) -> typing.Union[MetaOapg.properties.maxTorque, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commandedTorqueMagnitude"]) -> typing.Union[MetaOapg.properties.commandedTorqueMagnitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "bodyFrameVector", "ratedMagneticMoment", "powerAtRatedMagneticMoment", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", "busRegulator", "topology", "torque", "maxTorque", "commandedTorqueMagnitude", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, ],
        ratedMagneticMoment: typing.Union[MetaOapg.properties.ratedMagneticMoment, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        powerAtRatedMagneticMoment: typing.Union[MetaOapg.properties.powerAtRatedMagneticMoment, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        busRegulator: typing.Union[MetaOapg.properties.busRegulator, str, schemas.Unset] = schemas.unset,
        topology: typing.Union[MetaOapg.properties.topology, str, schemas.Unset] = schemas.unset,
        torque: typing.Union[MetaOapg.properties.torque, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        maxTorque: typing.Union[MetaOapg.properties.maxTorque, list, tuple, schemas.Unset] = schemas.unset,
        commandedTorqueMagnitude: typing.Union[MetaOapg.properties.commandedTorqueMagnitude, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MagnetorquerCreate':
        return super().__new__(
            cls,
            *_args,
            bodyFrameVector=bodyFrameVector,
            ratedMagneticMoment=ratedMagneticMoment,
            name=name,
            powerAtRatedMagneticMoment=powerAtRatedMagneticMoment,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            busRegulator=busRegulator,
            topology=topology,
            torque=torque,
            maxTorque=maxTorque,
            commandedTorqueMagnitude=commandedTorqueMagnitude,
            _configuration=_configuration,
            **kwargs,
        )
