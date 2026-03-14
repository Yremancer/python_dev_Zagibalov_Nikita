from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions.exceptions import CustomHTTPException
from core.log import get_logger

logger = get_logger(__name__)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(CustomHTTPException)
    async def custom_handler(request: Request, exc: CustomHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail,
        )

    @app.exception_handler(Exception)
    async def global_handler(request: Request, exc: Exception):
        logger.exception("Exception: %s", exc)
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal Server Error",
                "error_code": "INTERNAL_SERVER_ERROR",
            },
        )
