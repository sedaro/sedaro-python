# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from sedaro_base_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    MODELS_BRANCHES_BRANCH_ID_TEMPLATE = "/models/branches/{branchId}/template"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_ = "/simulations/branches/{branchId}/control/"
    SIMULATIONS_BRANCHES_BRANCH_ID_CONTROL_JOB_ID = "/simulations/branches/{branchId}/control/{jobId}"
    SIMULATIONS_JOBS_JOB_ID_EXTERNALS_AGENT_ID_EXTERNAL_STATE_BLOCK_ID = "/simulations/jobs/{jobId}/externals/{agentId}/{externalStateBlockId}"
    DATA_ID = "/data/{id}"
    MODELS_BRANCHES_BRANCH_ID = "/models/branches/{branchId}"
    MODELS_BRANCHES_BRANCH_IDSHAREAUTH_ = "/models/branches/{branchId}share-auth/"
    MODELS_BRANCHES_BRANCH_IDCOMMITS_ = "/models/branches/{branchId}commits/"
    MODELS_BRANCHES_CURRENT_BRANCH_ID_MERGE_INCOMING_BRANCH_ID = "/models/branches/{currentBranchId}/merge/{incomingBranchId}"
    MODELS_BRANCHES_BRANCH_IDCOMMITTED_ = "/models/branches/{branchId}committed/"
    MODELS_BRANCHES_BRANCH_IDSAVED_ = "/models/branches/{branchId}saved/"
