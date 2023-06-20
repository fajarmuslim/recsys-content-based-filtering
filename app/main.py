from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.routes import recommender
from app.handler.exception import (
    InvalidAPIKeyException,
    invalid_key_exception_exception_handler,
)


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(recommender.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[get_settings().cors_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_exception_handler(
        InvalidAPIKeyException, invalid_key_exception_exception_handler
    )
    return app


app = get_app()
