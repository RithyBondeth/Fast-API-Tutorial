from fastapi import APIRouter, Depends, Query
from app.schemas.user import (
    UserSchema,
    AllUserResponseSchema,
    UserResponseSchema,
    UserUpdateSchema,
)
from app.services.user_service import UserService
from app.core.deps import require_role

router = APIRouter()
user_service = UserService()


@router.post("", response_model=UserResponseSchema)
async def create_user(user: UserSchema):
    new_user = await user_service.create_user(user)
    return {"message": "User Created Successfully", "data": new_user}


@router.get("", response_model=AllUserResponseSchema)
async def get_all_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    users = await user_service.get_all_users(page, limit)
    return {
        "message": "Get All Users Successfully",
        "page": page,
        "limit": limit,
        "data": users,
    }


@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user_by_id(user_id: str):
    user = await user_service.get_user_by_id(user_id)
    return {"message": f"Get user with ID {user_id} Successfully", "data": user}


@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_user_by_id(user_id: str, user_update: UserUpdateSchema):
    updated_user = await user_service.update_user(user_id, user_update)
    return {
        "message": f"Update user with ID {user_id} Successfully",
        "data": updated_user,
    }


@router.delete(
    "/{user_id}",
    response_model=UserResponseSchema,
    dependencies=[Depends(require_role("admin"))],
)
async def delete_user_by_id(user_id: str):
    await user_service.delete_user(user_id)
    return {"message": f"Delete user with ID {user_id} Successfully", "data": None}
