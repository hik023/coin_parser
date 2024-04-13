from fastapi import APIRouter

from app.prices.views import router as prices_router

API_STR = "/api"

api_router = APIRouter()
api_router.include_router(prices_router, tags=["prices"])
