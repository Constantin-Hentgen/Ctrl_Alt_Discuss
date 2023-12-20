from dotenv import load_dotenv
from os import getenv

# Load environment variables from .env file, if it exists
load_dotenv()

ROOT_PATH = getenv("POETRY_CAD_ROOT_PATH")
OUTPUT_PATH = rf"{ROOT_PATH}\output"

OPENAI_LLM = "gpt-3.5-turbo-1106"
MISTRAL_LLM = "TheBloke_OpenHermes-2.5-Mistral-7B-GPTQ_gptq-4bit-32g-actorder_True"
MISTRAL_LLM_ENDPOINT = (
    "https://spoke-vacancies-identifier-ebook.trycloudflare.com/v1/chat/completions"
)
MISTRAL_LLM_API_KEY = getenv("POETRY_MISTRAL_API_KEY")
IMAGE_MODEL = "dall-e-3"
OPENAI_API_KEY = getenv("POETRY_OPENAI_API_KEY")
XI_API_KEYS = getenv("POETRY_XI_API_KEYS").split(",")

XI_TTS_MODEL = "eleven_multilingual_v1"
GITHUB_REPO = "Ctrl_Alt_Discuss"
GITHUB_REPO_OWNER = "Constantin-Hentgen"

LLM_CHOICE = "openai"  # || mistral
SOUND_FORMAT = "mp3"  # only format supported :(
HOST_NAME = "Daniel"
GUEST_NAME = "Michael"
