from pydantic import BaseModel
from app.models.v1.book import Book


class Bookshelf(BaseModel):
    id: str
    owner: str
    books: [Book]
