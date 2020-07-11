from fastapi import FastAPI
from models.user import User
from starlette.status import HTTP_201_CREATED

app = FastAPI()


@app.post("/user", status_code=HTTP_201_CREATED)
async def create_user(user: User):
    print(user)








