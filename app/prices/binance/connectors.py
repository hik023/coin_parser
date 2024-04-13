from pydantic import TypeAdapter

from app.prices.binance.schema import BinanceToken
from app.utils.connectors import AsyncServiceConnector


class BinanceConnector(AsyncServiceConnector):
    async def get_prices(self) -> BinanceToken:
        response = await self.client.get("/ticker/price")
        response.raise_for_status()

        ta = TypeAdapter(list[BinanceToken])
        return ta.validate_python(response.json())
