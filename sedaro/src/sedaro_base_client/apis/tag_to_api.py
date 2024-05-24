import typing_extensions

from sedaro_base_client.apis.tags import TagValues
from sedaro_base_client.apis.tags.branches_api import BranchesApi
from sedaro_base_client.apis.tags.data_api import DataApi
from sedaro_base_client.apis.tags.metamodels_api import MetamodelsApi
from sedaro_base_client.apis.tags.externals_api import ExternalsApi
from sedaro_base_client.apis.tags.jobs_api import JobsApi
from sedaro_base_client.apis.tags.repositories_api import RepositoriesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.METAMODELS: MetamodelsApi,
        TagValues.EXTERNALS: ExternalsApi,
        TagValues.JOBS: JobsApi,
        TagValues.REPOSITORIES: RepositoriesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.METAMODELS: MetamodelsApi,
        TagValues.EXTERNALS: ExternalsApi,
        TagValues.JOBS: JobsApi,
        TagValues.REPOSITORIES: RepositoriesApi,
    }
)
