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


class CelestialTarget(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
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
                    max_length = 100
            id = schemas.StrSchema
        
            @staticmethod
            def metamodel() -> typing.Type['Metamodel']:
                return Metamodel
            
            
            class targetType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "CELESTIAL_TARGET": "CELESTIAL_TARGET",
                    }
                
                @schemas.classproperty
                def CELESTIAL_TARGET(cls):
                    return cls("CELESTIAL_TARGET")
            rel_agentId = schemas.StrSchema
            conOps = schemas.StrSchema
            targetVector = schemas.StrSchema
            
            
            class targetGroups(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targetGroups':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            shadow = schemas.BoolSchema
            lst = schemas.NumberSchema
            position = schemas.AnyTypeSchema
            
            
            class lat(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            
            
            class lon(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            
            
            class alt(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            range = schemas.NumberSchema
            lineOfSight = schemas.BoolSchema
            relativePosition = schemas.AnyTypeSchema
            
            
            class azimuth(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            
            
            class elevation(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 360.0
                    inclusive_minimum = -360.0
            
            
            class polynomialEphemerisBody(
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
                            PolynomialEphemerisBody,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'polynomialEphemerisBody':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "id": id,
                "metamodel": metamodel,
                "targetType": targetType,
                "rel_agentId": rel_agentId,
                "conOps": conOps,
                "targetVector": targetVector,
                "targetGroups": targetGroups,
                "shadow": shadow,
                "lst": lst,
                "position": position,
                "lat": lat,
                "lon": lon,
                "alt": alt,
                "range": range,
                "lineOfSight": lineOfSight,
                "relativePosition": relativePosition,
                "azimuth": azimuth,
                "elevation": elevation,
                "polynomialEphemerisBody": polynomialEphemerisBody,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metamodel"]) -> 'Metamodel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetType"]) -> MetaOapg.properties.targetType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rel_agentId"]) -> MetaOapg.properties.rel_agentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["conOps"]) -> MetaOapg.properties.conOps: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetVector"]) -> MetaOapg.properties.targetVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroups"]) -> MetaOapg.properties.targetGroups: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shadow"]) -> MetaOapg.properties.shadow: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lst"]) -> MetaOapg.properties.lst: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lat"]) -> MetaOapg.properties.lat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lon"]) -> MetaOapg.properties.lon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alt"]) -> MetaOapg.properties.alt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["range"]) -> MetaOapg.properties.range: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lineOfSight"]) -> MetaOapg.properties.lineOfSight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relativePosition"]) -> MetaOapg.properties.relativePosition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["azimuth"]) -> MetaOapg.properties.azimuth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["elevation"]) -> MetaOapg.properties.elevation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["polynomialEphemerisBody"]) -> MetaOapg.properties.polynomialEphemerisBody: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["targetType"], typing_extensions.Literal["rel_agentId"], typing_extensions.Literal["conOps"], typing_extensions.Literal["targetVector"], typing_extensions.Literal["targetGroups"], typing_extensions.Literal["shadow"], typing_extensions.Literal["lst"], typing_extensions.Literal["position"], typing_extensions.Literal["lat"], typing_extensions.Literal["lon"], typing_extensions.Literal["alt"], typing_extensions.Literal["range"], typing_extensions.Literal["lineOfSight"], typing_extensions.Literal["relativePosition"], typing_extensions.Literal["azimuth"], typing_extensions.Literal["elevation"], typing_extensions.Literal["polynomialEphemerisBody"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metamodel"]) -> typing.Union['Metamodel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetType"]) -> typing.Union[MetaOapg.properties.targetType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rel_agentId"]) -> typing.Union[MetaOapg.properties.rel_agentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["conOps"]) -> typing.Union[MetaOapg.properties.conOps, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetVector"]) -> typing.Union[MetaOapg.properties.targetVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroups"]) -> typing.Union[MetaOapg.properties.targetGroups, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shadow"]) -> typing.Union[MetaOapg.properties.shadow, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lst"]) -> typing.Union[MetaOapg.properties.lst, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lat"]) -> typing.Union[MetaOapg.properties.lat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lon"]) -> typing.Union[MetaOapg.properties.lon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alt"]) -> typing.Union[MetaOapg.properties.alt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["range"]) -> typing.Union[MetaOapg.properties.range, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lineOfSight"]) -> typing.Union[MetaOapg.properties.lineOfSight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relativePosition"]) -> typing.Union[MetaOapg.properties.relativePosition, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["azimuth"]) -> typing.Union[MetaOapg.properties.azimuth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["elevation"]) -> typing.Union[MetaOapg.properties.elevation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["polynomialEphemerisBody"]) -> typing.Union[MetaOapg.properties.polynomialEphemerisBody, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["targetType"], typing_extensions.Literal["rel_agentId"], typing_extensions.Literal["conOps"], typing_extensions.Literal["targetVector"], typing_extensions.Literal["targetGroups"], typing_extensions.Literal["shadow"], typing_extensions.Literal["lst"], typing_extensions.Literal["position"], typing_extensions.Literal["lat"], typing_extensions.Literal["lon"], typing_extensions.Literal["alt"], typing_extensions.Literal["range"], typing_extensions.Literal["lineOfSight"], typing_extensions.Literal["relativePosition"], typing_extensions.Literal["azimuth"], typing_extensions.Literal["elevation"], typing_extensions.Literal["polynomialEphemerisBody"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metamodel: typing.Union['Metamodel', schemas.Unset] = schemas.unset,
        targetType: typing.Union[MetaOapg.properties.targetType, str, schemas.Unset] = schemas.unset,
        rel_agentId: typing.Union[MetaOapg.properties.rel_agentId, str, schemas.Unset] = schemas.unset,
        conOps: typing.Union[MetaOapg.properties.conOps, str, schemas.Unset] = schemas.unset,
        targetVector: typing.Union[MetaOapg.properties.targetVector, str, schemas.Unset] = schemas.unset,
        targetGroups: typing.Union[MetaOapg.properties.targetGroups, list, tuple, schemas.Unset] = schemas.unset,
        shadow: typing.Union[MetaOapg.properties.shadow, bool, schemas.Unset] = schemas.unset,
        lst: typing.Union[MetaOapg.properties.lst, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        lat: typing.Union[MetaOapg.properties.lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lon: typing.Union[MetaOapg.properties.lon, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        alt: typing.Union[MetaOapg.properties.alt, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        range: typing.Union[MetaOapg.properties.range, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        lineOfSight: typing.Union[MetaOapg.properties.lineOfSight, bool, schemas.Unset] = schemas.unset,
        relativePosition: typing.Union[MetaOapg.properties.relativePosition, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        azimuth: typing.Union[MetaOapg.properties.azimuth, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        elevation: typing.Union[MetaOapg.properties.elevation, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        polynomialEphemerisBody: typing.Union[MetaOapg.properties.polynomialEphemerisBody, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CelestialTarget':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            metamodel=metamodel,
            targetType=targetType,
            rel_agentId=rel_agentId,
            conOps=conOps,
            targetVector=targetVector,
            targetGroups=targetGroups,
            shadow=shadow,
            lst=lst,
            position=position,
            lat=lat,
            lon=lon,
            alt=alt,
            range=range,
            lineOfSight=lineOfSight,
            relativePosition=relativePosition,
            azimuth=azimuth,
            elevation=elevation,
            polynomialEphemerisBody=polynomialEphemerisBody,
            _configuration=_configuration,
        )

from sedaro_base_client.model.metamodel import Metamodel
from sedaro_base_client.model.polynomial_ephemeris_body import PolynomialEphemerisBody
