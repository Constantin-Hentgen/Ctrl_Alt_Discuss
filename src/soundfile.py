from elevenlabs import generate, set_api_key, save
from os import makedirs, remove, listdir
from pydub import AudioSegment
from random import getrandbits
from shutil import rmtree
from pathlib import Path
from os.path import join
from time import sleep
from re import match

# local imports
from configuration import (
    XI_TTS_MODEL,
    OUTPUT_PATH,
    XI_API_KEY,
    ROOT_PATH,
)


def generate_audio_xi_labs(
    sound_format: str,
    folder_name: str,
    script: str,
    index: int,
    voice: str,
) -> None:
    set_api_key(XI_API_KEY)
    audio = generate(
        model=XI_TTS_MODEL,
        text=script,
        voice=voice,
    )

    filename = f"{index}_{voice}.{sound_format}"
    save(audio, f"{OUTPUT_PATH}\\{folder_name}\\voices\\{filename}")


def generate_audio_file(
    script: list,
    folder_name: str,
    api_sleep: int = 30,
    sound_format="mp3",
) -> None:
    makedirs(f"{OUTPUT_PATH}\\{folder_name}\\voices")

    increment = 0
    for index, item in enumerate(script):
        if item["name"] == "Silence":
            silence_path = f"{ROOT_PATH}\\res\\second_of_silence.mp3"
            silence = AudioSegment.from_file(silence_path)
            final_audio.export(
                f"{OUTPUT_PATH}\\{folder_name}\\{index+1}_silence.{sound_format}",
                format=sound_format,
            )
            increment += 1

            generate_audio_xi_labs(
                script=item["line"],
                voice="Michael" if item["name"] == "Michael" else "Freya",
                index=index + 1 + increment,
                folder_name=folder_name,
                sound_format=sound_format,
            )
        sleep(api_sleep)

    merge_sound_file(
        folder_name=folder_name,
        input_sound_format=sound_format,
        output_sound_format=sound_format,
    )
    rmtree(f"{OUTPUT_PATH}\\{folder_name}\\voices")
    montage(folder_name=folder_name)
    remove(f"{OUTPUT_PATH}\\{folder_name}\\premade.{sound_format}")


def merge_sound_file(
    folder_name: str, input_sound_format: str, output_sound_format: str
) -> None:
    files = listdir(f"{OUTPUT_PATH}\\{folder_name}\\voices")
    sound_file = [
        file for file in files if match(rf"\d+_.+\.{input_sound_format}", file)
    ]
    sound_file.sort(key=lambda x: int(match(r"(\d+)_", x).group(1)))
    combined_audio = AudioSegment.silent()

    for audio_file in sound_file:
        file_path = join(f"{OUTPUT_PATH}\\{folder_name}\\voices", audio_file)
        match input_sound_format:
            case "mp3":
                audio_segment = AudioSegment.from_mp3(file_path)

        combined_audio += audio_segment

    combined_audio.export(
        f"{OUTPUT_PATH}\\{folder_name}\\premade.{output_sound_format}",
        format=output_sound_format,
    )


def montage(folder_name: str, sound_format: str = "mp3") -> None:
    intro_path = f"{ROOT_PATH}\\res\\intro.mp3"
    outro_path = f"{ROOT_PATH}\\res\\outro.mp3"

    intro = AudioSegment.from_file(intro_path)
    podcast = AudioSegment.from_file(f"{OUTPUT_PATH}\\{folder_name}\\premade.mp3")
    outro = AudioSegment.from_file(outro_path)

    final_audio = intro + podcast + outro

    final_audio.export(
        f"{OUTPUT_PATH}\\{folder_name}\\podcast.{sound_format}", format=sound_format
    )
