from fastapi import APIRouter, Depends

from app.prices.binance.dependencies import get_binance_service
from app.prices.binance.services import BinanceService
from app.prices.bybit.dependencies import get_bybit_service
from app.prices.bybit.services import BybitService
from app.prices.schema import Token
from app.prices.utils import combine_prices, combine_prices_dict

router = APIRouter(prefix="/prices")


@router.get("/", responses={200: {"description": "Get all values prices"}})
async def get_all_prices(
    binance_service: BinanceService = Depends(get_binance_service),
    bybit_service: BybitService = Depends(get_bybit_service),
) -> list[Token]:
    binance_prices = await binance_service.get_prices()
    bybit_prices = await bybit_service.get_prices()

    return combine_prices(binance_prices, bybit_prices)


@router.get(
    "/{symbol}/",
    responses={200: {"description": "Get price of current value"}}
)
async def get_symbol_price(
    symbol: str,
    binance_service: BinanceService = Depends(get_binance_service),
    bybit_service: BybitService = Depends(get_bybit_service),
) -> Token:
    binance_prices = await binance_service.get_prices()
    bybit_prices = await bybit_service.get_prices()

    prices = combine_prices_dict(binance_prices, bybit_prices)
    return prices[symbol]
