from elevenlabs import set_api_key, User
from configuration import XI_API_KEYS


def get_characters_left(xi_api_key: str) -> int:
    set_api_key(xi_api_key)
    user = User.from_api()
    characters_left = (
        user.subscription.character_limit - user.subscription.character_count
    )
    return characters_left


def is_xi_possible(line: str, xi_api_key: str) -> bool:
    return (
        True if get_characters_left(xi_api_key=xi_api_key) - len(line) >= 0 else False
    )


def get_xi_api_key(line: str) -> str:
    for key in XI_API_KEYS:
        if is_xi_possible(line=line, xi_api_key=key):
            characters_left = get_characters_left(xi_api_key=key)
            count_characters = len(line)
            print(
                f"key:{key} - balance:{characters_left} - future balance:{characters_left-count_characters}"
            )
            return key
    print("You’re broke :(")


def is_podcast_possible(script: list) -> bool:
    super_string = "".join(
        item["line"] for item in script if item["name"] != "Transition"
    )
    return True if len(super_string) <= get_nb_credits_left() else False


def get_nb_credits_left() -> int:
    try:
        return sum([get_characters_left(xi_api_key=key) for key in XI_API_KEYS])
    except Exception as e:
        print(f"Error occurred: {e}")
