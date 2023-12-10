from elevenlabs import set_api_key, User
from os import getenv


def xi_labs_characters_left() -> int:
    XI_API_KEY = getenv("XI_API_KEY")
    set_api_key(XI_API_KEY)
    user = User.from_api()
    characters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return characters_left
