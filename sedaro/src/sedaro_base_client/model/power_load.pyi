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


class PowerLoad(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "loadDefParams",
            "loadDefType",
            "name",
            "epsOutputType",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class epsOutputType(
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
                            EpsOutputTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'epsOutputType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class loadDefType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CONSTANT_POWER(cls):
                    return cls("CONSTANT_POWER")
        
            @staticmethod
            def loadDefParams() -> typing.Type['ConstantPowerParams']:
                return ConstantPowerParams
            id = schemas.StrSchema
        
            @staticmethod
            def metamodel() -> typing.Type['Metamodel']:
                return Metamodel
            busRegulator = schemas.StrSchema
            powerProcessor = schemas.StrSchema
            loadState = schemas.StrSchema
            powerConsumed = schemas.NumberSchema
            isActive = schemas.BoolSchema
            dutyCyclePeriod = schemas.NumberSchema
            
            
            class dutyCyclePercentage(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "name": name,
                "epsOutputType": epsOutputType,
                "loadDefType": loadDefType,
                "loadDefParams": loadDefParams,
                "id": id,
                "metamodel": metamodel,
                "busRegulator": busRegulator,
                "powerProcessor": powerProcessor,
                "loadState": loadState,
                "powerConsumed": powerConsumed,
                "isActive": isActive,
                "dutyCyclePeriod": dutyCyclePeriod,
                "dutyCyclePercentage": dutyCyclePercentage,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    loadDefParams: 'ConstantPowerParams'
    loadDefType: MetaOapg.properties.loadDefType
    name: MetaOapg.properties.name
    epsOutputType: MetaOapg.properties.epsOutputType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadDefParams"]) -> 'ConstantPowerParams': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadDefType"]) -> MetaOapg.properties.loadDefType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["epsOutputType"]) -> MetaOapg.properties.epsOutputType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metamodel"]) -> 'Metamodel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["busRegulator"]) -> MetaOapg.properties.busRegulator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerProcessor"]) -> MetaOapg.properties.powerProcessor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loadState"]) -> MetaOapg.properties.loadState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerConsumed"]) -> MetaOapg.properties.powerConsumed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dutyCyclePeriod"]) -> MetaOapg.properties.dutyCyclePeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dutyCyclePercentage"]) -> MetaOapg.properties.dutyCyclePercentage: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["loadDefParams"], typing_extensions.Literal["loadDefType"], typing_extensions.Literal["name"], typing_extensions.Literal["epsOutputType"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["busRegulator"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["loadState"], typing_extensions.Literal["powerConsumed"], typing_extensions.Literal["isActive"], typing_extensions.Literal["dutyCyclePeriod"], typing_extensions.Literal["dutyCyclePercentage"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadDefParams"]) -> 'ConstantPowerParams': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadDefType"]) -> MetaOapg.properties.loadDefType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["epsOutputType"]) -> MetaOapg.properties.epsOutputType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metamodel"]) -> typing.Union['Metamodel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["busRegulator"]) -> typing.Union[MetaOapg.properties.busRegulator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerProcessor"]) -> typing.Union[MetaOapg.properties.powerProcessor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loadState"]) -> typing.Union[MetaOapg.properties.loadState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerConsumed"]) -> typing.Union[MetaOapg.properties.powerConsumed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dutyCyclePeriod"]) -> typing.Union[MetaOapg.properties.dutyCyclePeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dutyCyclePercentage"]) -> typing.Union[MetaOapg.properties.dutyCyclePercentage, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["loadDefParams"], typing_extensions.Literal["loadDefType"], typing_extensions.Literal["name"], typing_extensions.Literal["epsOutputType"], typing_extensions.Literal["id"], typing_extensions.Literal["metamodel"], typing_extensions.Literal["busRegulator"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["loadState"], typing_extensions.Literal["powerConsumed"], typing_extensions.Literal["isActive"], typing_extensions.Literal["dutyCyclePeriod"], typing_extensions.Literal["dutyCyclePercentage"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        loadDefParams: 'ConstantPowerParams',
        loadDefType: typing.Union[MetaOapg.properties.loadDefType, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        epsOutputType: typing.Union[MetaOapg.properties.epsOutputType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        metamodel: typing.Union['Metamodel', schemas.Unset] = schemas.unset,
        busRegulator: typing.Union[MetaOapg.properties.busRegulator, str, schemas.Unset] = schemas.unset,
        powerProcessor: typing.Union[MetaOapg.properties.powerProcessor, str, schemas.Unset] = schemas.unset,
        loadState: typing.Union[MetaOapg.properties.loadState, str, schemas.Unset] = schemas.unset,
        powerConsumed: typing.Union[MetaOapg.properties.powerConsumed, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        dutyCyclePeriod: typing.Union[MetaOapg.properties.dutyCyclePeriod, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dutyCyclePercentage: typing.Union[MetaOapg.properties.dutyCyclePercentage, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PowerLoad':
        return super().__new__(
            cls,
            *_args,
            loadDefParams=loadDefParams,
            loadDefType=loadDefType,
            name=name,
            epsOutputType=epsOutputType,
            id=id,
            metamodel=metamodel,
            busRegulator=busRegulator,
            powerProcessor=powerProcessor,
            loadState=loadState,
            powerConsumed=powerConsumed,
            isActive=isActive,
            dutyCyclePeriod=dutyCyclePeriod,
            dutyCyclePercentage=dutyCyclePercentage,
            _configuration=_configuration,
        )

from sedaro_base_client.model.constant_power_params import ConstantPowerParams
from sedaro_base_client.model.eps_output_types import EpsOutputTypes
from sedaro_base_client.model.metamodel import Metamodel
