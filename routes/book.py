from fastapi import FastAPI
from models.book import Book

app = FastAPI()


@app.get("/book/{isbn}")
async def get_book_by_isbn(isbn: str):
    return {f"Book by isbn endpoint hit: {isbn}"}
    pass


