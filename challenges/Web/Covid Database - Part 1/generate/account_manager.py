USER_ID_MAP = {
    "hacker": "84640273",
    "admin": "43274923"
}


USER_INFO_MAP = {
    "84640273": {
        "name": "hacker",
        "email": "hacker@covid.io",
        "password": "KJ87^&%^&3JLH",
        "bio": "Eat. Sleep. Hacker."
    },
    "43274923": {
        "name": "admin",
        "email": "admin@covid.io",
        "password": "kjf73&@$*&Ykf",
        "bio": "HNF{yAyYyY_aDmiN_AcceSs}"
    }
}


def get_users() -> dict:
    return USER_ID_MAP


def get_user_info(user_id: str) -> dict:
    return USER_INFO_MAP.get(user_id)


def get_user_id(username: str) -> str:
    return USER_ID_MAP.get(username)


def authenticate_user(user_id: str, password: str) -> bool:
    if not is_valid_user_id(user_id):
        return False

    user_info = get_user_info(user_id)
    if not user_info:
        return False

    if user_info["password"] != password:
        return False
    
    return True


def is_valid_username(username: str) -> bool:
    return username in USER_ID_MAP


def is_valid_user_id(user_id: str) -> bool:
    return user_id in USER_INFO_MAP
