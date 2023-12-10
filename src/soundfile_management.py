from elevenlabs import generate, set_api_key, save, play, User, voices
from os import makedirs, remove
from pydub import AudioSegment
from random import getrandbits
from pydub import AudioSegment
from os import listdir, getenv
from shutil import rmtree
from openai import OpenAI
from pathlib import Path
from os.path import join
from time import sleep
from re import match


# local imports
from configuration import (
    OPENAI_TTS_MODEL,
    OPENAI_API_KEY,
    XI_TTS_MODEL,
    OUTPUT_PATH,
    XI_API_KEY,
    ROOT_PATH,
)


def generate_audio_openai(
    sound_format: str,
    folder_path: str,
    script: str,
    index: int,
    voice: str,
) -> None:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.audio.speech.create(
        model=OPENAI_TTS_MODEL, voice=voice, input=script
    )

    filename = f"{index}_{voice}.{sound_format}"
    response.stream_to_file(f"{folder_path}\\voices\\{filename}")


def generate_audio_xi_labs(
    sound_format: str,
    folder_path: str,
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
    save(audio, f"{folder_path}\\voices\\{filename}")


def merge_sound_file(
    folder_path: str, input_sound_format: str, output_sound_format: str
) -> None:
    files = listdir(f"{folder_path}\\voices")
    sound_file = [
        file for file in files if match(rf"\d+_.+\.{input_sound_format}", file)
    ]
    sound_file.sort(key=lambda x: int(match(r"(\d+)_", x).group(1)))
    combined_audio = AudioSegment.silent()

    for audio_file in sound_file:
        file_path = join(f"{folder_path}\\voices", audio_file)
        match input_sound_format:
            case "mp3":
                audio_segment = AudioSegment.from_mp3(file_path)

        combined_audio += audio_segment

    combined_audio.export(
        f"{folder_path}\\premade.{output_sound_format}", format=output_sound_format
    )


def montage(podcast_folder: str):
    intro_path = f"{ROOT_PATH}\\res\\intro.mp3"
    outro_path = f"{ROOT_PATH}\\res\\outro.mp3"

    intro = AudioSegment.from_file(intro_path)
    podcast = AudioSegment.from_file(f"{podcast_folder}\\premade.mp3")
    outro = AudioSegment.from_file(outro_path)

    final_audio = intro + podcast + outro

    final_audio.export(f"{podcast_folder}\\podcast.mp3", format="mp3")


def generate_audio_file(
    script: list,
    folder_name: str,
    tts: str = "openai",
    openai_sleep: int = 30,
    sound_format="mp3",
) -> None:
    folder_path = f"{OUTPUT_PATH}\\{folder_name}"
    songs_folder = f"{folder_path}\\voices"
    makedirs(f"{folder_path}\\voices")

    for index, item in enumerate(podcast_content["script"]):
        match tts:
            case "openai":
                generate_audio_openai(
                    script=item["line"],
                    voice="echo" if item["name"] == "Michael" else "nova",
                    index=index + 1,
                    folder_path=folder_path,
                    sound_format=sound_format,
                )
            case "xi-labs":
                generate_audio_xi_labs(
                    script=item["line"],
                    voice="Michael" if item["name"] == "Michael" else "Matilda",
                    index=index + 1,
                    folder_path=folder_path,
                    sound_format=sound_format,
                )
        sleep(openai_sleep)

    merge_sound_file(
        folder_path=folder_path,
        input_sound_format=sound_format,
        output_sound_format=sound_format,
    )
    rmtree(songs_folder)
    montage(podcast_folder=folder_path)
    remove(f"{folder_path}\\premade.{sound_format}")
