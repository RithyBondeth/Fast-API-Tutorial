import jwt
from bson import ObjectId
from app.schemas.auth import LoginSchema, RegisterSchema, RefreshTokenSchema
from app.core.database import db
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    SECRET_KEY,
    ALGORITHM,
)
from app.core.exceptions import UnauthorizedException, BadRequestException, NotFoundException


class AuthService:
    async def refresh(self, refresh_data: RefreshTokenSchema):
        try:
            # 1. Decode and validate the refresh token
            payload = jwt.decode(
                refresh_data.refresh_token, SECRET_KEY, algorithms=[ALGORITHM]
            )
            user_id = payload.get("user_id")
            if not user_id:
                raise UnauthorizedException("Invalid refresh token")
        except jwt.PyJWTError:
            raise UnauthorizedException("Invalid or expired refresh token")

        # 2. Verify the user still exists in the database
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise NotFoundException("User not found")

        # 3. Create new tokens (Token Rotation)
        new_access_token = create_access_token({"user_id": str(user["_id"])})
        new_refresh_token = create_refresh_token({"user_id": str(user["_id"])})

        return {
            "message": "Token Refreshed Successfully",
            "data": {
                "access_token": new_access_token,
                "refresh_token": new_refresh_token,
                "token_type": "bearer",
            },
        }

    async def register(self, user_data: RegisterSchema):
        # 1. Check if user already exists
        existing_user = await db.users.find_one({"email": user_data.email})
        if existing_user:
            raise BadRequestException("User with this email already exists")

        # 2. Prepare data (convert schema to dict)
        new_user = user_data.model_dump()
        # Hash password before saving
        new_user["password"] = hash_password(user_data.password)

        # 3. Insert user into database
        result = await db.users.insert_one(new_user)

        # 4. Return clean response (exclude sensitive/non-serializable data)
        new_user["id"] = str(result.inserted_id)
        new_user.pop("password", None)
        new_user.pop("_id", None)  # MongoDB ObjectId is not JSON-serializable

        return {"message": "Registered Successfully", "data": new_user}

    async def login(self, login_data: LoginSchema):
        # 1. Look for the user
        user = await db.users.find_one({"email": login_data.email})

        # 2. Check existence and verify password
        # We use 401 for both to prevent user enumeration
        if not user or not verify_password(login_data.password, user["password"]):
            raise UnauthorizedException("Invalid Credentials")

        # 3. Create the access and refresh token
        access_token = create_access_token({"user_id": str(user["_id"])})
        refresh_token = create_refresh_token({"user_id": str(user["_id"])})

        # 4. Return standard response
        return {
            "message": "Login Successfully",
            "data": {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "token_type": "bearer",
            },
        }
