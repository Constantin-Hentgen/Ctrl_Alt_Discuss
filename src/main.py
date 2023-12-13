# local import
from rss import fetch_article_content
from pipeline import pipeline

if __name__ == "__main__":
    article_url = "https://www.welivesecurity.com/en/eset-research/pernicious-potpourri-python-packages-pypi/?&web_view=true"
    article_content = fetch_article_content(article_url=article_url)

    pipeline(
        sound_format="mp3",  # only format supported so far :/
        topic="malicious python packages",
        source=article_content,
        reference="source : welivesecurity.com | A pernicious potpourri of Python packages in PyPI",
    )
