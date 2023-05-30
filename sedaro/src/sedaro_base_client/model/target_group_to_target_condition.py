# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.1.1
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


class TargetGroupToTargetCondition(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class to be used internally and inherited by `Metamodel` and `Block`. Adds helper methods and properties.
    """


    class MetaOapg:
        required = {
            "tgParam",
            "name",
            "targetParam",
            "relationship",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class relationship(
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
                            ConditionRelationship,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'relationship':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tgParam(
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
                            TargetParameters,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tgParam':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class targetParam(
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
                            TargetParameters,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'targetParam':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            id = schemas.StrSchema
            terminator = schemas.BoolSchema
            compliance = schemas.BoolSchema
            targetGroup = schemas.StrSchema
            isFilter = schemas.StrSchema
            
            
            class targetCompliance(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.BoolSchema
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, bool, ],
                ) -> 'targetCompliance':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class countRelationship(
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
                            ConditionRelationship,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'countRelationship':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            countValue = schemas.IntSchema
            
            
            class groupRoller(
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
                            GroupRollers,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'groupRoller':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            targetA = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "relationship": relationship,
                "tgParam": tgParam,
                "targetParam": targetParam,
                "id": id,
                "terminator": terminator,
                "compliance": compliance,
                "targetGroup": targetGroup,
                "isFilter": isFilter,
                "targetCompliance": targetCompliance,
                "countRelationship": countRelationship,
                "countValue": countValue,
                "groupRoller": groupRoller,
                "targetA": targetA,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    tgParam: MetaOapg.properties.tgParam
    name: MetaOapg.properties.name
    targetParam: MetaOapg.properties.targetParam
    relationship: MetaOapg.properties.relationship
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tgParam"]) -> MetaOapg.properties.tgParam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetParam"]) -> MetaOapg.properties.targetParam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminator"]) -> MetaOapg.properties.terminator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compliance"]) -> MetaOapg.properties.compliance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetGroup"]) -> MetaOapg.properties.targetGroup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFilter"]) -> MetaOapg.properties.isFilter: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetCompliance"]) -> MetaOapg.properties.targetCompliance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countRelationship"]) -> MetaOapg.properties.countRelationship: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countValue"]) -> MetaOapg.properties.countValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupRoller"]) -> MetaOapg.properties.groupRoller: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targetA"]) -> MetaOapg.properties.targetA: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tgParam"], typing_extensions.Literal["name"], typing_extensions.Literal["targetParam"], typing_extensions.Literal["relationship"], typing_extensions.Literal["id"], typing_extensions.Literal["terminator"], typing_extensions.Literal["compliance"], typing_extensions.Literal["targetGroup"], typing_extensions.Literal["isFilter"], typing_extensions.Literal["targetCompliance"], typing_extensions.Literal["countRelationship"], typing_extensions.Literal["countValue"], typing_extensions.Literal["groupRoller"], typing_extensions.Literal["targetA"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tgParam"]) -> MetaOapg.properties.tgParam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetParam"]) -> MetaOapg.properties.targetParam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relationship"]) -> MetaOapg.properties.relationship: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminator"]) -> typing.Union[MetaOapg.properties.terminator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compliance"]) -> typing.Union[MetaOapg.properties.compliance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetGroup"]) -> typing.Union[MetaOapg.properties.targetGroup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFilter"]) -> typing.Union[MetaOapg.properties.isFilter, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetCompliance"]) -> typing.Union[MetaOapg.properties.targetCompliance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countRelationship"]) -> typing.Union[MetaOapg.properties.countRelationship, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countValue"]) -> typing.Union[MetaOapg.properties.countValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupRoller"]) -> typing.Union[MetaOapg.properties.groupRoller, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targetA"]) -> typing.Union[MetaOapg.properties.targetA, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tgParam"], typing_extensions.Literal["name"], typing_extensions.Literal["targetParam"], typing_extensions.Literal["relationship"], typing_extensions.Literal["id"], typing_extensions.Literal["terminator"], typing_extensions.Literal["compliance"], typing_extensions.Literal["targetGroup"], typing_extensions.Literal["isFilter"], typing_extensions.Literal["targetCompliance"], typing_extensions.Literal["countRelationship"], typing_extensions.Literal["countValue"], typing_extensions.Literal["groupRoller"], typing_extensions.Literal["targetA"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        tgParam: typing.Union[MetaOapg.properties.tgParam, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        targetParam: typing.Union[MetaOapg.properties.targetParam, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        relationship: typing.Union[MetaOapg.properties.relationship, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        terminator: typing.Union[MetaOapg.properties.terminator, bool, schemas.Unset] = schemas.unset,
        compliance: typing.Union[MetaOapg.properties.compliance, bool, schemas.Unset] = schemas.unset,
        targetGroup: typing.Union[MetaOapg.properties.targetGroup, str, schemas.Unset] = schemas.unset,
        isFilter: typing.Union[MetaOapg.properties.isFilter, str, schemas.Unset] = schemas.unset,
        targetCompliance: typing.Union[MetaOapg.properties.targetCompliance, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        countRelationship: typing.Union[MetaOapg.properties.countRelationship, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        countValue: typing.Union[MetaOapg.properties.countValue, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        groupRoller: typing.Union[MetaOapg.properties.groupRoller, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        targetA: typing.Union[MetaOapg.properties.targetA, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TargetGroupToTargetCondition':
        return super().__new__(
            cls,
            *_args,
            tgParam=tgParam,
            name=name,
            targetParam=targetParam,
            relationship=relationship,
            id=id,
            terminator=terminator,
            compliance=compliance,
            targetGroup=targetGroup,
            isFilter=isFilter,
            targetCompliance=targetCompliance,
            countRelationship=countRelationship,
            countValue=countValue,
            groupRoller=groupRoller,
            targetA=targetA,
            _configuration=_configuration,
        )

from sedaro_base_client.model.condition_relationship import ConditionRelationship
from sedaro_base_client.model.group_rollers import GroupRollers
from sedaro_base_client.model.target_parameters import TargetParameters
