from datetime import datetime
from openai import OpenAI
from json import loads
from os import getenv
from json import dump

# local imports
from configuration import OPENAI_API_KEY, GPT_MODEL

from prompts.metadata import (
    PREPROMPT as metadata_preprompt,
)

from prompts.plan import PREPROMPT as plan_preprompt, PROMPT as plan_prompt

from prompts.introduction import (
    PREPROMPT as introduction_preprompt,
    PROMPT as introduction_prompt,
)

from prompts.development import (
    PREPROMPT as development_preprompt,
    PROMPT as development_prompt,
)

from prompts.conclusion import (
    PREPROMPT as conclusion_preprompt,
    PROMPT as conclusion_prompt,
)


def generate_content(preprompt: str, prompt: str) -> str:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=GPT_MODEL,
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
    result = generate_content(preprompt=plan_preprompt, prompt=plan_prompt)
    return result["plan"]


def generate_metadata(plan: dict) -> dict:
    print("Metadata generation...")
    metadata_prompt = str(plan)
    metadata = generate_content(preprompt=metadata_preprompt, prompt=metadata_prompt)

    now = datetime.now()
    formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

    output = {
        "datetime": formatted_time,
        "title": metadata["title"],
        "description": metadata["description"],
        "plan": plan,
        "thumbnail_prompt": metadata["thumbnail_prompt"],
        "folder_name": metadata["folder_name"],
        "metadata_preprompt": metadata_preprompt,
        "metadata_prompt": plan,
        "plan_preprompt": plan_preprompt,
        "plan_prompt": plan_prompt,
        "introduction_preprompt": introduction_preprompt,
        "introduction_prompt": introduction_prompt,
        "development_preprompt": development_preprompt,
        "development_prompt": development_prompt,
        "conclusion_preprompt": conclusion_preprompt,
        "conclusion_prompt": conclusion_prompt,
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
    return generate_content(
        preprompt=introduction_preprompt, prompt=introduction_prompt
    )


def generate_conclusion() -> dict:
    print("\tIntroduction generation...")
    return generate_content(preprompt=conclusion_preprompt, prompt=conclusion_prompt)


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
