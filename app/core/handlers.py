import logging
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from app.core.exceptions import AppBaseException

logger = logging.getLogger("fast_api_tutorial")


def register_exception_handlers(app: FastAPI):
    """
    Register all custom and global exception handlers to the FastAPI app.
    """

    @app.exception_handler(AppBaseException)
    async def app_base_exception_handler(request: Request, exc: AppBaseException):
        logger.warning(f"App Exception: {exc.message} (Status: {exc.status_code})")
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.message, "status": "error"},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail, "status": "error"},
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Error: {str(exc)}", exc_info=True)
        return JSONResponse(
            status_code=500,
            content={
                "message": "An unexpected error occurred. Please try again later.",
                "status": "error",
            },
        )
