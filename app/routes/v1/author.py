from fastapi import APIRouter, Body


router = APIRouter()


@router.get("/author/{id}/book")
async def get_author_books(id: str, category: str, order: str = "asc"):
    pass


@router.patch("/author/name")
async def patch_author_name(name: str = Body(..., embed=True)):
    return {"name in body: ": name}



