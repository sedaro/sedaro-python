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


class ThermalInterface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "sideB",
            "sideA",
        }
        
        class properties:
            name = schemas.StrSchema
            
            
            class sideA(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            SideCategories,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sideA':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class sideB(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            SideCategories,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sideB':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            area = schemas.NumberSchema
            material = schemas.StrSchema
            componentA = schemas.StrSchema
            componentB = schemas.StrSchema
            surfaceA = schemas.StrSchema
            surfaceB = schemas.StrSchema
            coolerA = schemas.StrSchema
            coolerB = schemas.StrSchema
            satellite = schemas.StrSchema
            resistance = schemas.NumberSchema
            tempDelta = schemas.NumberSchema
            heatFlowRate = schemas.NumberSchema
            hotTemp = schemas.NumberSchema
            coldTemp = schemas.NumberSchema
            hotMargin = schemas.NumberSchema
            coldMargin = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "sideA": sideA,
                "sideB": sideB,
                "id": id,
                "area": area,
                "material": material,
                "componentA": componentA,
                "componentB": componentB,
                "surfaceA": surfaceA,
                "surfaceB": surfaceB,
                "coolerA": coolerA,
                "coolerB": coolerB,
                "satellite": satellite,
                "resistance": resistance,
                "tempDelta": tempDelta,
                "heatFlowRate": heatFlowRate,
                "hotTemp": hotTemp,
                "coldTemp": coldTemp,
                "hotMargin": hotMargin,
                "coldMargin": coldMargin,
            }
    
    name: MetaOapg.properties.name
    sideB: MetaOapg.properties.sideB
    sideA: MetaOapg.properties.sideA
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sideA"]) -> MetaOapg.properties.sideA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sideB"]) -> MetaOapg.properties.sideB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["material"]) -> MetaOapg.properties.material: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentA"]) -> MetaOapg.properties.componentA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["componentB"]) -> MetaOapg.properties.componentB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceA"]) -> MetaOapg.properties.surfaceA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceB"]) -> MetaOapg.properties.surfaceB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coolerA"]) -> MetaOapg.properties.coolerA: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coolerB"]) -> MetaOapg.properties.coolerB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resistance"]) -> MetaOapg.properties.resistance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tempDelta"]) -> MetaOapg.properties.tempDelta: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heatFlowRate"]) -> MetaOapg.properties.heatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotTemp"]) -> MetaOapg.properties.hotTemp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldTemp"]) -> MetaOapg.properties.coldTemp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotMargin"]) -> MetaOapg.properties.hotMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldMargin"]) -> MetaOapg.properties.coldMargin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "sideA", "sideB", "id", "area", "material", "componentA", "componentB", "surfaceA", "surfaceB", "coolerA", "coolerB", "satellite", "resistance", "tempDelta", "heatFlowRate", "hotTemp", "coldTemp", "hotMargin", "coldMargin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sideA"]) -> MetaOapg.properties.sideA: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sideB"]) -> MetaOapg.properties.sideB: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> typing.Union[MetaOapg.properties.area, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["material"]) -> typing.Union[MetaOapg.properties.material, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentA"]) -> typing.Union[MetaOapg.properties.componentA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["componentB"]) -> typing.Union[MetaOapg.properties.componentB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceA"]) -> typing.Union[MetaOapg.properties.surfaceA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceB"]) -> typing.Union[MetaOapg.properties.surfaceB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coolerA"]) -> typing.Union[MetaOapg.properties.coolerA, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coolerB"]) -> typing.Union[MetaOapg.properties.coolerB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> typing.Union[MetaOapg.properties.satellite, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resistance"]) -> typing.Union[MetaOapg.properties.resistance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tempDelta"]) -> typing.Union[MetaOapg.properties.tempDelta, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heatFlowRate"]) -> typing.Union[MetaOapg.properties.heatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotTemp"]) -> typing.Union[MetaOapg.properties.hotTemp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldTemp"]) -> typing.Union[MetaOapg.properties.coldTemp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotMargin"]) -> typing.Union[MetaOapg.properties.hotMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldMargin"]) -> typing.Union[MetaOapg.properties.coldMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "sideA", "sideB", "id", "area", "material", "componentA", "componentB", "surfaceA", "surfaceB", "coolerA", "coolerB", "satellite", "resistance", "tempDelta", "heatFlowRate", "hotTemp", "coldTemp", "hotMargin", "coldMargin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        sideB: typing.Union[MetaOapg.properties.sideB, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        sideA: typing.Union[MetaOapg.properties.sideA, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        area: typing.Union[MetaOapg.properties.area, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        material: typing.Union[MetaOapg.properties.material, str, schemas.Unset] = schemas.unset,
        componentA: typing.Union[MetaOapg.properties.componentA, str, schemas.Unset] = schemas.unset,
        componentB: typing.Union[MetaOapg.properties.componentB, str, schemas.Unset] = schemas.unset,
        surfaceA: typing.Union[MetaOapg.properties.surfaceA, str, schemas.Unset] = schemas.unset,
        surfaceB: typing.Union[MetaOapg.properties.surfaceB, str, schemas.Unset] = schemas.unset,
        coolerA: typing.Union[MetaOapg.properties.coolerA, str, schemas.Unset] = schemas.unset,
        coolerB: typing.Union[MetaOapg.properties.coolerB, str, schemas.Unset] = schemas.unset,
        satellite: typing.Union[MetaOapg.properties.satellite, str, schemas.Unset] = schemas.unset,
        resistance: typing.Union[MetaOapg.properties.resistance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tempDelta: typing.Union[MetaOapg.properties.tempDelta, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        heatFlowRate: typing.Union[MetaOapg.properties.heatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hotTemp: typing.Union[MetaOapg.properties.hotTemp, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldTemp: typing.Union[MetaOapg.properties.coldTemp, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ThermalInterface':
        return super().__new__(
            cls,
            *_args,
            name=name,
            sideB=sideB,
            sideA=sideA,
            id=id,
            area=area,
            material=material,
            componentA=componentA,
            componentB=componentB,
            surfaceA=surfaceA,
            surfaceB=surfaceB,
            coolerA=coolerA,
            coolerB=coolerB,
            satellite=satellite,
            resistance=resistance,
            tempDelta=tempDelta,
            heatFlowRate=heatFlowRate,
            hotTemp=hotTemp,
            coldTemp=coldTemp,
            hotMargin=hotMargin,
            coldMargin=coldMargin,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.side_categories import SideCategories
