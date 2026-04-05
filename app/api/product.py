from app.schemas.product import AllProductResponseSchema
from fastapi import APIRouter
from app.schemas.product import ProductSchema, SingleProductResponseSchema
from app.core.database import db

router = APIRouter(prefix="/products", tags=["products"])


@router.post("", response_model=SingleProductResponseSchema)
async def create_product(product: ProductSchema):
    product_data = product.model_dump(by_alias=True, exclude_unset=True)
    if product_data.get("_id") is None:
        product_data.pop("_id", None)

    result = await db.products.insert_one(product_data)
    product.id = str(result.inserted_id)
    return {"message": "Product Created Successfully", "data": product}

@router.get("", response_model=AllProductResponseSchema)
async def get_all_products():
    products = await db.products.find().to_list(length=100)
    return {"message": "Get All Products Successfully", "data": products}