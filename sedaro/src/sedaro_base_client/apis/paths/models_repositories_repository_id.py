from sedaro_base_client.paths.models_repositories_repository_id.get import ApiForget
from sedaro_base_client.paths.models_repositories_repository_id.delete import ApiFordelete
from sedaro_base_client.paths.models_repositories_repository_id.patch import ApiForpatch


class ModelsRepositoriesRepositoryId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
