from fastapi import FastAPI

app_v1 = FastAPI(openapi_prefix="/v1")


@app_v1.get("/")
async def home():
    return {"Welcome to your virtual bookshelf!"}
