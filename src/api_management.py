from elevenlabs import set_api_key, User


def get_caracters_left(XI_API_KEY: str) -> int:
    set_api_key(XI_API_KEY)
    user = User.from_api()
    caracters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return caracters_left
