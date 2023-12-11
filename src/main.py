# local import
from pipeline import pipeline


if __name__ == "__main__":
    pipeline(sound_format="mp3", duration=8, specialization="IT", tts="openai")
