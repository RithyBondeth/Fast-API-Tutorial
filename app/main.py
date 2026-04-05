from fastapi import FastAPI
from app.api import product

app = FastAPI()

app.include_router(product.router)
