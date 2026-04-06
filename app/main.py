from fastapi import FastAPI
from app.api import product, user, auth

app = FastAPI()

# Product API
app.include_router(product.router)
# User API
app.include_router(user.router)
# Auth API
app.include_router(auth.router)
