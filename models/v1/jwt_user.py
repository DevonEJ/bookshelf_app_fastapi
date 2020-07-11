from pydantic import BaseModel
from models.shared import Role


class User(BaseModel):
    username: str
    password: str
    disabled: bool
    role: Role
