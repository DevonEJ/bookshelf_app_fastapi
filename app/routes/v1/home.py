from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {"Welcome to your virtual bookshelf!"}
