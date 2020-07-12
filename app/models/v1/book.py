from pydantic import BaseModel
from app.models.v1.author import Author


class Book(BaseModel):
    id: str
    name: str
    isbn: str
    author: Author
    genre: str
    read_count: int
