from os import getenv

# local imports
from source import fetch_article_content

ROOT_PATH = getenv("POETRY_BYTEBEACON_ROOT_PATH")
OUTPUT_PATH = rf"{ROOT_PATH}\output"

GPT_MODEL = "gpt-3.5-turbo-1106"
IMAGE_MODEL = "dall-e-3"
OPENAI_API_KEY = getenv("POETRY_OPENAI_API_KEY")
XI_API_KEY = getenv("POETRY_XI_API_KEY")

OPENAI_TTS_MODEL = "tts-1-hd"
XI_TTS_MODEL = "eleven_multilingual_v2"

RSS_LIST = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]
article_url = "https://www.nationalgeographic.com/history/history-magazine/article/roman-emperor-believed-god-assassinated"
article_content = fetch_article_content(article_url=article_url)

# rss_source_url = get_random_rss_source(list_rss_feed_urls=RSS_LIST)
# article = build_prompt(rss_source_url=rss_source_url)
