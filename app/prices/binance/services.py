from app.prices.binance.connectors import BinanceConnector


class BinanceService:
    def __init__(self, connector: BinanceConnector) -> None:
        self.connector = connector

    async def get_prices(self):
        return await self.connector.get_prices()
