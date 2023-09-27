# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sedaro_base_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    MODELS_BRANCHES_BRANCH_ID_TEMPLATE = "/models/branches/{branchId}/template"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_ = "/simulations/branches/{branchId}/control/"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID = "/simulations/branches/{branchId}/control/{jobId}"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_STUDY_ = "/simulations/branches/{branchId}/control/study/"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_STUDY_JOB_ID = "/simulations/branches/{branchId}/control/study/{jobId}"
    SIMULATIONS_JOBS_JOB_ID_EXTERNALS_AGENT_ID_EXTERNAL_STATE_BLOCK_ID = "/simulations/jobs/{jobId}/externals/{agentId}/{externalStateBlockId}"
    DATA_ID = "/data/{id}"
    MODELS_REPOSITORIES_ = "/models/repositories/"
    MODELS_REPOSITORIES_REPOSITORY_ID = "/models/repositories/{repositoryId}"
    MODELS_REPOSITORIES__IMPORT = "/models/repositories//import"
    MODELS_BRANCHES_BRANCH_ID = "/models/branches/{branchId}"
    MODELS_BRANCHES_BRANCH_ID_SHAREAUTH_ = "/models/branches/{branchId}/share-auth/"
    MODELS_BRANCHES_BRANCH_ID_COMMITS_ = "/models/branches/{branchId}/commits/"
    MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID = "/models/branches/{currentBranchId}/merge/{incomingBranchId}"
    MODELS_BRANCHES_BRANCH_ID_COMMITTED_ = "/models/branches/{branchId}/committed/"
    MODELS_BRANCHES_BRANCH_ID_SAVED_ = "/models/branches/{branchId}/saved/"
    MODELS_BRANCHES_BRANCH_ID_CHANGES_ = "/models/branches/{branchId}/changes/"
    MODELS_BRANCHES_BRANCH_ID_EXPORT_ = "/models/branches/{branchId}/export/"
