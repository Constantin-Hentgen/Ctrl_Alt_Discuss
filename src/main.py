# local import
from rss import fetch_article_content
from pipeline import pipeline

if __name__ == "__main__":
    article_url = "https://www.avast.com/c-eternalblue?redirect=1"
    article_content = fetch_article_content(article_url=article_url)

    pipeline(
        sound_format="mp3",  # only format supported so far :/
        topic="EternalBlue, the cyberattack nightmare",
        source=article_content,
        reference="source : avast.com | What Is EternalBlue and Why Is the MS17-010 Exploit Still Relevant? ",
        with_thumbnail=False,
        article_url=article_url,
    )
