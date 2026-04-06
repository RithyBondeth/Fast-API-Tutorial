from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr, BeforeValidator, ConfigDict
from typing_extensions import Annotated

PyObjectId = Annotated[str, BeforeValidator(str)]


class UserSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0)
    role: Optional[str] = "user"  # Default Role

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class UserUpdateSchema(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0)
    role: Optional[str] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class UserResponseSchema(BaseModel):
    message: str
    data: Optional[UserSchema] = None


class AllUserResponseSchema(BaseModel):
    message: str
    data: List[UserSchema]
