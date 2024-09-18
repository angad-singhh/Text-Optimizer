from fastapi import APIRouter
import requests
from ..models.models import Text
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("X-RAPIDAPI-KEY")

if not uri:
    raise ValueError("Please check your API key")

router = APIRouter(prefix="/translation", tags=["Language Transalation"])


@router.get("/languages")
def get_all_supported_languages():

    url = "https://ai-translate.p.rapidapi.com/languages"

    headers = {
        "x-rapidapi-key": uri,
        "x-rapidapi-host": "ai-translate.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers)

    return {"Response": response.json()}


@router.post("/translate")
def translate(text: Text):
    data = text.model_dump()
    sentences = data["input_text"].split(".")
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    url = "https://ai-translate.p.rapidapi.com/translate"
    payload = {
        "texts": sentences,
        "tl": data["translation_language"],
        "sl": data["input_language"],
    }
    headers = {
        "x-rapidapi-key": uri,
        "x-rapidapi-host": "ai-translate.p.rapidapi.com",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    return {"Transalated Text": response.json()}
