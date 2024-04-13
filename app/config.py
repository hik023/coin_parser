from functools import lru_cache
from typing import Optional

from pydantic import BaseModel
from pydantic_settings import BaseSettings


class BinanceSettings(BaseModel):
    BASE_URL: Optional[str] = ""


class BybitSettings(BaseModel):
    BASE_URL: Optional[str] = ""


class Settings(BaseSettings):
    PROJECT_NAME: str = "Coin parser"
    DOCS_URL: Optional[str] = "/docs"
    REDOC_URL: Optional[str] = "/redoc"
    OPENAPI_URL: Optional[str] = "/openapi.json"

    BINANCE: BinanceSettings = BinanceSettings()
    BYBIT: BybitSettings = BybitSettings()

    class Config:
        env_nested_delimiter = "__"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
