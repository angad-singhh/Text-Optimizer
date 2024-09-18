#  Text-Translator-and-Converter API

## Overview

The Language Optimizer API is a FastAPI-based application that provides functionality for multilingual text-to-speech conversion and multilingual text language translation. This project aims to enhance communication by allowing users to convert text into speech and translate text across multiple languages seamlessly.

## Features

- **Text-to-Speech (TTS)**: Convert written text any from multiple supported languages into AI generated speach in your prefered language.
- **Language Translation**: Translate text between multiple languages.
- **Multilingual Support**: Handle text in various languages for both TTS and translation.


## Endpoints

### Text-to-Speech

**Endpoint** : `/tts/languages` <br>
**Method** : `GET` <br>
**Response** :
  ```json
  {
    "Status": 200,
    "Supported languages": // list of all supported languages
  }
  ```

<br>
  
**Endpoint** : `/tts/convert` <br>
**Method** : `POST` <br>
**Request Body** :
  ```json
  {
    "text": str // text you wan to convert
    "language": str = "en" // desired language
    "speed": str = "slow"
  }
  ```
<br>
<hr>


### Text-Lnaguage-Translator

**Endpoint** : `/languages` <br>
**Method** : `GET` <br>
**Response** :
  ```json
  {
    "Status": 200,
    "Supported languages": // list of all supported languages
  }
  ```
**Response** : Audio file in MP3 format


<br>
  
**Endpoint** : `/translate` <br>
**Method** : `POST` <br>
**Request Body** :
  ```json
  {
    input_text: str = "" 
    translation_language: str // language in which you want translation
    input_language: str = "auto" // language of input text [Optional]
  }
```
**Response** : Translated text in JSON 

<br>
<hr>

## Connect with ME:

<a href="https://linkedin.com/in/angad-singhh" target="blank"><img align="center" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="angad-singhh" /></a>

<a href="mailto:angad.singh2605@gmail.com" target="blank"><img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="angad.singh2605@gmail.com" /></a>
