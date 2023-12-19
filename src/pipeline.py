# local imports
from content import generate_podcast_content
from soundfile import generate_audio_file
from thumbnail import generate_thumbnail

from api_management import is_xi_possible
from rss import fetch_article_content


def pipeline(
    topic: str,
    article_url: str,
    reference: str,
    sound_format: str = "mp3",
    with_thumbnail: bool = False,
    with_audio: bool = False,
) -> None:
    article_content = fetch_article_content(article_url=article_url)
    podcast_content = generate_podcast_content(
        reference=reference,
        source=article_content,
        topic=topic,
        article_url=article_url,
    )

    if with_thumbnail:
        generate_thumbnail(
            prompt=podcast_content["thumbnail_prompt"],
            folder_name=podcast_content["folder_name"],
        )

    if with_audio:
        if is_xi_possible(script=podcast_content["script"]):
            generate_audio_file(
                script=podcast_content["script"],
                sound_format=sound_format,
                folder_name=podcast_content["folder_name"],
            )
        else:
            print("Not enough xi-labs credits to generate this podcast :(")

    print(f"Podcast {podcast_content['folder_name']} ready to be uploaded :)")
