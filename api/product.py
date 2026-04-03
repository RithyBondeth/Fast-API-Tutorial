from fastapi import APIRouter
from schemas.product import ProductSchema

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductSchema)
def create_product(product: ProductSchema):
    return product

@router.get("/")
def get_all_products():
    return { "message": "Get All Products Successfully" }