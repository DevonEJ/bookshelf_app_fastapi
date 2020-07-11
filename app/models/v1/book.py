from pydantic import BaseModel
from app.models import Author


class Book(BaseModel):
    id: str
    name: str
    isbn: str
    author: Author
    genre: str
    read_count: int
