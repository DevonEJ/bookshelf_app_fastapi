from pydantic import BaseModel
from fastapi import Query
from models.shared import Role


class User(BaseModel):
    id: str
    name: str
    email: str = Query(..., regex='[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', title="Validate Email")
    role: Role
    bookshelf_id: str
