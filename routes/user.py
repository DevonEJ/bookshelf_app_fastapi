from fastapi import FastAPI
from models.user import User

app = FastAPI()


@app.post("/user")
async def create_user(user: User):
    print(user)








