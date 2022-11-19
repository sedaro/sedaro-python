# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [satellite.sedaro.com](https://satellite.sedaro.com).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com   # noqa: E501

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


class Categories(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """
    
    @schemas.classproperty
    def POWER(cls):
        return cls("POWER")
    
    @schemas.classproperty
    def CDH(cls):
        return cls("CDH")
    
    @schemas.classproperty
    def COMMS(cls):
        return cls("COMMS")
    
    @schemas.classproperty
    def GNC(cls):
        return cls("GNC")
    
    @schemas.classproperty
    def THERMAL(cls):
        return cls("THERMAL")
    
    @schemas.classproperty
    def STRUCTURE(cls):
        return cls("STRUCTURE")
    
    @schemas.classproperty
    def CUSTOM(cls):
        return cls("CUSTOM")
