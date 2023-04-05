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


class SimulationJob(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "dataId",
            "bedRef",
            "startTime",
            "stopTime",
            "id",
            "simulatedAgents",
            "status",
        }
        
        class properties:
            id = schemas.IntSchema
            
            
            class status(
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
                            Statuses,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            bedRef = schemas.StrSchema
            dataId = schemas.IntSchema
            startTime = schemas.NumberSchema
            stopTime = schemas.NumberSchema
            
            
            class simulatedAgents(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.StrSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                ) -> 'simulatedAgents':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            realTime = schemas.BoolSchema
            progress = schemas.DictSchema
            __annotations__ = {
                "id": id,
                "status": status,
                "bedRef": bedRef,
                "dataId": dataId,
                "startTime": startTime,
                "stopTime": stopTime,
                "simulatedAgents": simulatedAgents,
                "realTime": realTime,
                "progress": progress,
            }
    
    dataId: MetaOapg.properties.dataId
    bedRef: MetaOapg.properties.bedRef
    startTime: MetaOapg.properties.startTime
    stopTime: MetaOapg.properties.stopTime
    id: MetaOapg.properties.id
    simulatedAgents: MetaOapg.properties.simulatedAgents
    status: MetaOapg.properties.status
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bedRef"]) -> MetaOapg.properties.bedRef: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataId"]) -> MetaOapg.properties.dataId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stopTime"]) -> MetaOapg.properties.stopTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simulatedAgents"]) -> MetaOapg.properties.simulatedAgents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realTime"]) -> MetaOapg.properties.realTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["progress"]) -> MetaOapg.properties.progress: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "bedRef", "dataId", "startTime", "stopTime", "simulatedAgents", "realTime", "progress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bedRef"]) -> MetaOapg.properties.bedRef: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataId"]) -> MetaOapg.properties.dataId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startTime"]) -> MetaOapg.properties.startTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stopTime"]) -> MetaOapg.properties.stopTime: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simulatedAgents"]) -> MetaOapg.properties.simulatedAgents: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realTime"]) -> typing.Union[MetaOapg.properties.realTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["progress"]) -> typing.Union[MetaOapg.properties.progress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "bedRef", "dataId", "startTime", "stopTime", "simulatedAgents", "realTime", "progress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dataId: typing.Union[MetaOapg.properties.dataId, decimal.Decimal, int, ],
        bedRef: typing.Union[MetaOapg.properties.bedRef, str, ],
        startTime: typing.Union[MetaOapg.properties.startTime, decimal.Decimal, int, float, ],
        stopTime: typing.Union[MetaOapg.properties.stopTime, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        simulatedAgents: typing.Union[MetaOapg.properties.simulatedAgents, dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        realTime: typing.Union[MetaOapg.properties.realTime, bool, schemas.Unset] = schemas.unset,
        progress: typing.Union[MetaOapg.properties.progress, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SimulationJob':
        return super().__new__(
            cls,
            *_args,
            dataId=dataId,
            bedRef=bedRef,
            startTime=startTime,
            stopTime=stopTime,
            id=id,
            simulatedAgents=simulatedAgents,
            status=status,
            realTime=realTime,
            progress=progress,
            _configuration=_configuration,
            **kwargs,
        )

from sedaro_base_client.model.statuses import Statuses
