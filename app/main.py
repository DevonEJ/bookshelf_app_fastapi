from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from .routes.v1 import author, book, home, user

app = FastAPI()

oauth_schema = OAuth2PasswordBearer(tokenUrl="/token")


@app.post("/token")
async def login_for_access_token(oauth_form: OAuth2PasswordRequestForm = Depends()):
    pass


app.include_router(author.router, prefix="/v1")
app.include_router(book.router, prefix="/v1")
app.include_router(home.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")

