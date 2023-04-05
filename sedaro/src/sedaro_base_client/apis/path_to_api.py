import typing_extensions

from sedaro_base_client.paths import PathValues
from sedaro_base_client.apis.paths.models_branches_branch_id_template import ModelsBranchesBranchIdTemplate
from sedaro_base_client.apis.paths.simulations_branches_branch_id_control_ import SimulationsBranchesBranchIdControl
from sedaro_base_client.apis.paths.simulations_branches_branch_id_control_job_id import SimulationsBranchesBranchIdControlJobId
from sedaro_base_client.apis.paths.data_ import Data
from sedaro_base_client.apis.paths.models_branches_branch_id import ModelsBranchesBranchId
from sedaro_base_client.apis.paths.models_branches_branch_idshare_auth_ import ModelsBranchesBranchIdshareAuth
from sedaro_base_client.apis.paths.models_branches_branch_idcommits_ import ModelsBranchesBranchIdcommits
from sedaro_base_client.apis.paths.models_branches_current_branch_id_merge_incoming_branch_id import ModelsBranchesCurrentBranchIdMergeIncomingBranchId
from sedaro_base_client.apis.paths.models_branches_branch_idcommitted_ import ModelsBranchesBranchIdcommitted
from sedaro_base_client.apis.paths.models_branches_branch_idsaved_ import ModelsBranchesBranchIdsaved

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.MODELS_BRANCHES_BRANCH_ID_TEMPLATE: ModelsBranchesBranchIdTemplate,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_: SimulationsBranchesBranchIdControl,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID: SimulationsBranchesBranchIdControlJobId,
        PathValues.DATA_: Data,
        PathValues.MODELS_BRANCHES_BRANCH_ID: ModelsBranchesBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_IDSHAREAUTH_: ModelsBranchesBranchIdshareAuth,
        PathValues.MODELS_BRANCHES_BRANCH_IDCOMMITS_: ModelsBranchesBranchIdcommits,
        PathValues.MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID: ModelsBranchesCurrentBranchIdMergeIncomingBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_IDCOMMITTED_: ModelsBranchesBranchIdcommitted,
        PathValues.MODELS_BRANCHES_BRANCH_IDSAVED_: ModelsBranchesBranchIdsaved,
    }
)

path_to_api = PathToApi(
    {
        PathValues.MODELS_BRANCHES_BRANCH_ID_TEMPLATE: ModelsBranchesBranchIdTemplate,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_: SimulationsBranchesBranchIdControl,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID: SimulationsBranchesBranchIdControlJobId,
        PathValues.DATA_: Data,
        PathValues.MODELS_BRANCHES_BRANCH_ID: ModelsBranchesBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_IDSHAREAUTH_: ModelsBranchesBranchIdshareAuth,
        PathValues.MODELS_BRANCHES_BRANCH_IDCOMMITS_: ModelsBranchesBranchIdcommits,
        PathValues.MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID: ModelsBranchesCurrentBranchIdMergeIncomingBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_IDCOMMITTED_: ModelsBranchesBranchIdcommitted,
        PathValues.MODELS_BRANCHES_BRANCH_IDSAVED_: ModelsBranchesBranchIdsaved,
    }
)
