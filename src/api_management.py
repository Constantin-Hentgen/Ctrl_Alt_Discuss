from elevenlabs import set_api_key, User

# local imports
from secrets import XI_API_KEY


def xi_labs_characters_left() -> int:
    set_api_key(XI_API_KEY)
    user = User.from_api()
    characters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return characters_left
