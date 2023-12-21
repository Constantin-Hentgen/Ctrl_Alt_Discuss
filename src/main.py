# local import
from pipeline import pipeline

if __name__ == "__main__":
    pipeline(
        topic="The Melissa virus is a mass-mailing macro virus released on or around March 26, 1999. ",
        article_url="https://www.orangecyberdefense.com/fr/insights/blog/ethical-hacking/hacks-de-legende-2-1999-melissa",
        reference="source : orangecyberdefense.com | The Melissa virus is a mass-mailing macro virus released on or around March 26, 1999. ",
        with_thumbnail=False,
        with_audio=True,
    )
