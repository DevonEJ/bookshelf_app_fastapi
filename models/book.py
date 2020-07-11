from pydantic import BaseModel


class Book(BaseModel):
    id: str
    name: str
    isbn: str
    author_name: str
    read_count: int
