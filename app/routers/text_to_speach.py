from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
import requests
from ..models.models import TTS
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("X-RAPIDAPI-KEY")

if not uri:
    raise ValueError("Please check your API key")

router = APIRouter(prefix="/tts", tags=["Text to Speach"])


@router.get("/languages")
def get_supported_languages():
    url = "https://text-to-speach-api.p.rapidapi.com/supported-languages"

    headers = {
        "x-rapidapi-key": uri,
        "x-rapidapi-host": "text-to-speach-api.p.rapidapi.com",
    }
    response = requests.get(url, headers=headers)
    return {"Status": 200, "Supported languages": response.json()}


@router.post("/convert")
def convert_text_to_speach(tts: TTS):
    data = tts.model_dump()
    url = "https://text-to-speach-api.p.rapidapi.com/text-to-speech"

    payload = {"text": data["text"], "lang": data["language"], "speed": data["speed"]}
    headers = {
        "x-rapidapi-key": uri,
        "x-rapidapi-host": "text-to-speach-api.p.rapidapi.com",
        "Content-Type": "application/json",
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    audio_content = response.content

    return StreamingResponse(
        BytesIO(audio_content),
        media_type="audio/mpeg",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Content-Disposition": "attachment; filename=audio.mp3",
        },
    )
