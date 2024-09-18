from fastapi import FastAPI
from .routers import translate, text_to_speach

app = FastAPI()

app.include_router(translate.router)
app.include_router(text_to_speach.router)


@app.get("/")
def home():
    return {"Status": 200, "Response": "Welcome to home page"}
