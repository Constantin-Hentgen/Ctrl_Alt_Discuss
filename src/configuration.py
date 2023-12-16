from os import getenv

ROOT_PATH = getenv("POETRY_CAD_ROOT_PATH")
OUTPUT_PATH = rf"{ROOT_PATH}\output"

GPT_MODEL = "gpt-3.5-turbo-1106"
IMAGE_MODEL = "dall-e-3"
OPENAI_API_KEY = getenv("POETRY_OPENAI_API_KEY")
XI_API_KEY = getenv("POETRY_XI_API_KEY")

OPENAI_TTS_MODEL = "tts-1-hd"
XI_TTS_MODEL = "eleven_multilingual_v2"
PLAN_SIZE = 3
