from typing import Optional, Any
from pydantic import BaseModel, EmailStr


class RegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class AuthResponseSchema(BaseModel):
    message: str
    data: Optional[Any] = None


class RefreshTokenSchema(BaseModel):
    refresh_token: str
