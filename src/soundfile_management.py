from elevenlabs import generate, set_api_key, save, play, User, voices
from pydub import AudioSegment
from random import getrandbits
from openai import OpenAI
from pathlib import Path

# local imports
from secrets import OPENAI_API_KEY_PERSO as OPENAI_API_KEY


def generate_filename(is_openai: bool) -> str:
    win_path = r"C:\Users\Constantin\Desktop\Podcast_Project\output"
    path_universal = Path(win_path)
    if is_openai:
        filename = "openai_%032x.mp3" % getrandbits(128)
    else:
        filename = "xi-labs_%032x.mp3" % getrandbits(128)
    return f"{path_universal}\\{filename}"


def generate_audio_openai(script: str, voice: str) -> None:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.audio.speech.create(model="tts-1-hd", voice=voice, input=script)

    response.stream_to_file(generate_filename(is_openai=True))


def generate_audio_xi_labs(script: str, voice: str):
    set_api_key(XI_API_KEY)
    audio = generate(
        text=script,
        voice=voice,  # "Bella",
        model="eleven_multilingual_v2",
    )

    save(audio, generate_filename(is_openai=False))


def overlay_sound_files():
    sound1 = AudioSegment.from_mp3("/path/to/file1.mp3")
    sound2 = AudioSegment.from_mp3("/path/to/file1.mp3")

    # mix sound2 with sound1, starting at 5000ms into sound1)
    output = sound1.overlay(sound2, position=5000)

    # save the result
    output.export("mixed_sounds.mp3", format="mp3")


def merge_files():
    sound1 = AudioSegment.from_file("/path/to/sound.wav", format="wav")
    sound2 = AudioSegment.from_file("/path/to/another_sound.wav", format="wav")
    combined = sound1 + sound2
    file_handle = combined.export("/path/to/output.mp3", format="mp3")
