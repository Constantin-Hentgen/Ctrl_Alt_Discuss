# local imports
from soundfile_management import generate_audio_file
from thumbnail_generator import generate_thumbnail
from content import generate_podcast_content


def pipeline(
    sound_format: str = "mp3",
    duration: int = 5,
    specialization: str = "IT",
    tts: str = "openai",
) -> None:
    podcast_content = generate_podcast_content()

    generate_thumbnail(
        prompt=podcast_content["thumbnail_prompt"],
        folder_name=podcast_content["folder_name"],
    )

    generate_audio_file(script=podcast_content["script"], sound_format=sound_format)

    print("Podcast ready to be uploaded :)")
