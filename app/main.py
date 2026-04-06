from fastapi import FastAPI
from app.api.v1.api import api_router
from app.core.logging import setup_logging
from app.core.middleware import LoggingMiddleware
from app.core.handlers import register_exception_handlers

# 1. Initialize logging
logger = setup_logging()

# 2. Initialize FastAPI app
app = FastAPI(
    title="FastAPI MongoDB Tutorial", 
    version="1.0.0",
    docs_url="/docs",  # Explicitly standard
    redoc_url="/redoc"
)

# 3. Add Middleware
app.add_middleware(LoggingMiddleware)

# 4. Register Exception Handlers
register_exception_handlers(app)

# 5. Include API Routers
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB Tutorial API!"}