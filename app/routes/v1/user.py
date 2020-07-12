from fastapi import APIRouter, File
from app.models.v1.user import User
from starlette.status import HTTP_201_CREATED

router = APIRouter()


@router.post("/user", status_code=HTTP_201_CREATED)
async def create_user(user: User):
    print(user)


@router.post("/user/image")
async def upload_book_image(user_image: bytes = File(...)):
    return {"File": user_image}







