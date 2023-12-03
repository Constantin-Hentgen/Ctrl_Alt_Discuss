from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from feedparser import parse
from random import choice
import requests


def get_random_rss_source(list_rss_feed_urls: list) -> str:
    return choice(list_rss_feed_urls)


def get_latest_article_url(rss_source_url: str) -> str:
    # Parse the RSS feed
    feed = parse(rss_source_url)

    # Filter entries published within the last week
    one_week_ago = datetime.utcnow() - timedelta(days=7)
    filtered_entries = [
        entry
        for entry in feed.entries
        if entry.published_parsed >= one_week_ago.timetuple()
    ]

    if filtered_entries:
        # Shuffle the filtered entries and pick one randomly
        random_entry = choice(filtered_entries)

        # Get the URL of the randomly picked article
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
        # Add headers to mimic a real user's request
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

        # Make an HTTP request to the article URL with headers
        response = requests.get(article_url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # Parse the HTML content of the article
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the text content of the article
        article_content = ""
        for paragraph in soup.find_all("p"):
            article_content += paragraph.get_text() + "\n"

        return article_content.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching article content: {e}")
        return None


def build_prompt(rss_source_url: str) -> str:
    article_url = get_latest_article_url(rss_source_url=rss_source_url)
    content = fetch_article_content(article_url=article_url)
    return content
