from pydantic import BaseModel


class Text(BaseModel):
    input_text: str = ""
    translation_language: str
    input_language: str = "auto"
