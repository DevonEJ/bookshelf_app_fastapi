from fastapi import FastAPI

from .routes.v1 import author, book, home, user

app = FastAPI()

app.include_router(author.router, prefix="/v1")
app.include_router(book.router, prefix="/v1")
app.include_router(home.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")

