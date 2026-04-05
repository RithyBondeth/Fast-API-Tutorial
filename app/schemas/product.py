from typing import List, Any
from pydantic import BaseModel, Field
from typing import Optional


class ReviewSchema(BaseModel):
    user: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class ProductSchema(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    reviews: List[ReviewSchema] = []


class ProductResponseSchema(BaseModel):
    message: str
    data: List[ProductSchema]


class SingleProductResponseSchema(BaseModel):
    message: str
    data: ProductSchema
