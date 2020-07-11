from fastapi import FastAPI, File
from models.user import User
from starlette.status import HTTP_201_CREATED

app_v1 = FastAPI(openapi_prefix="/v1")


@app_v1.post("/user", status_code=HTTP_201_CREATED)
async def create_user(user: User):
    print(user)


@app_v1.post("/user/image")
async def upload_book_image(user_image: bytes = File(...)):
    return {"File": user_image}







