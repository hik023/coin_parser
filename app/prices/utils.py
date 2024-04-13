from app.prices.binance.schema import BinanceToken
from app.prices.bybit.schema import BybitToken
from app.prices.schema import Price, Token


# we can cache here
def combine_prices(
    binance_data: list[BinanceToken],
    bybit_data: list[BybitToken],
) -> list[Token]:
    binance_data.sort(key=lambda x: x.symbol)
    bybit_data.sort(key=lambda x: x.symbol)

    return [
        Token(
            name=binance.symbol,
            prices=Price(binance=binance.price, bybit=bybit.last_price),
        )
        for binance, bybit in zip(binance_data, bybit_data)
    ]


def combine_prices_dict(
    binance_data: list[BinanceToken],
    bybit_data: list[BybitToken],
) -> dict[str, Token]:
    binance_data.sort(key=lambda x: x.symbol)
    bybit_data.sort(key=lambda x: x.symbol)

    return {
        binance.symbol: Token(
            name=binance.symbol,
            prices=Price(binance=binance.price, bybit=bybit.last_price),
        )
        for binance, bybit in zip(binance_data, bybit_data)
    }
