from sedaro_base_client.paths.branches_branch_id.get import ApiForget
from sedaro_base_client.paths.branches_branch_id.post import ApiForpost
from sedaro_base_client.paths.branches_branch_id.delete import ApiFordelete
from sedaro_base_client.paths.branches_branch_id.patch import ApiForpatch


class BranchesBranchId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForpatch,
):
    pass
