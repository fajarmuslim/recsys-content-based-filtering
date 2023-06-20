from fastapi import Request
from starlette.status import HTTP_401_UNAUTHORIZED
from fastapi.responses import JSONResponse
from app.utils.time import indo_now


class InvalidAPIKeyException(Exception):
    pass


async def invalid_key_exception_exception_handler(
    request: Request, exc: InvalidAPIKeyException
):
    return JSONResponse(
        status_code=HTTP_401_UNAUTHORIZED,
        content={
            "status": "unauthorized",
            "message": "please provide correct access_token",
            "data": None,
            "errors": ["header access_token"],
            "timestamp": int(indo_now().timestamp()),
        },
    )
