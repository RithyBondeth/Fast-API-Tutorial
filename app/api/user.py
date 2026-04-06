from bson import ObjectId
from fastapi import APIRouter, HTTPException, Depends
from app.core.database import db
from app.schemas.user import (
    UserSchema,
    AllUserResponseSchema,
    UserResponseSchema,
    UserUpdateSchema,
)
from app.core.deps import require_role

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponseSchema)
async def create_user(user: UserSchema):
    # motor will add _id to the dict if we use model_dump(by_alias=True) or exclude_none=True
    # but here we just want to insert the Pydantic model's data
    user_data = user.model_dump(by_alias=True, exclude_unset=True)
    if user_data.get("_id") is None:
        user_data.pop("_id", None)

    result = await db.users.insert_one(user_data)
    user.id = str(result.inserted_id)
    return {"message": "User Created Successfully", "data": user}


@router.get("", response_model=AllUserResponseSchema)
async def get_all_users():
    users = await db.users.find().to_list(length=100)
    return {"message": "Get All Users Successfully", "data": users}


@router.get("/{user_id}", response_model=UserResponseSchema)
async def get_user_by_id(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Get user with ID {user_id} Successfully", "data": user}


@router.put("/{user_id}", response_model=UserResponseSchema)
async def update_user_by_id(user_id: str, user: UserUpdateSchema):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    update_data = user.model_dump(exclude_unset=True)
    result = await db.users.update_one(
        {"_id": ObjectId(user_id)}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
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
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"Delete user with ID {user_id} Successfully", "data": None}
