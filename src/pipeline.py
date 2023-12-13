# local imports
from content import generate_podcast_content
from soundfile import generate_audio_file
from thumbnail import generate_thumbnail


def pipeline(
    source: str,
    topic: str,
    reference: str,
    sound_format: str = "mp3",
    duration: int = 1,
    tts: str = "openai",
) -> None:
    podcast_content = generate_podcast_content(
        reference=reference, duration=duration, source=source, topic=topic
    )

    generate_thumbnail(
        prompt=podcast_content["thumbnail_prompt"],
        folder_name=podcast_content["folder_name"],
    )

    generate_audio_file(script=podcast_content["script"], sound_format=sound_format)

    print("Podcast ready to be uploaded :)")
