from pydantic import BaseModel
import enum


class Role(enum.Enum):
    admin: str = "administrator"
    customer: str = "customer"


class User(BaseModel):
    id: str
    name: str
    email: str
    role: Role
    bookshelf_id: str


