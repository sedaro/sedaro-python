# coding: utf-8

"""
    Sedaro API

     Allows for consumption of Sedaro services. Read more about Sedaro at [docs.sedaro.com](https://docs.sedaro.com).  ### Clients  **Python:** [sedaro](https://pypi.org/project/sedaro/) - This package provides additional functionality on top of the auto-generated OpenAPI client. See the package docs for more information.  ### API Key  To access the Sedaro service via this API, you will need an API key.  You can generate an API key for your account in the Sedaro [Management Console](https://satellite.sedaro.com/#/account). Once complete, pass the API key in all requests via the `X_API_KEY` HTTP header.  *API keys grant full access to your account and should never be shared. If you think your API key has been compromised, you can revoke it in the [Management Console](https://satellite.sedaro.com/#/account).*  ### Jupyter Notebooks  For additional examples of how to use this API for modeling and simulation, see our [Mod-Sim Notebooks](https://github.com/sedaro/modsim-notebooks).  ### Community, Support, Discussion  If you have any issues or suggestions, please reach out:  1. Join the Sedaro Community [Slack](https://join.slack.com/t/sedaro-community/shared_invite/zt-1jps4i711-mXy88AZQ9AV7YcEXr8x7Ow) 2. Email us at support@sedarotech.com  ### Known Issues  - Error responses are more specific than what is shown throughout the documentation.  A 4xx or 5xx error will be returned in all error cases.  Only a `200` status indicates success.  See a given error response for additional details.   # noqa: E501

    The version of the OpenAPI document: 4.5.2
    Generated by: https://openapi-generator.tech
"""

from sedaro_base_client.paths.models_branches_branch_id_commits_.post import CommitToBranch
from sedaro_base_client.paths.models_branches_branch_id.post import CreateBranch
from sedaro_base_client.paths.models_branches_branch_id.delete import DeleteBranch
from sedaro_base_client.paths.models_branches_branch_id_export_.get import ExportBranch
from sedaro_base_client.paths.models_branches_branch_id.get import GetBranch
from sedaro_base_client.paths.models_branches_branch_id_changes_.get import GetBranchChanges
from sedaro_base_client.paths.models_branches_branch_id_committed_.get import GetCommittedBranchData
from sedaro_base_client.paths.models_branches_branch_id_saved_.get import GetSavedBranchData
from sedaro_base_client.paths.models_branches_current_branch_id_merge_incoming_branch_id.post import MergeBranches
from sedaro_base_client.paths.models_branches_branch_id.patch import UpdateBranch
from sedaro_base_client.paths.models_branches_branch_id_share_auth_.post import VerifyBranchPassword


class BranchesApi(
    CommitToBranch,
    CreateBranch,
    DeleteBranch,
    ExportBranch,
    GetBranch,
    GetBranchChanges,
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
