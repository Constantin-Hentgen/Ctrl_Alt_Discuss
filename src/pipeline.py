# local imports
from content import generate_podcast_content
from soundfile import generate_audio_file
from thumbnail import generate_thumbnail
from api_management import is_xi_possible


def pipeline(
    source: str,
    topic: str,
    reference: str,
    sound_format: str = "mp3",
) -> None:
    podcast_content = generate_podcast_content(
        reference=reference, source=source, topic=topic
    )

    generate_thumbnail(
        prompt=podcast_content["thumbnail_prompt"],
        folder_name=podcast_content["folder_name"],
    )

    tts = "openai"
    if is_xi_possible(script=podcast_content["script"]):
        choice = input("\nXI-labs possible, openai/xi-labs: ")
        if choice == "xi-labs":
            tts = "xi-labs"

    generate_audio_file(
        script=podcast_content["script"],
        sound_format=sound_format,
        folder_name=podcast_content["folder_name"],
        tts=tts,
    )

    print(f"Podcast {podcast_content['folder_name']} ready to be uploaded :)")
