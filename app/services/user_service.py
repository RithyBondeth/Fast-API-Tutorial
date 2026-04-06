from typing import Optional, List
from bson import ObjectId
from app.core.database import db
from app.schemas.user import UserSchema, UserUpdateSchema
from app.core.exceptions import NotFoundException, BadRequestException


class UserService:
    async def create_user(self, user: UserSchema):
        user_data = user.model_dump(by_alias=True, exclude_unset=True)
        if user_data.get("_id") is None:
            user_data.pop("_id", None)

        result = await db.users.insert_one(user_data)
        user.id = str(result.inserted_id)
        return user

    async def get_all_users(self, page: int, limit: int) -> List[dict]:
        skip = (page - 1) * limit
        return await db.users.find().skip(skip).limit(limit).to_list(length=limit)

    async def get_user_by_id(self, user_id: str) -> dict:
        if not ObjectId.is_valid(user_id):
            raise BadRequestException("Invalid user ID format")

        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise NotFoundException(f"User with ID {user_id} not found")
        return user

    async def update_user(
        self, user_id: str, user_update: UserUpdateSchema
    ) -> dict:
        if not ObjectId.is_valid(user_id):
            raise BadRequestException("Invalid user ID format")

        update_data = user_update.model_dump(exclude_unset=True)
        result = await db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": update_data}
        )

        if result.matched_count == 0:
            raise NotFoundException(f"User with ID {user_id} not found")

        return await db.users.find_one({"_id": ObjectId(user_id)})

    async def delete_user(self, user_id: str) -> bool:
        if not ObjectId.is_valid(user_id):
            raise BadRequestException("Invalid user ID format")

        result = await db.users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0:
            raise NotFoundException(f"User with ID {user_id} not found")
        return True
