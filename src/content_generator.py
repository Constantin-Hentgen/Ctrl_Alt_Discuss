from datetime import datetime
from openai import OpenAI
from json import loads
from os import getenv


# local imports
from configuration import (
    PREPROMPT_METADATA,
    PROMPT_CONCLUSION,
    PROMPT_INTRODUCTION,
    PROMPT_DEVELOPMENT,
    PROMPT_PLAN,
    PREPROMPT,
    GPT_MODEL,
)


# generalist openai request
def generate_content(
    prompt: str, preprompt: str = PREPROMPT, model: str = GPT_MODEL
) -> str:
    OPENAI_API_KEY = getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": preprompt,
            },
            {"role": "user", "content": prompt},
        ],
    )

    return loads(response.choices[0].message.content)


def generate_plan() -> list:
    print("Plan generation...")
    return generate_content(prompt=PROMPT_PLAN)["plan"]


def generate_metadata(plan: dict) -> dict:
    print("Metadata generation...")
    PROMPT_METADATA = str(plan)
    metadata = generate_content(preprompt=PREPROMPT_METADATA, prompt=PROMPT_METADATA)

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

    output = {
        "datetime": formatted_time,
        "title": metadata["title"],
        "description": metadata["description"],
        "plan": plan,
        "thumbnail_prompt": metadata["thumbnail_prompt"],
        "folder_name": metadata["folder_name"],
        "metadata_preprompt": PREPROMPT_METADATA,
        "metadata_prompt": PROMPT_METADATA,
        "main_preprompt": PREPROMPT,
        "plan_prompt": PROMPT_PLAN,
        "introduction_prompt": PROMPT_INTRODUCTION,
        "development_prompt": PROMPT_DEVELOPMENT,
        "conclusion_prompt": PROMPT_CONCLUSION,
    }

    json_file_path = f"{OUTPUT_PATH}\\{metadata['folder_name']}\\metadata.json"

    with open(json_file_path, "w") as json_file:
        dump(metadata, json_file, indent=2)


def generate_development(plan: list) -> dict:
    print("\tDevelopment generation")
    development = []

    for part in plan:
        temp_prompt = (
            f"{PROMPT_DEVELOPMENT}"
            f"\nthe name of the part you have to write is :"
            f"{part['title']}"
            f", and follow this instruction to write a good dialogue : "
            f"{part['description']}"
        )
        development.append(generate_content(prompt=temp_prompt))

    return development


def generate_introduction() -> dict:
    print("\tIntroduction generation...")
    return generate_content(prompt=PROMPT_INTRODUCTION)


def generate_conclusion() -> dict:
    print("\tIntroduction generation...")
    return generate_content(prompt=PROMPT_CONCLUSION)


def generate_script(plan: list, folder_name: str) -> list:
    print("Script generation...")
    introduction = generate_introduction()
    development = generate_development(plan)
    conclusion = generate_conclusion()
    output = (
        introduction["script"]
        + [line for chapter in development for line in chapter["script"]]
        + conclusion["script"]
    )

    json_file_path = f"{OUTPUT_PATH}\\{folder_name}\\script.json"

    with open(json_file_path, "w") as json_file:
        dump(output, json_file, indent=2)

    return output


def generate_podcast_content() -> dict:
    plan = generate_plan()
    metadata = generate_metadata(plan=plan)
    script = generate_script(folder_name=metadata["folder_name"])

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "thumbnail_prompt": f"{metadata['thumbnail_prompt']}\n NO WRITING or INSCRIPTIONS",
        "folder_name": metadata["folder_name"],
        "script": script,
    }
