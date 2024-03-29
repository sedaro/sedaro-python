# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.7.0
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


class BusRegulator(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A BusRegulator Block
    """


    class MetaOapg:
        required = {
            "efficiency",
            "name",
            "inputType",
            "maxOutputPower",
            "voltage",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class inputType(
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
                            InputTypes,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'inputType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            voltage = schemas.NumberSchema
            
            
            class maxOutputPower(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_minimum = 0.0
            
            
            class efficiency(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 1.0
            id = schemas.StrSchema
            inRegulator = schemas.StrSchema
            powerProcessor = schemas.StrSchema
            
            
            class outRegulators(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'outRegulators':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class loads(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loads':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dynamicallyLoadedComponents(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dynamicallyLoadedComponents':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dissipations(
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
                            BaseDissipations,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'dissipations':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class outputPowers(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.NumberSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, decimal.Decimal, int, float, ],
                ) -> 'outputPowers':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "BusRegulator": "BUS_REGULATOR",
                    }
                
                @schemas.classproperty
                def BUS_REGULATOR(cls):
                    return cls("BusRegulator")
            __annotations__ = {
                "name": name,
                "inputType": inputType,
                "voltage": voltage,
                "maxOutputPower": maxOutputPower,
                "efficiency": efficiency,
                "id": id,
                "inRegulator": inRegulator,
                "powerProcessor": powerProcessor,
                "outRegulators": outRegulators,
                "loads": loads,
                "dynamicallyLoadedComponents": dynamicallyLoadedComponents,
                "dissipations": dissipations,
                "outputPowers": outputPowers,
                "type": type,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    efficiency: MetaOapg.properties.efficiency
    name: MetaOapg.properties.name
    inputType: MetaOapg.properties.inputType
    maxOutputPower: MetaOapg.properties.maxOutputPower
    voltage: MetaOapg.properties.voltage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["efficiency"]) -> MetaOapg.properties.efficiency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputType"]) -> MetaOapg.properties.inputType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxOutputPower"]) -> MetaOapg.properties.maxOutputPower: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["voltage"]) -> MetaOapg.properties.voltage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inRegulator"]) -> MetaOapg.properties.inRegulator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["powerProcessor"]) -> MetaOapg.properties.powerProcessor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outRegulators"]) -> MetaOapg.properties.outRegulators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loads"]) -> MetaOapg.properties.loads: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dynamicallyLoadedComponents"]) -> MetaOapg.properties.dynamicallyLoadedComponents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dissipations"]) -> MetaOapg.properties.dissipations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outputPowers"]) -> MetaOapg.properties.outputPowers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["efficiency"], typing_extensions.Literal["name"], typing_extensions.Literal["inputType"], typing_extensions.Literal["maxOutputPower"], typing_extensions.Literal["voltage"], typing_extensions.Literal["id"], typing_extensions.Literal["inRegulator"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["outRegulators"], typing_extensions.Literal["loads"], typing_extensions.Literal["dynamicallyLoadedComponents"], typing_extensions.Literal["dissipations"], typing_extensions.Literal["outputPowers"], typing_extensions.Literal["type"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["efficiency"]) -> MetaOapg.properties.efficiency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputType"]) -> MetaOapg.properties.inputType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxOutputPower"]) -> MetaOapg.properties.maxOutputPower: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["voltage"]) -> MetaOapg.properties.voltage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inRegulator"]) -> typing.Union[MetaOapg.properties.inRegulator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["powerProcessor"]) -> typing.Union[MetaOapg.properties.powerProcessor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outRegulators"]) -> typing.Union[MetaOapg.properties.outRegulators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loads"]) -> typing.Union[MetaOapg.properties.loads, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dynamicallyLoadedComponents"]) -> typing.Union[MetaOapg.properties.dynamicallyLoadedComponents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dissipations"]) -> typing.Union[MetaOapg.properties.dissipations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outputPowers"]) -> typing.Union[MetaOapg.properties.outputPowers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["efficiency"], typing_extensions.Literal["name"], typing_extensions.Literal["inputType"], typing_extensions.Literal["maxOutputPower"], typing_extensions.Literal["voltage"], typing_extensions.Literal["id"], typing_extensions.Literal["inRegulator"], typing_extensions.Literal["powerProcessor"], typing_extensions.Literal["outRegulators"], typing_extensions.Literal["loads"], typing_extensions.Literal["dynamicallyLoadedComponents"], typing_extensions.Literal["dissipations"], typing_extensions.Literal["outputPowers"], typing_extensions.Literal["type"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        efficiency: typing.Union[MetaOapg.properties.efficiency, decimal.Decimal, int, float, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        inputType: typing.Union[MetaOapg.properties.inputType, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        maxOutputPower: typing.Union[MetaOapg.properties.maxOutputPower, decimal.Decimal, int, float, ],
        voltage: typing.Union[MetaOapg.properties.voltage, decimal.Decimal, int, float, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        inRegulator: typing.Union[MetaOapg.properties.inRegulator, str, schemas.Unset] = schemas.unset,
        powerProcessor: typing.Union[MetaOapg.properties.powerProcessor, str, schemas.Unset] = schemas.unset,
        outRegulators: typing.Union[MetaOapg.properties.outRegulators, list, tuple, schemas.Unset] = schemas.unset,
        loads: typing.Union[MetaOapg.properties.loads, list, tuple, schemas.Unset] = schemas.unset,
        dynamicallyLoadedComponents: typing.Union[MetaOapg.properties.dynamicallyLoadedComponents, list, tuple, schemas.Unset] = schemas.unset,
        dissipations: typing.Union[MetaOapg.properties.dissipations, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        outputPowers: typing.Union[MetaOapg.properties.outputPowers, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BusRegulator':
        return super().__new__(
            cls,
            *_args,
            efficiency=efficiency,
            name=name,
            inputType=inputType,
            maxOutputPower=maxOutputPower,
            voltage=voltage,
            id=id,
            inRegulator=inRegulator,
            powerProcessor=powerProcessor,
            outRegulators=outRegulators,
            loads=loads,
            dynamicallyLoadedComponents=dynamicallyLoadedComponents,
            dissipations=dissipations,
            outputPowers=outputPowers,
            type=type,
            _configuration=_configuration,
        )

from sedaro_base_client.model.base_dissipations import BaseDissipations
from sedaro_base_client.model.input_types import InputTypes
