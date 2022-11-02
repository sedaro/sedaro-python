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


class FixedSurface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "area",
            "bodyFrameVector",
            "surfaceCentroid",
            "motionType",
            "name",
            "satellite",
            "surfaceMaterial",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class motionType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("FIXED")
            area = schemas.NumberSchema
            
            
            class surfaceCentroid(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'surfaceCentroid':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            bodyFrameVector = schemas.StrSchema
            surfaceMaterial = schemas.StrSchema
            satellite = schemas.StrSchema
            id = schemas.StrSchema
            
            
            class panels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'panels':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class thermal_interface_A(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_A':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class thermal_interface_B(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'thermal_interface_B':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            heliocenterAngle = schemas.NumberSchema
            geocenterAngle = schemas.NumberSchema
            
            
            class earthAlbedoViewFactor(
                schemas.NumberSchema
            ):
                pass
            
            
            class earthIrViewFactor(
                schemas.NumberSchema
            ):
                pass
            
            
            class solarViewFactor(
                schemas.NumberSchema
            ):
                pass
            surfaceNormalVector = schemas.AnyTypeSchema
            
            
            class sat2Sun(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sat2Sun':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            earthIrHeatFlowRate = schemas.NumberSchema
            earthAlbedoHeatFlowRate = schemas.NumberSchema
            solarHeatFlowRate = schemas.NumberSchema
            spaceHeatFlowRate = schemas.NumberSchema
            heatFlowRate = schemas.NumberSchema
            temperature = schemas.NumberSchema
            hotMargin = schemas.NumberSchema
            coldMargin = schemas.NumberSchema
            __annotations__ = {
                "name": name,
                "motionType": motionType,
                "area": area,
                "surfaceCentroid": surfaceCentroid,
                "bodyFrameVector": bodyFrameVector,
                "surfaceMaterial": surfaceMaterial,
                "satellite": satellite,
                "id": id,
                "panels": panels,
                "thermal_interface_A": thermal_interface_A,
                "thermal_interface_B": thermal_interface_B,
                "heliocenterAngle": heliocenterAngle,
                "geocenterAngle": geocenterAngle,
                "earthAlbedoViewFactor": earthAlbedoViewFactor,
                "earthIrViewFactor": earthIrViewFactor,
                "solarViewFactor": solarViewFactor,
                "surfaceNormalVector": surfaceNormalVector,
                "sat2Sun": sat2Sun,
                "earthIrHeatFlowRate": earthIrHeatFlowRate,
                "earthAlbedoHeatFlowRate": earthAlbedoHeatFlowRate,
                "solarHeatFlowRate": solarHeatFlowRate,
                "spaceHeatFlowRate": spaceHeatFlowRate,
                "heatFlowRate": heatFlowRate,
                "temperature": temperature,
                "hotMargin": hotMargin,
                "coldMargin": coldMargin,
            }
    
    area: MetaOapg.properties.area
    bodyFrameVector: MetaOapg.properties.bodyFrameVector
    surfaceCentroid: MetaOapg.properties.surfaceCentroid
    motionType: MetaOapg.properties.motionType
    name: MetaOapg.properties.name
    satellite: MetaOapg.properties.satellite
    surfaceMaterial: MetaOapg.properties.surfaceMaterial
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["motionType"]) -> MetaOapg.properties.motionType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceMaterial"]) -> MetaOapg.properties.surfaceMaterial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["panels"]) -> MetaOapg.properties.panels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_A"]) -> MetaOapg.properties.thermal_interface_A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thermal_interface_B"]) -> MetaOapg.properties.thermal_interface_B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heliocenterAngle"]) -> MetaOapg.properties.heliocenterAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geocenterAngle"]) -> MetaOapg.properties.geocenterAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthAlbedoViewFactor"]) -> MetaOapg.properties.earthAlbedoViewFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthIrViewFactor"]) -> MetaOapg.properties.earthIrViewFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarViewFactor"]) -> MetaOapg.properties.solarViewFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceNormalVector"]) -> MetaOapg.properties.surfaceNormalVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sat2Sun"]) -> MetaOapg.properties.sat2Sun: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthIrHeatFlowRate"]) -> MetaOapg.properties.earthIrHeatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earthAlbedoHeatFlowRate"]) -> MetaOapg.properties.earthAlbedoHeatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["solarHeatFlowRate"]) -> MetaOapg.properties.solarHeatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["spaceHeatFlowRate"]) -> MetaOapg.properties.spaceHeatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heatFlowRate"]) -> MetaOapg.properties.heatFlowRate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temperature"]) -> MetaOapg.properties.temperature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hotMargin"]) -> MetaOapg.properties.hotMargin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coldMargin"]) -> MetaOapg.properties.coldMargin: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "motionType", "area", "surfaceCentroid", "bodyFrameVector", "surfaceMaterial", "satellite", "id", "panels", "thermal_interface_A", "thermal_interface_B", "heliocenterAngle", "geocenterAngle", "earthAlbedoViewFactor", "earthIrViewFactor", "solarViewFactor", "surfaceNormalVector", "sat2Sun", "earthIrHeatFlowRate", "earthAlbedoHeatFlowRate", "solarHeatFlowRate", "spaceHeatFlowRate", "heatFlowRate", "temperature", "hotMargin", "coldMargin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["motionType"]) -> MetaOapg.properties.motionType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceMaterial"]) -> MetaOapg.properties.surfaceMaterial: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["satellite"]) -> MetaOapg.properties.satellite: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["panels"]) -> typing.Union[MetaOapg.properties.panels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_A"]) -> typing.Union[MetaOapg.properties.thermal_interface_A, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thermal_interface_B"]) -> typing.Union[MetaOapg.properties.thermal_interface_B, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heliocenterAngle"]) -> typing.Union[MetaOapg.properties.heliocenterAngle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geocenterAngle"]) -> typing.Union[MetaOapg.properties.geocenterAngle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthAlbedoViewFactor"]) -> typing.Union[MetaOapg.properties.earthAlbedoViewFactor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthIrViewFactor"]) -> typing.Union[MetaOapg.properties.earthIrViewFactor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarViewFactor"]) -> typing.Union[MetaOapg.properties.solarViewFactor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceNormalVector"]) -> typing.Union[MetaOapg.properties.surfaceNormalVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sat2Sun"]) -> typing.Union[MetaOapg.properties.sat2Sun, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthIrHeatFlowRate"]) -> typing.Union[MetaOapg.properties.earthIrHeatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earthAlbedoHeatFlowRate"]) -> typing.Union[MetaOapg.properties.earthAlbedoHeatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["solarHeatFlowRate"]) -> typing.Union[MetaOapg.properties.solarHeatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["spaceHeatFlowRate"]) -> typing.Union[MetaOapg.properties.spaceHeatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heatFlowRate"]) -> typing.Union[MetaOapg.properties.heatFlowRate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temperature"]) -> typing.Union[MetaOapg.properties.temperature, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hotMargin"]) -> typing.Union[MetaOapg.properties.hotMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coldMargin"]) -> typing.Union[MetaOapg.properties.coldMargin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "motionType", "area", "surfaceCentroid", "bodyFrameVector", "surfaceMaterial", "satellite", "id", "panels", "thermal_interface_A", "thermal_interface_B", "heliocenterAngle", "geocenterAngle", "earthAlbedoViewFactor", "earthIrViewFactor", "solarViewFactor", "surfaceNormalVector", "sat2Sun", "earthIrHeatFlowRate", "earthAlbedoHeatFlowRate", "solarHeatFlowRate", "spaceHeatFlowRate", "heatFlowRate", "temperature", "hotMargin", "coldMargin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        area: typing.Union[MetaOapg.properties.area, decimal.Decimal, int, float, ],
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, ],
        surfaceCentroid: typing.Union[MetaOapg.properties.surfaceCentroid, list, tuple, ],
        motionType: typing.Union[MetaOapg.properties.motionType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        satellite: typing.Union[MetaOapg.properties.satellite, str, ],
        surfaceMaterial: typing.Union[MetaOapg.properties.surfaceMaterial, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        panels: typing.Union[MetaOapg.properties.panels, list, tuple, schemas.Unset] = schemas.unset,
        thermal_interface_A: typing.Union[MetaOapg.properties.thermal_interface_A, list, tuple, schemas.Unset] = schemas.unset,
        thermal_interface_B: typing.Union[MetaOapg.properties.thermal_interface_B, list, tuple, schemas.Unset] = schemas.unset,
        heliocenterAngle: typing.Union[MetaOapg.properties.heliocenterAngle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        geocenterAngle: typing.Union[MetaOapg.properties.geocenterAngle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthAlbedoViewFactor: typing.Union[MetaOapg.properties.earthAlbedoViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthIrViewFactor: typing.Union[MetaOapg.properties.earthIrViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        solarViewFactor: typing.Union[MetaOapg.properties.solarViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        surfaceNormalVector: typing.Union[MetaOapg.properties.surfaceNormalVector, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        sat2Sun: typing.Union[MetaOapg.properties.sat2Sun, list, tuple, schemas.Unset] = schemas.unset,
        earthIrHeatFlowRate: typing.Union[MetaOapg.properties.earthIrHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthAlbedoHeatFlowRate: typing.Union[MetaOapg.properties.earthAlbedoHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        solarHeatFlowRate: typing.Union[MetaOapg.properties.solarHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        spaceHeatFlowRate: typing.Union[MetaOapg.properties.spaceHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        heatFlowRate: typing.Union[MetaOapg.properties.heatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FixedSurface':
        return super().__new__(
            cls,
            *args,
            area=area,
            bodyFrameVector=bodyFrameVector,
            surfaceCentroid=surfaceCentroid,
            motionType=motionType,
            name=name,
            satellite=satellite,
            surfaceMaterial=surfaceMaterial,
            id=id,
            panels=panels,
            thermal_interface_A=thermal_interface_A,
            thermal_interface_B=thermal_interface_B,
            heliocenterAngle=heliocenterAngle,
            geocenterAngle=geocenterAngle,
            earthAlbedoViewFactor=earthAlbedoViewFactor,
            earthIrViewFactor=earthIrViewFactor,
            solarViewFactor=solarViewFactor,
            surfaceNormalVector=surfaceNormalVector,
            sat2Sun=sat2Sun,
            earthIrHeatFlowRate=earthIrHeatFlowRate,
            earthAlbedoHeatFlowRate=earthAlbedoHeatFlowRate,
            solarHeatFlowRate=solarHeatFlowRate,
            spaceHeatFlowRate=spaceHeatFlowRate,
            heatFlowRate=heatFlowRate,
            temperature=temperature,
            hotMargin=hotMargin,
            coldMargin=coldMargin,
            _configuration=_configuration,
            **kwargs,
        )
