from pydantic import BaseModel


class Text(BaseModel):
    input_text: str = ""
    translation_language: str
    input_language: str = "auto"


class TTS(BaseModel):
    text: str
    language: str = "en"
    speed: str = "slow"
