# local import
from source import fetch_article_content
from pipeline import pipeline

if __name__ == "__main__":
    article_url = "https://www.usine-digitale.fr/article/ransomware-boeing-touche-par-une-attaque-de-lockbit.N2190108"
    article_content = fetch_article_content(article_url=article_url)

    pipeline(
        sound_format="mp3",  # only format supported so far :/
        duration=1,  # in minutes  (estimated)
        topic="ransomware",
        source=article_content,
        reference="source : usine-digitale.fr | ransomware boeing touché par une attaque de lockbit",
        tts="openai",  # ||"xi-labs"
    )
