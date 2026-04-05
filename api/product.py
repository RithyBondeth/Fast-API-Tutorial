from fastapi import APIRouter
from schemas.product import ProductSchema, ProductResponseSchema, SingleProductResponseSchema
from data.product import products

router = APIRouter(prefix="/products", tags=["products"])


@router.post("/", response_model=SingleProductResponseSchema)
def create_product(product: ProductSchema):
    if product.id is None:
        product.id = len(products) + 1
    products.append(product)
    return {
        "message": "Product Created Successfully",
        "data": product,
    }


@router.get("/", response_model=ProductResponseSchema)
def get_all_products():
    return {
        "message": "Get All Products Successfully",
        "data": products,
    }


@router.get("/{product_id}", response_model=SingleProductResponseSchema)
def get_product_by_id(product_id: int):
    if(product_id > len(products)):
        raise HTTPException(status_code=404, detail="Product not found")
    return {
        "message": f"Get Product with ID {product_id} Successfully",
        "data": products[product_id -1],
    }

@router.put("/{product_id}", response_model=SingleProductResponseSchema)
def update_product_by_id(product_id: int, product: ProductSchema):
    if(product_id > len(products)):
        raise HTTPException(status_code=404, detail="Product not found")
    
    products[product_id - 1] = product
    product.id = product_id

    return {
        "message": f"Update Product with ID {product_id} Successfully",
        "data": products[product_id -1],
    }

@router.delete("/{product_id}")
def delete_product_by_id(product_id: int):
    if(product_id > len(products)):
        raise HTTPException(status_code=404, detail="Product not found")
    
    products.pop(product_id - 1)
    return {
        "message": f"Delete Product with ID {product_id} Successfully",
    }