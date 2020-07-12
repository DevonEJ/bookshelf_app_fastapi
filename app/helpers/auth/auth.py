import os
from passlib.context import CryptContext
from typing import Any, Dict
from dotenv import find_dotenv, load_dotenv
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
import jwt

from app.models.v1.jwt_user import JWTUser

load_dotenv(find_dotenv())

# Loaded from .env file via settings.py
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_AFTER_MINUTES = os.getenv("JWT_EXPIRE_AFTER_MINUTES")

password_context = CryptContext(schemes=["bcrypt"])

oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")


# Encryption and verification of passwords
def encrypt_password(password: str) -> CryptContext.__hash__:
    return password_context.hash(password)


def check_encrypted_password(plaintext_password: str, encrypted_password: CryptContext.__hash__) -> bool:
    try:
        return password_context.verify(plaintext_password, encrypted_password)
    except Exception as e:
        return False


fake_jwt_user = {"username": "test", "password": "", "disabled": False, "role": "customer"}
fake_jwt_user = JWTUser(**fake_jwt_user)


# Creation of JWT
def authenticate_user(user: JWTUser) -> Any:
    # If user is in the database
    if fake_jwt_user.username == user.username:
        if not fake_jwt_user.disabled:
            if check_encrypted_password(user.password, encrypt_password(fake_jwt_user.password)):
                # TODO - Remove after testing
                user.role = "administrator"
                return user
    return None


def create_jwt_token(user: JWTUser) -> Dict[str, Any]:
    expiration_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_AFTER_MINUTES)
    payload = {
        "username": user.username,
        "role": user.role,
        "exp": expiration_time
    }
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return {"token": token}


def verify_jwt_token(token: str = Depends(oauth_schema)) -> bool:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)

        # Extract attributes from jwt payload
        username = payload.get("sub")
        role = payload.get("role")
        expiration = payload.get("exp")

        # Check token has not expired
        if expiration < datetime.utcnow():
            # Check user exists in database
            if fake_jwt_user.username == username:
                return verify_user_role(role)

    except Exception as e:
        return False
    return False


def verify_user_role(role: str) -> bool:
    if role == "administrator":
        return True
    return False



