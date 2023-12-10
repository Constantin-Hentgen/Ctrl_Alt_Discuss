from openai import OpenAI
from requests import get
from os import getenv

# local imports
from configuration import STABLE_DIFFUSION_MODEL


def download_thumbnail(url: str, save_path: str) -> None:
    try:
        response = get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Thumbnail downloaded successfully and saved at {save_path}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_thumbnail(
    prompt: str,
    path: str,
    quantity: int = 1,
    pixels: int = 1024,
    model: str = STABLE_DIFFUSION_MODEL,
    quality: str = "standard",
) -> None:
    OPENAI_API_KEY = getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=f"{pixels}x{pixels}",
        quality=quality,
        n=quantity,
    )

    thumbnail_url = response.data[0].url
    download_thumbnail(url=thumbnail_url, save_path=f"{path}\\thumbnail.png")
