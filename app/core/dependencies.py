from bson import ObjectId
from app.core.security import ALGORITHM
from app.core.security import SECRET_KEY
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from app.db.mongodb import db
import jwt


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        # 1. Check if user_id exists and is a valid MongoDB ID
        if not user_id or not ObjectId.is_valid(user_id):
            raise HTTPException(status_code=401, detail="Invalid token payload")

    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    # 2. Fetch the user
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 3. Clean up the data (for serialization)
    user["id"] = str(user["_id"])
    del user["_id"]
    if "password" in user:
        del user["password"]  # Security: Don't pass the password around!

    return user


def require_role(required_role: str):
    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role") != required_role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user

    return role_checker
