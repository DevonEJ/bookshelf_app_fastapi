from pydantic import BaseModel
from models.v1.book import Book


class Bookshelf(BaseModel):
    id: str
    owner: str
    books: [Book]
