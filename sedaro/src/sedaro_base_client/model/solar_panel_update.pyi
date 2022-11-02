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


class SolarPanelUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "numSeries",
            "surface",
            "name",
            "numParallel",
            "cell",
            "blockingDiodeDrop",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class numSeries(
                schemas.IntSchema
            ):
                pass
            
            
            class numParallel(
                schemas.IntSchema
            ):
                pass
            
            
            class blockingDiodeDrop(
                schemas.NumberSchema
            ):
                pass
            cell = schemas.StrSchema
            surface = schemas.StrSchema
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
            __annotations__ = {
                "name": name,
                "numSeries": numSeries,
                "numParallel": numParallel,
                "blockingDiodeDrop": blockingDiodeDrop,
                "cell": cell,
                "surface": surface,
                "id": id,
                "partNumber": partNumber,
                "manufacturer": manufacturer,
                "hotTempRating": hotTempRating,
                "coldTempRating": coldTempRating,
                "thermalCapacitance": thermalCapacitance,
            }
    
    numSeries: MetaOapg.properties.numSeries
    surface: MetaOapg.properties.surface
    name: MetaOapg.properties.name
    numParallel: MetaOapg.properties.numParallel
    cell: MetaOapg.properties.cell
    blockingDiodeDrop: MetaOapg.properties.blockingDiodeDrop
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numSeries"]) -> MetaOapg.properties.numSeries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numParallel"]) -> MetaOapg.properties.numParallel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blockingDiodeDrop"]) -> MetaOapg.properties.blockingDiodeDrop: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cell"]) -> MetaOapg.properties.cell: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surface"]) -> MetaOapg.properties.surface: ...
    
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "numSeries", "numParallel", "blockingDiodeDrop", "cell", "surface", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numSeries"]) -> MetaOapg.properties.numSeries: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numParallel"]) -> MetaOapg.properties.numParallel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blockingDiodeDrop"]) -> MetaOapg.properties.blockingDiodeDrop: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cell"]) -> MetaOapg.properties.cell: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surface"]) -> MetaOapg.properties.surface: ...
    
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "numSeries", "numParallel", "blockingDiodeDrop", "cell", "surface", "id", "partNumber", "manufacturer", "hotTempRating", "coldTempRating", "thermalCapacitance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        numSeries: typing.Union[MetaOapg.properties.numSeries, decimal.Decimal, int, ],
        surface: typing.Union[MetaOapg.properties.surface, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        numParallel: typing.Union[MetaOapg.properties.numParallel, decimal.Decimal, int, ],
        cell: typing.Union[MetaOapg.properties.cell, str, ],
        blockingDiodeDrop: typing.Union[MetaOapg.properties.blockingDiodeDrop, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        partNumber: typing.Union[MetaOapg.properties.partNumber, str, schemas.Unset] = schemas.unset,
        manufacturer: typing.Union[MetaOapg.properties.manufacturer, str, schemas.Unset] = schemas.unset,
        hotTempRating: typing.Union[MetaOapg.properties.hotTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTempRating: typing.Union[MetaOapg.properties.coldTempRating, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        thermalCapacitance: typing.Union[MetaOapg.properties.thermalCapacitance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SolarPanelUpdate':
        return super().__new__(
            cls,
            *args,
            numSeries=numSeries,
            surface=surface,
            name=name,
            numParallel=numParallel,
            cell=cell,
            blockingDiodeDrop=blockingDiodeDrop,
            id=id,
            partNumber=partNumber,
            manufacturer=manufacturer,
            hotTempRating=hotTempRating,
            coldTempRating=coldTempRating,
            thermalCapacitance=thermalCapacitance,
            _configuration=_configuration,
            **kwargs,
        )
