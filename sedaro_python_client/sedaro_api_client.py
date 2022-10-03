from .python_client.openapi_client import ApiClient, Configuration

config = Configuration(
    host='http://localhost:8000/',
)


class SedaroApiClient(ApiClient):
    def __init__(self, *args, api_key='', **kwargs):
        return super().__init__(
            configuration=config,
            *args,
            **kwargs,
            header_name='X_API_KEY',
            header_value=api_key
        )
