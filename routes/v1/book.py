from fastapi import FastAPI, File
from models.book import Book
from models.author import Author

app = FastAPI(openapi_prefix="/v1")


@app.get("/book/{isbn}", response_model=Book, response_model_exclude=["author"])
async def get_book_by_isbn(isbn: str):

    author_dict = {
            "id": "123",
            "name": "Tolkein",
            "country": "England",
            "gender": "male",
            "deceased": True,
            "books": ["0000"]
    }
    author = Author(**author_dict)

    book_dict = {
        "id": "0000",
        "name": "The Lord of the Rings",
        "isbn": "fgfg434233232",
        "author": author,
        "genre": "fantasy",
        "read_count": 5
    }
    book = Book(**book_dict)
    return book


#TODO Fix 'unable to parse request body' error
@app.post("/book/image")
async def upload_book_image(book_image: bytes = File(...)):
    return {"File": book_image}

