from fastapi import FastAPI
from .routers import translate

app = FastAPI()

app.include_router(translate.router)


@app.get("/")
def home():
    return {"Status": 200, "Response": "Welcome to home page"}
