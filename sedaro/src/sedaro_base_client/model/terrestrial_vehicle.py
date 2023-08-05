# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.5.2
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


class TerrestrialVehicle(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to inherit when creating a `Metamodel`
    """


    class MetaOapg:
        required = {
            "cadScaleFactor",
            "cadSignedUrl",
            "cadKey",
        }
        
        class properties:
            
            
            class cadKey(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 48
            
            
            class cadSignedUrl(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 1024
            cadScaleFactor = schemas.NumberSchema
            
            
            class blocks(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.DictSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, ],
                ) -> 'blocks':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class index(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, list, tuple, ],
                ) -> 'index':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class position(
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
                            PositionBase306,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'position':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class velocity(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'velocity':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class attitude(
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
                            QuaternionBase306,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class angularVelocity(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'angularVelocity':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            selfId = schemas.StrSchema
            
            
            class cadFileName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            currentWaypointPath = schemas.StrSchema
            ramVector = schemas.StrSchema
            upVector = schemas.StrSchema
            activeOpMode = schemas.StrSchema
            
            
            class enabledModules(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'enabledModules':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "cadKey": cadKey,
                "cadSignedUrl": cadSignedUrl,
                "cadScaleFactor": cadScaleFactor,
                "blocks": blocks,
                "index": index,
                "position": position,
                "velocity": velocity,
                "attitude": attitude,
                "angularVelocity": angularVelocity,
                "selfId": selfId,
                "cadFileName": cadFileName,
                "currentWaypointPath": currentWaypointPath,
                "ramVector": ramVector,
                "upVector": upVector,
                "activeOpMode": activeOpMode,
                "enabledModules": enabledModules,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    cadScaleFactor: MetaOapg.properties.cadScaleFactor
    cadSignedUrl: MetaOapg.properties.cadSignedUrl
    cadKey: MetaOapg.properties.cadKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadScaleFactor"]) -> MetaOapg.properties.cadScaleFactor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadSignedUrl"]) -> MetaOapg.properties.cadSignedUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadKey"]) -> MetaOapg.properties.cadKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["blocks"]) -> MetaOapg.properties.blocks: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["velocity"]) -> MetaOapg.properties.velocity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attitude"]) -> MetaOapg.properties.attitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["angularVelocity"]) -> MetaOapg.properties.angularVelocity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfId"]) -> MetaOapg.properties.selfId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cadFileName"]) -> MetaOapg.properties.cadFileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentWaypointPath"]) -> MetaOapg.properties.currentWaypointPath: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ramVector"]) -> MetaOapg.properties.ramVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["upVector"]) -> MetaOapg.properties.upVector: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeOpMode"]) -> MetaOapg.properties.activeOpMode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabledModules"]) -> MetaOapg.properties.enabledModules: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cadScaleFactor"], typing_extensions.Literal["cadSignedUrl"], typing_extensions.Literal["cadKey"], typing_extensions.Literal["blocks"], typing_extensions.Literal["index"], typing_extensions.Literal["position"], typing_extensions.Literal["velocity"], typing_extensions.Literal["attitude"], typing_extensions.Literal["angularVelocity"], typing_extensions.Literal["selfId"], typing_extensions.Literal["cadFileName"], typing_extensions.Literal["currentWaypointPath"], typing_extensions.Literal["ramVector"], typing_extensions.Literal["upVector"], typing_extensions.Literal["activeOpMode"], typing_extensions.Literal["enabledModules"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadScaleFactor"]) -> MetaOapg.properties.cadScaleFactor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadSignedUrl"]) -> MetaOapg.properties.cadSignedUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadKey"]) -> MetaOapg.properties.cadKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["blocks"]) -> typing.Union[MetaOapg.properties.blocks, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["index"]) -> typing.Union[MetaOapg.properties.index, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["velocity"]) -> typing.Union[MetaOapg.properties.velocity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attitude"]) -> typing.Union[MetaOapg.properties.attitude, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["angularVelocity"]) -> typing.Union[MetaOapg.properties.angularVelocity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfId"]) -> typing.Union[MetaOapg.properties.selfId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cadFileName"]) -> typing.Union[MetaOapg.properties.cadFileName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentWaypointPath"]) -> typing.Union[MetaOapg.properties.currentWaypointPath, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ramVector"]) -> typing.Union[MetaOapg.properties.ramVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["upVector"]) -> typing.Union[MetaOapg.properties.upVector, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeOpMode"]) -> typing.Union[MetaOapg.properties.activeOpMode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabledModules"]) -> typing.Union[MetaOapg.properties.enabledModules, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cadScaleFactor"], typing_extensions.Literal["cadSignedUrl"], typing_extensions.Literal["cadKey"], typing_extensions.Literal["blocks"], typing_extensions.Literal["index"], typing_extensions.Literal["position"], typing_extensions.Literal["velocity"], typing_extensions.Literal["attitude"], typing_extensions.Literal["angularVelocity"], typing_extensions.Literal["selfId"], typing_extensions.Literal["cadFileName"], typing_extensions.Literal["currentWaypointPath"], typing_extensions.Literal["ramVector"], typing_extensions.Literal["upVector"], typing_extensions.Literal["activeOpMode"], typing_extensions.Literal["enabledModules"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cadScaleFactor: typing.Union[MetaOapg.properties.cadScaleFactor, decimal.Decimal, int, float, ],
        cadSignedUrl: typing.Union[MetaOapg.properties.cadSignedUrl, str, ],
        cadKey: typing.Union[MetaOapg.properties.cadKey, str, ],
        blocks: typing.Union[MetaOapg.properties.blocks, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        index: typing.Union[MetaOapg.properties.index, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        velocity: typing.Union[MetaOapg.properties.velocity, list, tuple, schemas.Unset] = schemas.unset,
        attitude: typing.Union[MetaOapg.properties.attitude, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        angularVelocity: typing.Union[MetaOapg.properties.angularVelocity, list, tuple, schemas.Unset] = schemas.unset,
        selfId: typing.Union[MetaOapg.properties.selfId, str, schemas.Unset] = schemas.unset,
        cadFileName: typing.Union[MetaOapg.properties.cadFileName, str, schemas.Unset] = schemas.unset,
        currentWaypointPath: typing.Union[MetaOapg.properties.currentWaypointPath, str, schemas.Unset] = schemas.unset,
        ramVector: typing.Union[MetaOapg.properties.ramVector, str, schemas.Unset] = schemas.unset,
        upVector: typing.Union[MetaOapg.properties.upVector, str, schemas.Unset] = schemas.unset,
        activeOpMode: typing.Union[MetaOapg.properties.activeOpMode, str, schemas.Unset] = schemas.unset,
        enabledModules: typing.Union[MetaOapg.properties.enabledModules, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TerrestrialVehicle':
        return super().__new__(
            cls,
            *_args,
            cadScaleFactor=cadScaleFactor,
            cadSignedUrl=cadSignedUrl,
            cadKey=cadKey,
            blocks=blocks,
            index=index,
            position=position,
            velocity=velocity,
            attitude=attitude,
            angularVelocity=angularVelocity,
            selfId=selfId,
            cadFileName=cadFileName,
            currentWaypointPath=currentWaypointPath,
            ramVector=ramVector,
            upVector=upVector,
            activeOpMode=activeOpMode,
            enabledModules=enabledModules,
            _configuration=_configuration,
        )

from sedaro_base_client.model.position_base306 import PositionBase306
from sedaro_base_client.model.quaternion_base306 import QuaternionBase306
