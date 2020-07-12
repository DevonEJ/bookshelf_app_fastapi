import os
from passlib.context import CryptContext
from dotenv import find_dotenv, load_dotenv

from app.models.v1.jwt_user import JWTUser

load_dotenv(find_dotenv())

# Loaded from .env file via settings.py
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_AFTER_MINUTES = os.getenv("JWT_EXPIRE_AFTER_MINUTES")

password_context = CryptContext(schemes=["bcrypt"])


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
def authenticate_user(username: str, password: str) -> bool:
    # If user is in the database
    if fake_jwt_user.username == username:
        if not fake_jwt_user.disabled:
            if check_encrypted_password(password, encrypt_password(fake_jwt_user.password)):
                return True

    return False


def create_jwt_token(username: str):
    pass

