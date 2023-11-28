from time import sleep

# local imports
from soundfile_management import generate_audio_openai
from configuration import GPT_MODEL, PRE_PROMPT
from script_generator import generate_script

if __name__ == "__main__":
    prompt = """
        various SQL injections techniques - cybersecurity and web hacking\n
        Google just been hacked this morning 1may 2023 by an SQL attack on its youtube server
    """

    script = generate_script(model=GPT_MODEL, preprompt=PRE_PROMPT, prompt=prompt)

    # sleep(30)
    # generate_audio_openai(script=script, voice="onyx")
    # generate_audio_xi_labs(script=script, voice="Liam")

    # generate the thumbnail // DONE
    # generate a description // DONE
    # generate a title // DONE
    # create a folder
    # within the folder generate files like "1_Patrick.mp3", "2_Stephanie"
    # merge all the files
