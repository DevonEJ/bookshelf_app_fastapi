from pydantic import BaseModel
from app.models.shared import Role


class JWTUser(BaseModel):
    username: str
    password: str
    disabled: bool = False
    role: Role = None
