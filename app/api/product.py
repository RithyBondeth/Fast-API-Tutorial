from app.schemas.product import ProductUpdateSchema
from bson import ObjectId
from app.schemas.product import AllProductResponseSchema
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.product import ProductSchema, SingleProductResponseSchema
from app.core.database import db
from app.core.deps import get_current_user

router = APIRouter(prefix="/products", tags=["products"], dependencies=[Depends(get_current_user)])


@router.post("", response_model=SingleProductResponseSchema)
async def create_product(product: ProductSchema):
    # This route is now protected! Only logged-in users can reach here.
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

@router.get("/{product_id}", response_model=SingleProductResponseSchema)
async def get_product_by_id(product_id: str):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID format")
    
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    if product is None: 
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": f"Get product with ID {product_id} Successfully", "data": product}

@router.put("/{product_id}", response_model=SingleProductResponseSchema)
async def update_product_by_id(product_id: str, product: ProductUpdateSchema):
    if not ObjectId.is_valid(product_id):
        raise HTTPException(status_code=400, detail="Invalid product ID format")

    update_data = product.model_dump(exclude_unset=True)
    result = await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": update_data})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
        
    updated_product = await db.products.find_one({"_id": ObjectId(product_id)})
    return {"message": f"Product with ID {product_id} Updated Successfully", "data": updated_product}