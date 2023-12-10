from openai import OpenAI
from json import loads

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
    return generate_content(prompt=PROMPT_PLAN)


def generate_metadata(plan: dict) -> dict:
    return generate_content(preprompt=PREPROMPT_METADATA, prompt=str(plan))


def generate_development(plan: dict) -> dict:
    plan_list = plan["plan"]
    development = []

    for part in plan_list:
        temp_prompt = (
            f"{PROMPT_DEVELOPMENT}"
            f"\nthe name of the part you have to write is :"
            f"{part['title']}"
            f", and follow this instruction to write a good dialogue : "
            f"{part['description']}"
        )
        development.append(generate_content(prompt=temp_prompt))

    return development


def generate_introduction(plan: dict) -> dict:
    return generate_content(prompt=PROMPT_INTRODUCTION)


def generate_conclusion() -> dict:
    return generate_content(prompt=PROMPT_CONCLUSION)


def generate_podcast() -> dict:
    plan = generate_plan()
    metadata = generate_metadata(plan)
    introduction = generate_introduction(plan)
    development = generate_development(plan)
    conclusion = generate_conclusion()

    return {
        "title": metadata["title"],
        "description": metadata["description"],
        "thumbnail_prompt": f"{metadata['thumbnail_prompt']}\n NO WRITING or INSCRIPTIONS",
        "folder_name": metadata["folder_name"],
        "script": introduction["script"]
        + [line for chapter in development for line in chapter["script"]]
        + conclusion["script"],
    }
