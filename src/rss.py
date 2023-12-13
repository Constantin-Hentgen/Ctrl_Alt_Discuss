from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from feedparser import parse
from random import choice
import requests


def get_latest_article_url(rss_source_url: str) -> str:
    feed = parse(rss_source_url)

    one_week_ago = datetime.utcnow() - timedelta(days=7)
    filtered_entries = [
        entry
        for entry in feed.entries
        if entry.published_parsed >= one_week_ago.timetuple()
    ]

    if filtered_entries:
        random_entry = choice(filtered_entries)
        latest_article_url = random_entry.link

        print(
            f"The URL of a random article from the last week is: {latest_article_url}"
        )
        return latest_article_url
    else:
        print("No articles found in the selected RSS feed published in the last week.")
        return None


def fetch_article_content(article_url: str) -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        response = requests.get(article_url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        soup = BeautifulSoup(response.text, "html.parser")
        article_content = ""
        for paragraph in soup.find_all("p"):
            article_content += paragraph.get_text() + "\n"

        return article_content.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching article content: {e}")
        return None
