from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
from elevenlabs import generate, set_api_key, save
from os import makedirs, remove, listdir
from pydub import AudioSegment
from random import getrandbits
from shutil import rmtree
from pathlib import Path
from os.path import join
from time import sleep
from re import match
import elevenlabs
import sys


# local imports
from api_management import get_xi_api_key
from configuration import (
    SOUND_FORMAT,
    XI_TTS_MODEL,
    OUTPUT_PATH,
    GUEST_VOICE,
    HOST_VOICE,
    GUEST_NAME,
    ROOT_PATH,
    HOST_NAME,
    API_SLEEP,
)


def rate_limit_prevention(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except elevenlabs.api.error.RateLimitError:
                print("\n\nElevenlabs RateLimit :(\n\n")
                rotate_VPN()
                sleep(5)
                continue
            break

    return wrapper


@rate_limit_prevention
def generate_audio_xi_labs(
    folder_name: str,
    line: str,
    index: int,
    voice: str,
) -> None:
    xi_api_key = get_xi_api_key(line=line)

    if xi_api_key is not None:
        set_api_key(xi_api_key)
        audio = generate(
            model=XI_TTS_MODEL,
            text=line,
            voice=voice,
        )

        filename = f"{index}_{voice}.{SOUND_FORMAT}"
        save(audio, f"{OUTPUT_PATH}\\{folder_name}\\voices\\{filename}")
    else:
        print("You’re broke :(")
        sys.exit(0)


def generate_audio_file(script: list, folder_name: str) -> None:
    initialize_VPN(save=1, area_input=["complete rotation"])
    makedirs(f"{OUTPUT_PATH}\\{folder_name}\\voices")

    increment = 0
    for index, item in enumerate(script):
        if item["name"] == "Transition":
            transition_path = f"{ROOT_PATH}\\res\\transition.{SOUND_FORMAT}"
            transition = AudioSegment.from_file(transition_path)
            transition.export(
                f"{OUTPUT_PATH}\\{folder_name}\\voices\\{index+1}_transition.{SOUND_FORMAT}",
                format=SOUND_FORMAT,
            )
            increment += 1
        else:
            generate_audio_xi_labs(
                line=item["line"],
                voice=GUEST_VOICE if item["name"] == GUEST_NAME else HOST_VOICE,
                index=index + 1 + increment,
                folder_name=folder_name,
            )
        sleep(API_SLEEP)

    merge_sound_file(
        folder_name=folder_name,
    )
    rmtree(f"{OUTPUT_PATH}\\{folder_name}\\voices")
    montage(folder_name=folder_name)
    remove(f"{OUTPUT_PATH}\\{folder_name}\\premade.{SOUND_FORMAT}")


def merge_sound_file(folder_name: str) -> None:
    files = listdir(f"{OUTPUT_PATH}\\{folder_name}\\voices")
    sound_file = [file for file in files if match(rf"\d+_.+\.{SOUND_FORMAT}", file)]
    sound_file.sort(key=lambda x: int(match(r"(\d+)_", x).group(1)))
    combined_audio = AudioSegment.silent()

    for audio_file in sound_file:
        file_path = join(f"{OUTPUT_PATH}\\{folder_name}\\voices", audio_file)
        match SOUND_FORMAT:
            case "mp3":
                audio_segment = AudioSegment.from_mp3(file_path)

        combined_audio += audio_segment

    combined_audio.export(
        f"{OUTPUT_PATH}\\{folder_name}\\premade.{SOUND_FORMAT}",
        format=SOUND_FORMAT,
    )


def montage(folder_name: str) -> None:
    outro_path = f"{ROOT_PATH}\\res\\outro.{SOUND_FORMAT}"
    intro_path = f"{ROOT_PATH}\\res\\intro.{SOUND_FORMAT}"

    intro = AudioSegment.from_file(intro_path)
    podcast = AudioSegment.from_file(
        f"{OUTPUT_PATH}\\{folder_name}\\premade.{SOUND_FORMAT}"
    )
    outro = AudioSegment.from_file(outro_path)

    final_audio = intro + podcast + outro

    final_audio.export(
        f"{OUTPUT_PATH}\\{folder_name}\\podcast.{SOUND_FORMAT}", format=SOUND_FORMAT
    )
