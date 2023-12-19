from elevenlabs import set_api_key, User
from configuration import XI_API_KEYS


def get_characters_left(xi_api_key: str) -> int:
    set_api_key(xi_api_key)
    user = User.from_api()
    characters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return characters_left


def is_xi_possible(script: list, xi_api_key: str) -> bool:
    return (
        True
        if get_characters_left(xi_api_key=xi_api_key) - count_characters(script=script)
        >= 0
        else False
    )


def count_characters(script: list) -> int:
    return len("".join([item["line"] for item in script]))


def get_xi_api_key(script: str) -> str:
    for key in XI_API_KEYS:
        if is_xi_possible(script=script, xi_api_key=key):
            return key
    print("You’re broke :(")
