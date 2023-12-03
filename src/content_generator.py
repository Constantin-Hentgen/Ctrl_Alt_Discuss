from openai import OpenAI
from json import loads

# local imports
from secrets import OPENAI_API_KEY_THB as OPENAI_API_KEY


def generate_content(model: str, preprompt: str, prompt: str) -> str:
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
