# local import
from rss import fetch_article_content
from pipeline import pipeline

if __name__ == "__main__":
    article_url = "https://www.malwarebytes.com/wannacry#:~:text=The%20WannaCry%20attackers%20encrypted%20Windows,150%20countries%20in%20just%20hours."
    article_content = fetch_article_content(article_url=article_url)

    pipeline(
        sound_format="mp3",  # only format supported so far :/
        topic="Wannacry story : What was wannacry ransomware attack ?",
        source=article_content,
        reference="source : malwarebytes.com | What was the WannaCry ransomware attack? ",
        with_thumbnail=False,
    )
