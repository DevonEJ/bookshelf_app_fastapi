from fastapi import FastAPI, Body
from models.book import Book


app = FastAPI(openapi_prefix="/v1")


@app.get("/author/{id}/book")
async def get_author_books(id: str, category: str, order: str = "asc"):
    pass


@app.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"name in body: ": name}



