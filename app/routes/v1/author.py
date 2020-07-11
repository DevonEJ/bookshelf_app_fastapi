from fastapi import FastAPI, Body


app_v1 = FastAPI(openapi_prefix="/v1")


@app_v1.get("/author/{id}/book")
async def get_author_books(id: str, category: str, order: str = "asc"):
    pass


@app_v1.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"name in body: ": name}



