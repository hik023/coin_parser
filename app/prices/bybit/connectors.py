from pydantic import TypeAdapter

from app.prices.bybit.schema import BybitToken
from app.utils.connectors import AsyncServiceConnector


class BybitConnector(AsyncServiceConnector):
    async def get_prices(self) -> BybitToken:
        response = await self.client.get("/tickers")
        response.raise_for_status()

        ta = TypeAdapter(list[BybitToken])
        return ta.validate_python(response.json()["result"])
