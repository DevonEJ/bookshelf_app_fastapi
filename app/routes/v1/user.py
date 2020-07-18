from fastapi import APIRouter, File, Header, Depends
from app.models.v1.user import User
from starlette.status import HTTP_201_CREATED
from app.helpers.auth.auth import verify_jwt_token

router = APIRouter()


@router.post("/user", status_code=HTTP_201_CREATED)
async def create_user(user: User, x_custom: str = Header("default"), jwt: bool = Depends(verify_jwt_token) ):
    return{"request body": user, "request custom header": x_custom}


@router.post("/user/image")
async def upload_book_image(user_image: bytes = File(...)):
    return {"File": user_image}







