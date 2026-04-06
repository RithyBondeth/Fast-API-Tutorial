from typing import Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from app.schemas.product import (
    ProductSchema,
    ProductUpdateSchema,
    SingleProductResponseSchema,
    AllProductResponseSchema,
)
from app.services.product_service import ProductService
from app.core.deps import get_current_user

router = APIRouter()
product_service = ProductService()


@router.post(
    "", response_model=SingleProductResponseSchema, dependencies=[Depends(get_current_user)]
)
async def create_product(product: ProductSchema):
    new_product = await product_service.create_product(product)
    return {"message": "Product Created Successfully", "data": new_product}


@router.get(
    "", response_model=AllProductResponseSchema, dependencies=[Depends(get_current_user)]
)
async def get_all_products(
    page: int = Query(1, ge=1), limit: int = Query(10, ge=1), search: Optional[str] = None
):
    products = await product_service.get_all_products(page, limit, search)
    return {
        "message": "Get All Products Successfully",
        "page": page,
        "limit": limit,
        "data": products,
    }


@router.get(
    "/{product_id}",
    response_model=SingleProductResponseSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_product_by_id(product_id: str):
    product = await product_service.get_product_by_id(product_id)
    return {
        "message": f"Get product with ID {product_id} Successfully",
        "data": product,
    }


@router.put(
    "/{product_id}",
    response_model=SingleProductResponseSchema,
    dependencies=[Depends(get_current_user)],
)
async def update_product_by_id(product_id: str, product_update: ProductUpdateSchema):
    updated_product = await product_service.update_product(product_id, product_update)
    return {
        "message": f"Product with ID {product_id} Updated Successfully",
        "data": updated_product,
    }
