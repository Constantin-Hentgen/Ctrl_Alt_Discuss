# local import
from pipeline import pipeline

if __name__ == "__main__":
    pipeline(
        custom_intro_data="It’s the Second podcast, and it’s christmas soon. (mention it in the small talk / welcoming)",
        topic="The evolution of security: the story of Code Red",
        article_url="https://www.kaspersky.com/blog/history-lessons-code-red/45082/",
        reference="source : kaspersky.com | The evolution of security: the story of Code Red",
        with_thumbnail=False,
        with_audio=True,
    )
