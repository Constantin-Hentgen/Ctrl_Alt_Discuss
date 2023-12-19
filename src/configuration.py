from dotenv import load_dotenv
from os import getenv

# Load environment variables from .env file, if it exists
load_dotenv()

ROOT_PATH = getenv("POETRY_CAD_ROOT_PATH")
OUTPUT_PATH = rf"{ROOT_PATH}\output"

GPT_MODEL = "gpt-3.5-turbo-1106"
IMAGE_MODEL = "dall-e-3"
OPENAI_API_KEY = getenv("POETRY_OPENAI_API_KEY")
XI_API_KEYS = getenv("POETRY_XI_API_KEYS").split(",")

XI_TTS_MODEL = "eleven_multilingual_v2"
GITHUB_REPO = "Ctrl_Alt_Discuss"
GITHUB_REPO_OWNER = "Constantin-Hentgen"
