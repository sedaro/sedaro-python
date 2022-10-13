from sedaro_old.api_client import ApiClient
from .configuration import config
from .utils import parse_urllib_response
from .branch import Branch


class SedaroApiClient(ApiClient):
    def __init__(self, api_key, *args, **kwargs):
        return super().__init__(
            configuration=config,
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )

    def get_branch(self, branch_id: int) -> Branch:
        """Gets a Sedaro Branch based on the give `branch_id`. Must be accessible to this `SedaroApiClient` via the
        `api_key`.

        Args:
            branch_id (int): the id of the desired Sedaro Branch

        Returns:
            Branch: A `Branch` object that has various helpful methods on it.
        """
        res = self.call_api(f'/models/branches/{branch_id}', 'GET')
        return Branch(
            id=branch_id,
            data=parse_urllib_response(res)['data'],
            _sedaro_client=self
        )
