# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.1
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


class Parameters(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An enumeration.
    """


    class MetaOapg:
        enum_value_to_name = {
            "SHADOW": "SHADOW",
            "BETA": "BETA",
            "MEAN_ANOM": "MEAN_ANOM",
            "TRUE_ANOM": "TRUE_ANOM",
            "LAT": "LAT",
            "LON": "LON",
            "ALT": "ALT",
            "LO_SIGHT": "LO_SIGHT",
            "RANGE": "RANGE",
            "SOLAR_AZ": "SOLAR_AZ",
            "SOLAR_EL": "SOLAR_EL",
            "SAT_AZ": "SAT_AZ",
            "SAT_EL": "SAT_EL",
            "LOCAL_SIDEREAL_TIME": "LOCAL_SIDEREAL_TIME",
            "BATTERY_SOC": "BATTERY_SOC",
            schemas.NoneClass.NONE: "NONE",
        }
    
    @schemas.classproperty
    def SHADOW(cls):
        return cls("SHADOW")
    
    @schemas.classproperty
    def BETA(cls):
        return cls("BETA")
    
    @schemas.classproperty
    def MEAN_ANOM(cls):
        return cls("MEAN_ANOM")
    
    @schemas.classproperty
    def TRUE_ANOM(cls):
        return cls("TRUE_ANOM")
    
    @schemas.classproperty
    def LAT(cls):
        return cls("LAT")
    
    @schemas.classproperty
    def LON(cls):
        return cls("LON")
    
    @schemas.classproperty
    def ALT(cls):
        return cls("ALT")
    
    @schemas.classproperty
    def LO_SIGHT(cls):
        return cls("LO_SIGHT")
    
    @schemas.classproperty
    def RANGE(cls):
        return cls("RANGE")
    
    @schemas.classproperty
    def SOLAR_AZ(cls):
        return cls("SOLAR_AZ")
    
    @schemas.classproperty
    def SOLAR_EL(cls):
        return cls("SOLAR_EL")
    
    @schemas.classproperty
    def SAT_AZ(cls):
        return cls("SAT_AZ")
    
    @schemas.classproperty
    def SAT_EL(cls):
        return cls("SAT_EL")
    
    @schemas.classproperty
    def LOCAL_SIDEREAL_TIME(cls):
        return cls("LOCAL_SIDEREAL_TIME")
    
    @schemas.classproperty
    def BATTERY_SOC(cls):
        return cls("BATTERY_SOC")
    
    @schemas.classproperty
    def NONE(cls):
        return cls(None)
