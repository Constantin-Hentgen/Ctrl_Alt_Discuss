from datetime import datetime
from openai import OpenAI
from json import loads
from os import getenv
from json import dump

# local imports
from configuration import OPENAI_API_KEY, GPT_MODEL

from prompts.metadata import (
    SYSTEM_PROMPT as metadata_system_prompt,
)

from prompts.plan import SYSTEM_PROMPT as plan_system_prompt
from prompts.introduction import SYSTEM_PROMPT as introduction_system_prompt

from prompts.development import (
    SYSTEM_PROMPT as development_system_prompt,
    PROMPT as development_prompt,
)

from prompts.conclusion import (
    SYSTEM_PROMPT as conclusion_system_prompt,
    PROMPT as conclusion_prompt,
)


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


def generate_plan(duration: int, depth_level: str, source: str, topic: str) -> list:
    print("Plan generation...")
    number_of_parts = duration * 3
    prompt = (
        f"The plan should contains {number_of_parts} and has to popularize and explain the following topic : {topic}"
        f"The target audience is {depth_level} in this subject so make the parts fit their expectations."
    )

    if source is not None:
        prompt += f"\n build the plan with this source : \n {source}"

    result = generate_content(system_prompt=plan_system_prompt, prompt=prompt)
    return result["plan"]


def generate_introduction(plan: str, specialization: str, topic: str) -> dict:
    print("\tIntroduction generation...")
    prompt = f"{plan}\n field of expertise : {specialization}\n main topic : {topic}"
    return generate_content(system_prompt=introduction_system_prompt, prompt=prompt)


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


def generate_conclusion(development: str) -> dict:
    print("\tIntroduction generation...")
    return generate_content(
        system_prompt=conclusion_system_prompt, prompt=conclusion_prompt
    )


def generate_metadata(plan: dict) -> dict:
    print("Metadata generation...")
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
        "metadata_system_prompt": metadata_system_prompt,
        "metadata_prompt": plan,
        "plan_system_prompt": plan_system_prompt,
        "plan_prompt": plan_prompt,
        "introduction_system_prompt": introduction_system_prompt,
        "introduction_prompt": introduction_prompt,
        "development_system_prompt": development_system_prompt,
        "development_prompt": development_prompt,
        "conclusion_system_prompt": conclusion_system_prompt,
        "conclusion_prompt": conclusion_prompt,
    }

    json_file_path = f"{OUTPUT_PATH}\\{metadata['folder_name']}\\metadata.json"

    with open(json_file_path, "w") as json_file:
        dump(metadata, json_file, indent=2)


def generate_script(plan: list, folder_name: str) -> list:
    print("Script generation...")
    introduction = generate_introduction(plan=plan)
    development = generate_development(plan=plan)
    conclusion = generate_conclusion(development=development)
    output = (
        introduction["script"]
        + [line for chapter in development for line in chapter["script"]]
        + conclusion["script"]
    )

    json_file_path = f"{OUTPUT_PATH}\\{folder_name}\\script.json"

    with open(json_file_path, "w") as json_file:
        dump(output, json_file, indent=2)

    return output


def generate_podcast_content(duration: int, depth_level: str, source: str) -> dict:
    plan = generate_plan(duration=duration, depth_level=depth_level, source=source)
    metadata = generate_metadata(plan=plan)
    script = generate_script(folder_name=metadata["folder_name"])

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "thumbnail_prompt": f"{metadata['thumbnail_prompt']}\n NO WRITING or INSCRIPTIONS",
        "folder_name": metadata["folder_name"],
        "script": script,
    }
