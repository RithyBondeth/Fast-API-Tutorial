from app.schemas.auth import (
    AuthResponseSchema,
    RegisterSchema,
    LoginSchema,
    RefreshTokenSchema,
)
from app.services.auth_service import AuthService
from fastapi import APIRouter, Depends
from app.core.deps import get_current_user

router = APIRouter()
auth_service = AuthService()


@router.post("/refresh", response_model=AuthResponseSchema)
async def refresh(refresh_data: RefreshTokenSchema):
    return await auth_service.refresh(refresh_data)


@router.get("/me", response_model=AuthResponseSchema)
async def get_me(user: dict = Depends(get_current_user)):
    return {"message": "Get Current User Successfully", "data": user}


@router.post("/register", response_model=AuthResponseSchema)
async def register(user: RegisterSchema):
    return await auth_service.register(user)


@router.post("/login", response_model=AuthResponseSchema)
async def login(login_data: LoginSchema):
    return await auth_service.login(login_data)
