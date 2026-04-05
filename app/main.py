from fastapi import FastAPI
from app.api import product, user

app = FastAPI()

app.include_router(product.router)
app.include_router(user.router)
