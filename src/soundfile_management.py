from elevenlabs import generate, set_api_key, save, play, User, voices
from pydub import AudioSegment
from random import getrandbits
from pydub import AudioSegment
from openai import OpenAI
from pathlib import Path
from os.path import join
from os import listdir
from re import match

# local imports
from secrets import OPENAI_API_KEY_PERSO as OPENAI_API_KEY
from secrets import XI_API_KEY

from configuration import ROOT_PATH


def generate_audio_openai(
    script: str,
    index: int,
    folder_path: str,
    voice: str,
    sound_format: str = "mp3",
) -> None:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.audio.speech.create(model="tts-1-hd", voice=voice, input=script)
    filename = f"{index}_{voice}.{sound_format}"
    response.stream_to_file(f"{folder_path}\\voices\\{filename}")


# to update to openai standards
def generate_audio_xi_labs(
    script: str,
    index: int,
    folder_path: str,
    voice: str = "Liam",
    sound_format: str = "mp3",
) -> None:
    set_api_key(XI_API_KEY)
    audio = generate(
        text=script,
        voice=voice,  # "Bella",
        model="eleven_multilingual_v2",
    )
    filename = f"{index}_{voice}.{sound_format}"
    save(audio, f"{folder_path}\\voices\\{filename}")


def merge_sound_file(
    folder_path: str, input_sound_format: str = "mp3", output_sound_format: str = "mp3"
) -> None:
    files = listdir(f"{folder_path}\\voices")
    sound_file = [file for file in files if match(r"\d+_.+\.mp3", file)]
    sound_file.sort(key=lambda x: int(match(r"(\d+)_", x).group(1)))
    combined_audio = AudioSegment.silent()

    for mp3_file in sound_file:
        file_path = join(f"{folder_path}\\voices", mp3_file)
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
