from elevenlabs import set_api_key, User


def get_caracters_left(XI_API_KEY: str) -> int:
    set_api_key(XI_API_KEY)
    user = User.from_api()
    caracters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return caracters_left


def count_caracters(script: list) -> int:
    return len("".join([item["line"] for item in script]))


def is_xi_possible(script: list) -> bool:
    return True if get_caracters_left() - count_caracters(script=script) >= 0 else False
