from typing_extensions import deprecated
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta 

SECRET_KEY = "supersecret"
ALGORITHM = "HS256"

pwd_context = CryptContext(
    schemes=["bcrypt"], 
    deprecated="auto",
    truncate_error=False  # This allows passwords > 72 chars by truncating them
)

#Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify Password
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Create JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

