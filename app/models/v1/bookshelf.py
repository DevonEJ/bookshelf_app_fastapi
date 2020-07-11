from pydantic import BaseModel
from app.models import Book


class Bookshelf(BaseModel):
    id: str
    owner: str
    books: [Book]
