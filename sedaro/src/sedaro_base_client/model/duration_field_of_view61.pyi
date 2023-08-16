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


class DurationFieldOfView61(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            min = schemas.NumberSchema
            s = schemas.NumberSchema
            hour = schemas.NumberSchema
            
            
            class day(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "min": min,
                "s": s,
                "hour": hour,
                "day": day,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["s"]) -> MetaOapg.properties.s: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hour"]) -> MetaOapg.properties.hour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["day"]) -> MetaOapg.properties.day: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["min"], typing_extensions.Literal["s"], typing_extensions.Literal["hour"], typing_extensions.Literal["day"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["s"]) -> typing.Union[MetaOapg.properties.s, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hour"]) -> typing.Union[MetaOapg.properties.hour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["day"]) -> typing.Union[MetaOapg.properties.day, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["min"], typing_extensions.Literal["s"], typing_extensions.Literal["hour"], typing_extensions.Literal["day"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        min: typing.Union[MetaOapg.properties.min, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        s: typing.Union[MetaOapg.properties.s, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        hour: typing.Union[MetaOapg.properties.hour, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        day: typing.Union[MetaOapg.properties.day, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DurationFieldOfView61':
        return super().__new__(
            cls,
            *_args,
            min=min,
            s=s,
            hour=hour,
            day=day,
            _configuration=_configuration,
        )