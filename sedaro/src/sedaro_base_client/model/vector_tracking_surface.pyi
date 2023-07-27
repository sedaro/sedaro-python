# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.3.1
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


class VectorTrackingSurface(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "area",
            "surfaceCentroid",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            area = schemas.NumberSchema
            surfaceCentroid = schemas.AnyTypeSchema
            id = schemas.StrSchema
            bodyFrameVector = schemas.StrSchema
            surfaceMaterial = schemas.StrSchema
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
            
            
            class surfaceNormalVector(
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
                            FrameVectorBase299,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'surfaceNormalVector':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class sat2Sun(
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
                            FrameVectorBase299,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'sat2Sun':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            earthIrHeatFlowRate = schemas.NumberSchema
            earthAlbedoHeatFlowRate = schemas.NumberSchema
            solarHeatFlowRate = schemas.NumberSchema
            spaceHeatFlowRate = schemas.NumberSchema
            heatFlowRate = schemas.NumberSchema
            
            
            class temperature(
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
                            TemperatureBase299,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'temperature':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            hotMargin = schemas.NumberSchema
            coldMargin = schemas.NumberSchema
            antiTrack = schemas.BoolSchema
            
            
            class refVector1(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refVector1':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class refVector2(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'refVector2':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class vectorProjection(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'vectorProjection':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class articulationAngle(
                schemas.NumberSchema
            ):
                pass
            trackedVector = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "area": area,
                "surfaceCentroid": surfaceCentroid,
                "id": id,
                "bodyFrameVector": bodyFrameVector,
                "surfaceMaterial": surfaceMaterial,
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
                "antiTrack": antiTrack,
                "refVector1": refVector1,
                "refVector2": refVector2,
                "vectorProjection": vectorProjection,
                "articulationAngle": articulationAngle,
                "trackedVector": trackedVector,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    area: MetaOapg.properties.area
    surfaceCentroid: MetaOapg.properties.surfaceCentroid
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bodyFrameVector"]) -> MetaOapg.properties.bodyFrameVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["surfaceMaterial"]) -> MetaOapg.properties.surfaceMaterial: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["antiTrack"]) -> MetaOapg.properties.antiTrack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refVector1"]) -> MetaOapg.properties.refVector1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refVector2"]) -> MetaOapg.properties.refVector2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vectorProjection"]) -> MetaOapg.properties.vectorProjection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["articulationAngle"]) -> MetaOapg.properties.articulationAngle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trackedVector"]) -> MetaOapg.properties.trackedVector: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["area"], typing_extensions.Literal["surfaceCentroid"], typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["bodyFrameVector"], typing_extensions.Literal["surfaceMaterial"], typing_extensions.Literal["geocenterAngle"], typing_extensions.Literal["earthAlbedoViewFactor"], typing_extensions.Literal["earthIrViewFactor"], typing_extensions.Literal["solarViewFactor"], typing_extensions.Literal["surfaceNormalVector"], typing_extensions.Literal["sat2Sun"], typing_extensions.Literal["earthIrHeatFlowRate"], typing_extensions.Literal["earthAlbedoHeatFlowRate"], typing_extensions.Literal["solarHeatFlowRate"], typing_extensions.Literal["spaceHeatFlowRate"], typing_extensions.Literal["heatFlowRate"], typing_extensions.Literal["temperature"], typing_extensions.Literal["hotMargin"], typing_extensions.Literal["coldMargin"], typing_extensions.Literal["antiTrack"], typing_extensions.Literal["refVector1"], typing_extensions.Literal["refVector2"], typing_extensions.Literal["vectorProjection"], typing_extensions.Literal["articulationAngle"], typing_extensions.Literal["trackedVector"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["area"]) -> MetaOapg.properties.area: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceCentroid"]) -> MetaOapg.properties.surfaceCentroid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bodyFrameVector"]) -> typing.Union[MetaOapg.properties.bodyFrameVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["surfaceMaterial"]) -> typing.Union[MetaOapg.properties.surfaceMaterial, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["antiTrack"]) -> typing.Union[MetaOapg.properties.antiTrack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refVector1"]) -> typing.Union[MetaOapg.properties.refVector1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refVector2"]) -> typing.Union[MetaOapg.properties.refVector2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vectorProjection"]) -> typing.Union[MetaOapg.properties.vectorProjection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["articulationAngle"]) -> typing.Union[MetaOapg.properties.articulationAngle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trackedVector"]) -> typing.Union[MetaOapg.properties.trackedVector, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["area"], typing_extensions.Literal["surfaceCentroid"], typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["bodyFrameVector"], typing_extensions.Literal["surfaceMaterial"], typing_extensions.Literal["geocenterAngle"], typing_extensions.Literal["earthAlbedoViewFactor"], typing_extensions.Literal["earthIrViewFactor"], typing_extensions.Literal["solarViewFactor"], typing_extensions.Literal["surfaceNormalVector"], typing_extensions.Literal["sat2Sun"], typing_extensions.Literal["earthIrHeatFlowRate"], typing_extensions.Literal["earthAlbedoHeatFlowRate"], typing_extensions.Literal["solarHeatFlowRate"], typing_extensions.Literal["spaceHeatFlowRate"], typing_extensions.Literal["heatFlowRate"], typing_extensions.Literal["temperature"], typing_extensions.Literal["hotMargin"], typing_extensions.Literal["coldMargin"], typing_extensions.Literal["antiTrack"], typing_extensions.Literal["refVector1"], typing_extensions.Literal["refVector2"], typing_extensions.Literal["vectorProjection"], typing_extensions.Literal["articulationAngle"], typing_extensions.Literal["trackedVector"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        area: typing.Union[MetaOapg.properties.area, decimal.Decimal, int, float, ],
        surfaceCentroid: typing.Union[MetaOapg.properties.surfaceCentroid, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        bodyFrameVector: typing.Union[MetaOapg.properties.bodyFrameVector, str, schemas.Unset] = schemas.unset,
        surfaceMaterial: typing.Union[MetaOapg.properties.surfaceMaterial, str, schemas.Unset] = schemas.unset,
        geocenterAngle: typing.Union[MetaOapg.properties.geocenterAngle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthAlbedoViewFactor: typing.Union[MetaOapg.properties.earthAlbedoViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthIrViewFactor: typing.Union[MetaOapg.properties.earthIrViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        solarViewFactor: typing.Union[MetaOapg.properties.solarViewFactor, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        surfaceNormalVector: typing.Union[MetaOapg.properties.surfaceNormalVector, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        sat2Sun: typing.Union[MetaOapg.properties.sat2Sun, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        earthIrHeatFlowRate: typing.Union[MetaOapg.properties.earthIrHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        earthAlbedoHeatFlowRate: typing.Union[MetaOapg.properties.earthAlbedoHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        solarHeatFlowRate: typing.Union[MetaOapg.properties.solarHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        spaceHeatFlowRate: typing.Union[MetaOapg.properties.spaceHeatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        heatFlowRate: typing.Union[MetaOapg.properties.heatFlowRate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        temperature: typing.Union[MetaOapg.properties.temperature, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        hotMargin: typing.Union[MetaOapg.properties.hotMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        coldMargin: typing.Union[MetaOapg.properties.coldMargin, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        antiTrack: typing.Union[MetaOapg.properties.antiTrack, bool, schemas.Unset] = schemas.unset,
        refVector1: typing.Union[MetaOapg.properties.refVector1, list, tuple, schemas.Unset] = schemas.unset,
        refVector2: typing.Union[MetaOapg.properties.refVector2, list, tuple, schemas.Unset] = schemas.unset,
        vectorProjection: typing.Union[MetaOapg.properties.vectorProjection, list, tuple, schemas.Unset] = schemas.unset,
        articulationAngle: typing.Union[MetaOapg.properties.articulationAngle, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        trackedVector: typing.Union[MetaOapg.properties.trackedVector, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'VectorTrackingSurface':
        return super().__new__(
            cls,
            *_args,
            area=area,
            surfaceCentroid=surfaceCentroid,
            name=name,
            id=id,
            bodyFrameVector=bodyFrameVector,
            surfaceMaterial=surfaceMaterial,
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
            antiTrack=antiTrack,
            refVector1=refVector1,
            refVector2=refVector2,
            vectorProjection=vectorProjection,
            articulationAngle=articulationAngle,
            trackedVector=trackedVector,
            _configuration=_configuration,
        )

from sedaro_base_client.model.frame_vector_base299 import FrameVectorBase299
from sedaro_base_client.model.temperature_base299 import TemperatureBase299
