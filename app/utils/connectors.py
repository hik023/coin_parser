from typing import Any

from httpx import AsyncClient


class AsyncServiceConnector:
    client: AsyncClient

    def __init__(self, *, base_url: str, **kwargs: Any) -> None:
        self.base_url = base_url
        self.client = AsyncClient(base_url=base_url, **kwargs)
