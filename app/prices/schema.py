from typing import Optional

from pydantic import BaseModel


class Price(BaseModel):
    binance: Optional[float]
    bybit: Optional[float]


class Token(BaseModel):
    name: str
    prices: Price
