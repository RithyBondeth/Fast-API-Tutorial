from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.api import api_router
from app.core.middleware import setup_logging, LoggingMiddleware
from app.core.exceptions import register_exception_handlers

# 1. Initialize logging
logger = setup_logging()

# 2. Initialize FastAPI app
app = FastAPI(
    title="FastAPI MongoDB Tutorial",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# 3. Add CORS Middleware (Essential for connecting to Frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Add Custom Logging Middleware
app.add_middleware(LoggingMiddleware)

# 5. Register Exception Handlers
register_exception_handlers(app)

# 6. Include API Routers
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI MongoDB Tutorial API!"}