from typing import Optional, List
from bson import ObjectId
from app.core.database import db
from app.schemas.product import ProductSchema, ProductUpdateSchema
from app.core.exceptions import NotFoundException, BadRequestException


class ProductService:
    async def create_product(self, product: ProductSchema):
        product_data = product.model_dump(by_alias=True, exclude_unset=True)
        if product_data.get("_id") is None:
            product_data.pop("_id", None)

        result = await db.products.insert_one(product_data)
        product.id = str(result.inserted_id)
        return product

    async def get_all_products(
        self, page: int, limit: int, search: Optional[str] = None
    ) -> List[dict]:
        skip = (page - 1) * limit
        query = {}
        if search:
            query["name"] = {"$regex": search, "$options": "i"}

        return (
            await db.products.find(query).skip(skip).limit(limit).to_list(length=limit)
        )

    async def get_product_by_id(self, product_id: str) -> dict:
        if not ObjectId.is_valid(product_id):
            raise BadRequestException("Invalid product ID format")

        product = await db.products.find_one({"_id": ObjectId(product_id)})
        if not product:
            raise NotFoundException(f"Product with ID {product_id} not found")
        return product

    async def update_product(
        self, product_id: str, product_update: ProductUpdateSchema
    ) -> dict:
        if not ObjectId.is_valid(product_id):
            raise BadRequestException("Invalid product ID format")

        update_data = product_update.model_dump(exclude_unset=True)
        result = await db.products.update_one(
            {"_id": ObjectId(product_id)}, {"$set": update_data}
        )

        if result.matched_count == 0:
            raise NotFoundException(f"Product with ID {product_id} not found")

        return await db.products.find_one({"_id": ObjectId(product_id)})
