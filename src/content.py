from json import loads, dumps, dump
from datetime import datetime
import requests
from openai import OpenAI
from os import makedirs
import sys


# local imports
from configuration import (
    OPENAI_API_KEY,
    GPT_MODEL,
    OUTPUT_PATH,
    PLAN_SIZE,
    GITHUB_REPO,
    GITHUB_REPO_OWNER,
)

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
            print(f"\nGenerating {display_name}...")
            result = func(*args, **kwargs)
            preview = dumps(result, indent=2)
            print(f"\n{preview}\n")
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
        return result

    return wrapper


def get_latest_release_tag():
    url = f"https://api.github.com/repos/{GITHUB_REPO_OWNER}/{GITHUB_REPO}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        release_data = response.json()
        tag_name = release_data.get("tag_name")
        return tag_name
    else:
        print(f"Failed to retrieve latest release. Status code: {response.status_code}")
        return None


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
def generate_plan(source: str, topic: str) -> list:
    number_of_parts = PLAN_SIZE
    prompt = (
        f"The plan should contains {number_of_parts} and has to popularize and explain the following topic : {topic}"
        f"The target audience is ignorant in this subject so make the parts so focus on the popularization aspect."
    )

    if source is not None:
        prompt += f"\n build the plan with this source : \n {source}"

    result = generate_content(system_prompt=plan_system_prompt, prompt=prompt)
    return result["plan"]


@content_validator
def generate_introduction(plan: str, topic: str, reference: str) -> list:
    prompt = f"{plan}\n main topic : {topic}\n reference: {reference}"
    return generate_content(system_prompt=introduction_system_prompt, prompt=prompt)[
        "script"
    ]


@content_validator
def generate_development(plan: list, introduction: list, source: str) -> list:
    development = []

    for part in plan:
        prompt = str(
            (
                f"\nthe name of the part you have to write is :"
                f"{part['title']}"
                f", with the following description : "
                f"{part['description']}"
                f"here is the introduction of the podcast : {introduction}",
                f"\n Here is the source article content:",
                f"{source}",
            )
        )
        development.append(
            generate_content(system_prompt=development_system_prompt, prompt=prompt)[
                "script"
            ]
        )

    development = [item for part in development for item in part]
    return development


@content_validator
def generate_conclusion(introduction: str, development: list) -> list:
    prompt = f"introduction : {introduction}, development : {development}"
    return generate_content(system_prompt=conclusion_system_prompt, prompt=prompt)[
        "script"
    ]


@content_validator
def generate_metadata(plan: dict, topic: str, article_url: str) -> dict:
    metadata_prompt = f"plan: {plan}\n topic: {topic}"
    metadata = generate_content(
        system_prompt=metadata_system_prompt, prompt=metadata_prompt
    )

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")
    version = get_latest_release_tag()

    output = {
        "datetime": formatted_time,
        "version": version,
        "title": metadata["title"],
        "description": metadata["description"],
        "article_url": article_url,
        "plan": plan,
        "thumbnail_prompt": metadata["thumbnail_prompt"],
        "folder_name": metadata["folder_name"],
    }

    return output


def generate_podcast_content(
    reference: str, source: str, topic: str, article_url: str
) -> dict:
    plan = generate_plan(source=source, topic=topic)
    introduction = generate_introduction(plan=plan, reference=reference, topic=topic)
    development = generate_development(
        introduction=introduction, plan=plan, source=source
    )
    conclusion = generate_conclusion(introduction=introduction, development=development)
    metadata = generate_metadata(plan=plan, topic=topic, article_url=article_url)

    script = introduction + development + conclusion

    podcast_path = f"{OUTPUT_PATH}\\{metadata['folder_name']}"
    makedirs(podcast_path)
    metadata_path = f"{podcast_path}\\metadata.json"

    with open(metadata_path, "w") as json_file:
        dump(metadata, json_file, indent=2)

    script_path = f"{podcast_path}\\script.json"

    with open(script_path, "w") as json_file:
        dump(script, json_file, indent=2)

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "thumbnail_prompt": f"{metadata['thumbnail_prompt']}\n NO WRITING or INSCRIPTIONS",
        "folder_name": metadata["folder_name"],
        "script": script,
    }
