import typing_extensions

from sedaro_base_client.apis.tags import TagValues
from sedaro_base_client.apis.tags.branches_api import BranchesApi
from sedaro_base_client.apis.tags.data_api import DataApi
from sedaro_base_client.apis.tags.templates_api import TemplatesApi
from sedaro_base_client.apis.tags.externals_api import ExternalsApi
from sedaro_base_client.apis.tags.jobs_api import JobsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.EXTERNALS: ExternalsApi,
        TagValues.JOBS: JobsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.BRANCHES: BranchesApi,
        TagValues.DATA: DataApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.EXTERNALS: ExternalsApi,
        TagValues.JOBS: JobsApi,
    }
)
