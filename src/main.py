from json import load

# local imports
from content import generate_podcast_content
from soundfile import generate_audio_file
from thumbnail import generate_thumbnail
from configuration import (
    CUSTOM_INTRO_DATA,
    CUSTOM_OUTRO_DATA,
    ARTICLE_URL,
    OUTPUT_PATH,
    SUBJECT,
)


if __name__ == "__main__":
    podcast_content = generate_podcast_content()
    thumbnail_prompt = podcast_content["thumbnail_prompt"]
    folder_name = podcast_content["folder_name"]
    rework_finished = bool(input("\n\nDid you finish editing the script ? (bool) : "))

    if rework_finished:
        with open(
            f"{OUTPUT_PATH}\\{folder_name}\\script.json",
            "r",
            encoding="utf-8",
        ) as document:
            script = load(document)
            generate_audio_file(
                script=script,
                folder_name=folder_name,
            )

    print(f"\n\nThumbnail prompt : {thumbnail_prompt}")
    choice = bool(input("\nAre you satisfied with this prompt ? (bool): "))
    thumbnail_prompt = input("Write your prompt: ") if not choice else thumbnail_prompt
    generate_thumbnail(prompt=thumbnail_prompt, folder_name=folder_name)
    print(f"Podcast {folder_name} ready to be uploaded :)")
