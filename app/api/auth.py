from app.schemas.auth import AuthResponseSchema, RegisterSchema, LoginSchema
from app.services.auth_service import AuthService
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

auth_service = AuthService()

@router.post("/register", response_model=AuthResponseSchema)
async def register(user: RegisterSchema):
    return await auth_service.register(user)

@router.post("/login", response_model=AuthResponseSchema)
async def login(login_data: LoginSchema):
    return await auth_service.login(login_data)