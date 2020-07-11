from passlib.context import CryptContext

from app.models.v1.jwt_user import JWTUser


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
fake_jwt_user = JWTUser(fake_jwt_user)


print(encrypt_password("password"))


# Creation of JWT
def authenticate_user(username: str, password: str):
    pass

