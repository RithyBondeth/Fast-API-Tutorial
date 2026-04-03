from fastapi import FastAPI
from api import product

app = FastAPI()

app.include_router(product.router)