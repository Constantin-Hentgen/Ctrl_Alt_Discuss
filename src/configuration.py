from dotenv import load_dotenv
from os import getenv

# Load environment variables from .env file, if it exists
load_dotenv()

ROOT_PATH = getenv("POETRY_CAD_ROOT_PATH")
OUTPUT_PATH = rf"{ROOT_PATH}\output"
GITHUB_REPO = "Ctrl_Alt_Discuss"
GITHUB_REPO_OWNER = "Constantin-Hentgen"

# API keys

OPENAI_API_KEY_LLM = getenv("POETRY_OPENAI_API_KEY_LLM")
OPENAI_API_KEY_IMG = getenv("POETRY_OPENAI_API_KEY_IMG")
XI_API_KEYS = getenv("POETRY_XI_API_KEYS").split(",")

# AI models

OPENAI_LLM = "gpt-3.5-turbo-1106"
MISTRAL_LLM_API_KEY = getenv("POETRY_MISTRAL_API_KEY")
IMAGE_MODEL = "dall-e-3"
XI_TTS_MODEL = "eleven_multilingual_v1"
LLM_CHOICE = "openai"  # openai || mistral
MISTRAL_LLM = "TheBloke_OpenHermes-2.5-Mistral-7B-GPTQ_gptq-4bit-32g-actorder_True"
MISTRAL_LLM_ENDPOINT = (
    "https://spoke-vacancies-identifier-ebook.trycloudflare.com/v1/chat/completions"
)

# Current podcast

HOST_NAME = "Daniel"
HOST_VOICE = "Liam"

GUEST_VOICE = "Michael"
GUEST_NAME = "Michael"

SOUND_FORMAT = "mp3"  # only format supported :(

WITH_THUMBNAIL = False
THUMBNAIL_QUANTITY = 1
THUMBNAIL_PIXELS = 750
API_SLEEP = 30  # more than 30 is adviced

## Content
DATE = "morning Thursday 5th February 2024"
SUBJECT = "Quantum Computing Unleashed: Revolutionizing Cybersecurity"
MODE = "Defense"  # "Attack" || "Defense"
CUSTOM_INTRO_DATA = "it’s the podcast number 13"
CUSTOM_OUTRO_DATA = "Say see you next week"
ARTICLE_URL = ""


RSS_FLOWS = ["", ""]
