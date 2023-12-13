# local import
from source import fetch_article_content
from pipeline import pipeline

if __name__ == "__main__":
    article_url = "https://www.nationalgeographic.com/history/history-magazine/article/roman-emperor-believed-god-assassinated"
    article_content = fetch_article_content(article_url=article_url)

    pipeline(
        sound_format="mp3",  # only format supported so far :/
        duration=8,  # in minutes  (estimated)
        depth_level="Expert",  # || Ignorant || Beginner || Hobbyist || Advanced || Expert
        specialization="IT",  # || History || Mechanics || ...
        source=article_content,
        tts="openai",  # ||"xi-labs"
    )
