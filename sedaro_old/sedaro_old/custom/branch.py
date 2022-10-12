from typing import Dict
from dataclasses import dataclass
from sedaro_old.api_client import ApiClient


@dataclass
class Branch:
    id: int
    data: Dict
    sedaro_client: ApiClient

    def __str__(self):
        return f'Branch(id: {self.id})'
