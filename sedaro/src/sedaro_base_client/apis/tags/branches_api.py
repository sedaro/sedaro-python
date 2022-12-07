# coding: utf-8

"""
    Sedaro Satellite API

     Allows for consumption of Sedaro Satellite services. Read more about Sedaro Satellite at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Currently the documentation for 200 responses to Block create, read, update, and delete (CRUD) operations is incorrect. This is due to an issue with our documentation generator.  Under each Block Group, the documentation will show `name`, `collection`, and `data` keys.  In reality, this level does not exist and should be skipped.  See the schema under the `data` key of a Template's Block Group for the correct schema of such Block Group. - Error responses are most specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 3.3.1
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_idcommits_.post import CommitToBranch
from sedaro_base_client.paths.models_branches_branch_id.post import CreateBranch
from sedaro_base_client.paths.models_branches_branch_id.delete import DeleteBranch
from sedaro_base_client.paths.models_branches_branch_id.get import GetBranch
from sedaro_base_client.paths.models_branches_branch_idcommitted_.get import GetCommittedBranchData
from sedaro_base_client.paths.models_branches_branch_idsaved_.get import GetSavedBranchData
from sedaro_base_client.paths.models_branches_current_branch_id_merge_incoming_branch_id.post import MergeBranches
from sedaro_base_client.paths.models_branches_branch_id.patch import UpdateBranch
from sedaro_base_client.paths.models_branches_branch_idshare_auth_.post import VerifyBranchPassword


class BranchesApi(
    CommitToBranch,
    CreateBranch,
    DeleteBranch,
    GetBranch,
    GetCommittedBranchData,
    GetSavedBranchData,
    MergeBranches,
    UpdateBranch,
    VerifyBranchPassword,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
