from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"])


def encrypt_password(password: str) -> CryptContext.__hash__:
    return password_context.hash(password)


def check_encrypted_password(plaintext_password: str, encrypted_password: CryptContext.__hash__) -> bool:
    return password_context.verify(plaintext_password, encrypted_password)
