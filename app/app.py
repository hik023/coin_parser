from fastapi import FastAPI

from app.api import API_STR, api_router
from app.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOC_URL,
        openapi_url=settings.OPENAPI_URL,
    )
    app.state.settings = settings

    setup_routes(app)

    return app


def setup_routes(app: FastAPI) -> None:
    app.include_router(api_router, prefix=API_STR)
