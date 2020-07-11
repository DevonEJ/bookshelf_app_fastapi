from fastapi import FastAPI

app = FastAPI(openapi_prefix="/v1")


@app.get("/")
async def home():
    return {"Welcome to your virtual bookshelf!"}
