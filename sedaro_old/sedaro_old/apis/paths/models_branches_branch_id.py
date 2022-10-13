from sedaro_old.paths.models_branches_branch_id.get import ApiForget
from sedaro_old.paths.models_branches_branch_id.post import ApiForpost
from sedaro_old.paths.models_branches_branch_id.delete import ApiFordelete
from sedaro_old.paths.models_branches_branch_id.patch import ApiForpatch


class ModelsBranchesBranchId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
