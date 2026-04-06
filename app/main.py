from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from app.api.v1.api import api_router
from app.core.exceptions import AppBaseException

app = FastAPI(title="FastAPI MongoDB Tutorial", version="1.0.0")

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(AppBaseException)
async def app_base_exception_handler(request: Request, exc: AppBaseException):
    """
    This handles all our custom exceptions (NotFound, Unauthorized, etc.)
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message, "status": "error"},
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    This handles standard FastAPI / Starlette HTTP exceptions.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail, "status": "error"},
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """
    This is a catch-all for any unexpected errors.
    It prevents the internal server error (500) from leaking details.
    """
    # In a real app, you would log 'exc' here.
    return JSONResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred. Please try again later.",
            "status": "error",
        },
    )