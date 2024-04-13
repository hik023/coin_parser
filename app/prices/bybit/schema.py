from pydantic import BaseModel


class BybitToken(BaseModel):
    symbol: str
    last_price: float
