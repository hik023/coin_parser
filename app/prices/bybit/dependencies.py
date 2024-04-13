from app.config import get_settings
from app.prices.bybit.connectors import BybitConnector
from app.prices.bybit.services import BybitService

bybit_connector = BybitConnector(
    base_url=get_settings().BYBIT.BASE_URL,
)


def get_bybit_service() -> BybitService:
    return BybitService(connector=bybit_connector)
