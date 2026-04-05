from fastapi import FastAPI
from app.api import product, user

app = FastAPI()

# Product API
app.include_router(product.router)
# User API
app.include_router(user.router)
