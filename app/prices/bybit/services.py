from app.prices.bybit.connectors import BybitConnector


class BybitService:
    def __init__(self, connector: BybitConnector) -> None:
        self.connector = connector

    async def get_prices(self):
        return await self.connector.get_prices()
