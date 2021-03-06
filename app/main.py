from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_401_UNAUTHORIZED

from .routes.v1 import author, book, home, user
from .helpers.auth.auth import authenticate_user, create_jwt_token
from .models.v1.jwt_user import JWTUser

app = FastAPI()


# TODO - Move token endpoint into v1 routes

@app.post("/token")
async def login_for_access_token(oauth_form: OAuth2PasswordRequestForm = Depends()):
    user_dict = {"username": oauth_form.username, "password": oauth_form.password}
    unauth_user = JWTUser(**user_dict)

    jwt_user = authenticate_user(unauth_user)
    if jwt_user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)
    else:
        return create_jwt_token(jwt_user)


app.include_router(author.router, prefix="/v1")
app.include_router(book.router, prefix="/v1")
app.include_router(home.router, prefix="/v1")
app.include_router(user.router, prefix="/v1")

