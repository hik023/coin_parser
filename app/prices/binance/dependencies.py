from app.config import get_settings
from app.prices.binance.connectors import BinanceConnector
from app.prices.binance.services import BinanceService

binance_connector = BinanceConnector(
    base_url=get_settings().BINANCE.BASE_URL,
)


def get_binance_service() -> BinanceService:
    return BinanceService(connector=binance_connector)
