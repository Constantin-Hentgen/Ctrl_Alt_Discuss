# local import
from pipeline import pipeline

if __name__ == "__main__":
    pipeline(
        sound_format="mp3",  # only format supported so far :/
        topic="Stuxnet is a computer worm that was used to attack Iranian nuclear facilities",
        article_url="https://www.malwarebytes.com/stuxnet",
        reference="source : malwarebytes.com | Stuxnet is a computer worm that was used to attack Iranian nuclear facilities",
        with_thumbnail=False,
        with_audio=True,
    )
