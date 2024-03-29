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


class QuaternionBase323(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class body_ecef(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 4
                    min_items = 4
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'body_ecef':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class body_eci(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 4
                    min_items = 4
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'body_eci':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class eci_body(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 4
                    min_items = 4
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'eci_body':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class ecef_body(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 4
                    min_items = 4
                    items = schemas.NumberSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, float, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ecef_body':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "body_ecef": body_ecef,
                "body_eci": body_eci,
                "eci_body": eci_body,
                "ecef_body": ecef_body,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_ecef"]) -> MetaOapg.properties.body_ecef: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["body_eci"]) -> MetaOapg.properties.body_eci: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eci_body"]) -> MetaOapg.properties.eci_body: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ecef_body"]) -> MetaOapg.properties.ecef_body: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["body_ecef"], typing_extensions.Literal["body_eci"], typing_extensions.Literal["eci_body"], typing_extensions.Literal["ecef_body"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_ecef"]) -> typing.Union[MetaOapg.properties.body_ecef, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["body_eci"]) -> typing.Union[MetaOapg.properties.body_eci, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eci_body"]) -> typing.Union[MetaOapg.properties.eci_body, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ecef_body"]) -> typing.Union[MetaOapg.properties.ecef_body, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["body_ecef"], typing_extensions.Literal["body_eci"], typing_extensions.Literal["eci_body"], typing_extensions.Literal["ecef_body"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        body_ecef: typing.Union[MetaOapg.properties.body_ecef, list, tuple, schemas.Unset] = schemas.unset,
        body_eci: typing.Union[MetaOapg.properties.body_eci, list, tuple, schemas.Unset] = schemas.unset,
        eci_body: typing.Union[MetaOapg.properties.eci_body, list, tuple, schemas.Unset] = schemas.unset,
        ecef_body: typing.Union[MetaOapg.properties.ecef_body, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'QuaternionBase323':
        return super().__new__(
            cls,
            *_args,
            body_ecef=body_ecef,
            body_eci=body_eci,
            eci_body=eci_body,
            ecef_body=ecef_body,
            _configuration=_configuration,
        )
