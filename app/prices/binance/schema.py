from pydantic import BaseModel


class BinanceToken(BaseModel):
    symbol: str
    price: float
