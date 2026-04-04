from fastapi import APIRouter
from schemas.product import ProductSchema

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=ProductSchema)
def create_product(product: ProductSchema):
    return product


@router.get("/", response_model=list[ProductSchema])
def get_all_products():
    return {
        "message": "Get All Products Successfully",
        "data": [
            {
                "id": 1,
                "name": "Product 1",
                "price": 100,
                "description": "Description 1",
            },
            {
                "id": 2,
                "name": "Product 2",
                "price": 200,
                "description": "Description 2",
            },
            {
                "id": 3,
                "name": "Product 3",
                "price": 300,
                "description": "Description 3",
            },
        ],
    }
