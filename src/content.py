from json import loads, dumps, dump
from datetime import datetime
from openai import OpenAI
from os import getenv
import sys


# local imports
from configuration import OPENAI_API_KEY, GPT_MODEL, OUTPUT_PATH

from prompts.introduction import SYSTEM_PROMPT as introduction_system_prompt
from prompts.development import SYSTEM_PROMPT as development_system_prompt
from prompts.conclusion import SYSTEM_PROMPT as conclusion_system_prompt
from prompts.plan import SYSTEM_PROMPT as plan_system_prompt
from prompts.metadata import (
    SYSTEM_PROMPT as metadata_system_prompt,
)


def content_validator(func):
    def wrapper(*args, **kwargs):
        while True:
            display_name = func.__name__.replace("generate_", "").replace("_", " ")
            print(f"Generating {display_name}...")
            result = dumps(func(*args, **kwargs), indent=2)
            print(f"\n{result}\n")
            response = input(
                "Are you satisfied with the result? (yes/retry/stop): "
            ).lower()
            if response == "yes":
                break
            elif response == "stop":
                print("Stopping the program.")
                sys.exit(0)
            elif response != "retry":
                print("Invalid response. Please enter 'yes', 'retry', or 'stop'.")

        print()

    return wrapper


def generate_content(system_prompt: str, prompt: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=GPT_MODEL,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": prompt},
        ],
    )

    return loads(response.choices[0].message.content)


@content_validator
def generate_plan(duration: int, source: str, topic: str) -> list:
    number_of_parts = duration * 3
    prompt = (
        f"The plan should contains {number_of_parts} and has to popularize and explain the following topic : {topic}"
        f"The target audience is ignorant in this subject so make the parts so focus on the popularization aspect."
    )

    if source is not None:
        prompt += f"\n build the plan with this source : \n {source}"

    result = generate_content(system_prompt=plan_system_prompt, prompt=prompt)
    return result["plan"]


@content_validator
def generate_introduction(plan: str, topic: str, reference: str) -> dict:
    prompt = f"{plan}\n main topic : {topic}\n reference: {reference}"
    return generate_content(system_prompt=introduction_system_prompt, prompt=prompt)


@content_validator
def generate_development(plan: list, introduction: list) -> dict:
    development = []

    for part in plan:
        prompt = (
            f"\nthe name of the part you have to write is :"
            f"{part['title']}"
            f", with the following description : "
            f"{part['description']}"
            f"here is the introduction of the podcast : {introduction}"
        )
        development.append(
            generate_content(system_prompt=development_system_prompt, prompt=prompt)[
                "script"
            ]
        )

    development = [item for part in development for item in part]
    return development


@content_validator
def generate_conclusion(introduction: str, development: list) -> dict:
    prompt = f"introduction : {introduction}, development : {development}"
    return generate_content(system_prompt=conclusion_system_prompt, prompt=prompt)


@content_validator
def generate_metadata(plan: dict) -> dict:
    metadata_prompt = str(plan)
    metadata = generate_content(
        system_prompt=metadata_system_prompt, prompt=metadata_prompt
    )

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

    output = {
        "datetime": formatted_time,
        "title": metadata["title"],
        "description": metadata["description"],
        "plan": plan,
        "thumbnail_prompt": metadata["thumbnail_prompt"],
        "folder_name": metadata["folder_name"],
    }
    return output

    json_file_path = f"{OUTPUT_PATH}\\{metadata['folder_name']}\\metadata.json"

    with open(json_file_path, "w") as json_file:
        dump(metadata, json_file, indent=2)


def generate_script(plan: list, reference: str, topic: str) -> list:
    introduction = generate_introduction(plan=plan, reference=reference, topic=topic)
    development = generate_development(plan=plan, introduction=introduction)
    conclusion = generate_conclusion(introduction=introduction, development=development)

    output = introduction["script"] + development["script"] + conclusion["script"]
    return output


def generate_podcast_content(
    reference: str,
    duration: int,
    source: str,
    topic: str,
) -> dict:
    plan = generate_plan(duration=duration, source=source, topic=topic)
    metadata = generate_metadata(plan=plan)
    script = generate_script(
        folder_name=metadata["folder_name"],
        reference=reference,
        topic=topic,
    )

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "thumbnail_prompt": f"{metadata['thumbnail_prompt']}\n NO WRITING or INSCRIPTIONS",
        "folder_name": metadata["folder_name"],
        "script": script,
    }
