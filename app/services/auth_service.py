from app.schemas.auth import LoginSchema, RegisterSchema
from app.core.database import db
from app.core.security import hash_password, verify_password, create_access_token
from fastapi import HTTPException


class AuthService:

    async def register(self, user_data: RegisterSchema):
        # 1. Check if user already exists
        existing_user = await db.users.find_one({"email": user_data.email})
        if existing_user:
            raise HTTPException(
                status_code=400, detail="User with this email already exists"
            )

        # 2. Prepare data (convert schema to dict)
        new_user = user_data.model_dump()
        # Hash password before saving
        new_user["password"] = hash_password(user_data.password)

        # 3. Insert user into database
        result = await db.users.insert_one(new_user)
        
        # 4. Return clean response (exclude password)
        new_user["id"] = str(result.inserted_id)
        new_user.pop("password", None)
        
        return {"message": "Registered Successfully", "data": new_user}

    async def login(self, login_data: LoginSchema):
        # 1. Look for the user
        user = await db.users.find_one({"email": login_data.email})

        # 2. Check existence and verify password
        # We use 401 for both to prevent user enumeration
        if not user or not verify_password(login_data.password, user["password"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        # 3. Create the token
        access_token = create_access_token({"user_id": str(user["_id"])})

        # 4. Return standard response
        return {
            "message": "Login Successfully",
            "data": {"access_token": access_token, "token_type": "bearer"},
        }
