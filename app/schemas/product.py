from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
from app.schemas.user import PyObjectId


class ReviewSchema(BaseModel):
    user: str
    rating: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class ProductSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    name: str
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    reviews: List[ReviewSchema] = []

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class ProductUpdateSchema(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None
    reviews: Optional[List[ReviewSchema]] = []

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class AllProductResponseSchema(BaseModel):
    message: str
    data: Optional[List[ProductSchema]] = []


class SingleProductResponseSchema(BaseModel):
    message: str
    data: Optional[ProductSchema] = None
