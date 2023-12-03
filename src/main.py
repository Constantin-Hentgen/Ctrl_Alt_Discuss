from unidecode import unidecode
from os import makedirs, remove
from shutil import rmtree
from pathlib import Path
from time import sleep
from json import dump

# local imports
from configuration import GPT_MODEL, PRE_PROMPT, prompt, OUTPUT_PATH
from thumbnail_generator import generate_thumbnail
from content_generator import generate_content
from soundfile_management import (
    generate_audio_openai,
    generate_audio_xi_labs,
    merge_sound_file,
    montage,
)


if __name__ == "__main__":
    # let the time to initialize the prompt variable and get the article content
    sleep(5)

    podcast_content = generate_content(
        model=GPT_MODEL, preprompt=PRE_PROMPT, prompt=prompt
    )

    folder_name = unidecode(podcast_content["folder_name"].replace(" ", "_"))
    folder_path = f"{OUTPUT_PATH}\\{folder_name}"
    songs_folder = f"{folder_path}\\voices"
    makedirs(f"{folder_path}\\voices")

    generate_thumbnail(
        prompt=f"{podcast_content['thumbnail_prompt']} (avoid writings and characters in the generation)",
        path=folder_path,
    )

    for index, item in enumerate(podcast_content["script"]):
        # generate_audio_openai(
        #     script=item["line"],
        #     voice="onyx" if item["name"] == "Alex" else "nova",
        #     index=index + 1,
        #     folder_path=folder_path,
        #     sound_format="mp3",
        # )
        generate_audio_xi_labs(
            script=item["line"],
            voice="Michael" if item["name"] == "Michael" else "Bella",
            index=index + 1,
            folder_path=folder_path,
            sound_format="mp3",
        )
        sleep(30)

    merge_sound_file(folder_path=folder_path)
    rmtree(songs_folder)
    montage(podcast_folder=folder_path)
    remove(f"{folder_path}\\premade.mp3")

    metadata = {
        "title": podcast_content["title"],
        "description": podcast_content["description"],
    }

    json_file_path = f"{folder_path}\\metadata.json"
    with open(json_file_path, "w") as json_file:
        dump(metadata, json_file, indent=2)

    print("Podcast ready to be uploaded :)")
