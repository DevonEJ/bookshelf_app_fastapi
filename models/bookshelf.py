from pydantic import BaseModel
from models.book import Book


class Bookshelf(BaseModel):
    id: str
    owner: str
    books: [Book]
