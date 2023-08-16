import typing_extensions

from sedaro_base_client.paths import PathValues
from sedaro_base_client.apis.paths.models_branches_branch_id_template import ModelsBranchesBranchIdTemplate
from sedaro_base_client.apis.paths.simulations_branches_branch_id_control_ import SimulationsBranchesBranchIdControl
from sedaro_base_client.apis.paths.simulations_branches_branch_id_control_job_id import SimulationsBranchesBranchIdControlJobId
from sedaro_base_client.apis.paths.simulations_jobs_job_id_externals_agent_id_external_state_block_id import SimulationsJobsJobIdExternalsAgentIdExternalStateBlockId
from sedaro_base_client.apis.paths.data_id import DataId
from sedaro_base_client.apis.paths.models_repositories_ import ModelsRepositories
from sedaro_base_client.apis.paths.models_repositories_repository_id import ModelsRepositoriesRepositoryId
from sedaro_base_client.apis.paths.models_repositories__import import ModelsRepositoriesImport
from sedaro_base_client.apis.paths.models_branches_branch_id import ModelsBranchesBranchId
from sedaro_base_client.apis.paths.models_branches_branch_id_share_auth_ import ModelsBranchesBranchIdShareAuth
from sedaro_base_client.apis.paths.models_branches_branch_id_commits_ import ModelsBranchesBranchIdCommits
from sedaro_base_client.apis.paths.models_branches_current_branch_id_merge_incoming_branch_id import ModelsBranchesCurrentBranchIdMergeIncomingBranchId
from sedaro_base_client.apis.paths.models_branches_branch_id_committed_ import ModelsBranchesBranchIdCommitted
from sedaro_base_client.apis.paths.models_branches_branch_id_saved_ import ModelsBranchesBranchIdSaved
from sedaro_base_client.apis.paths.models_branches_branch_id_changes_ import ModelsBranchesBranchIdChanges
from sedaro_base_client.apis.paths.models_branches_branch_id_export_ import ModelsBranchesBranchIdExport

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.MODELS_BRANCHES_BRANCH_ID_TEMPLATE: ModelsBranchesBranchIdTemplate,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_: SimulationsBranchesBranchIdControl,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID: SimulationsBranchesBranchIdControlJobId,
        PathValues.SIMULATIONS_JOBS_JOB_ID_EXTERNALS_AGENT_ID_EXTERNAL_STATE_BLOCK_ID: SimulationsJobsJobIdExternalsAgentIdExternalStateBlockId,
        PathValues.DATA_ID: DataId,
        PathValues.MODELS_REPOSITORIES_: ModelsRepositories,
        PathValues.MODELS_REPOSITORIES_REPOSITORY_ID: ModelsRepositoriesRepositoryId,
        PathValues.MODELS_REPOSITORIES__IMPORT: ModelsRepositoriesImport,
        PathValues.MODELS_BRANCHES_BRANCH_ID: ModelsBranchesBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_ID_SHAREAUTH_: ModelsBranchesBranchIdShareAuth,
        PathValues.MODELS_BRANCHES_BRANCH_ID_COMMITS_: ModelsBranchesBranchIdCommits,
        PathValues.MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID: ModelsBranchesCurrentBranchIdMergeIncomingBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_ID_COMMITTED_: ModelsBranchesBranchIdCommitted,
        PathValues.MODELS_BRANCHES_BRANCH_ID_SAVED_: ModelsBranchesBranchIdSaved,
        PathValues.MODELS_BRANCHES_BRANCH_ID_CHANGES_: ModelsBranchesBranchIdChanges,
        PathValues.MODELS_BRANCHES_BRANCH_ID_EXPORT_: ModelsBranchesBranchIdExport,
    }
)

path_to_api = PathToApi(
    {
        PathValues.MODELS_BRANCHES_BRANCH_ID_TEMPLATE: ModelsBranchesBranchIdTemplate,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_: SimulationsBranchesBranchIdControl,
        PathValues.SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID: SimulationsBranchesBranchIdControlJobId,
        PathValues.SIMULATIONS_JOBS_JOB_ID_EXTERNALS_AGENT_ID_EXTERNAL_STATE_BLOCK_ID: SimulationsJobsJobIdExternalsAgentIdExternalStateBlockId,
        PathValues.DATA_ID: DataId,
        PathValues.MODELS_REPOSITORIES_: ModelsRepositories,
        PathValues.MODELS_REPOSITORIES_REPOSITORY_ID: ModelsRepositoriesRepositoryId,
        PathValues.MODELS_REPOSITORIES__IMPORT: ModelsRepositoriesImport,
        PathValues.MODELS_BRANCHES_BRANCH_ID: ModelsBranchesBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_ID_SHAREAUTH_: ModelsBranchesBranchIdShareAuth,
        PathValues.MODELS_BRANCHES_BRANCH_ID_COMMITS_: ModelsBranchesBranchIdCommits,
        PathValues.MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID: ModelsBranchesCurrentBranchIdMergeIncomingBranchId,
        PathValues.MODELS_BRANCHES_BRANCH_ID_COMMITTED_: ModelsBranchesBranchIdCommitted,
        PathValues.MODELS_BRANCHES_BRANCH_ID_SAVED_: ModelsBranchesBranchIdSaved,
        PathValues.MODELS_BRANCHES_BRANCH_ID_CHANGES_: ModelsBranchesBranchIdChanges,
        PathValues.MODELS_BRANCHES_BRANCH_ID_EXPORT_: ModelsBranchesBranchIdExport,
    }
)
