USER_ID_MAP = {
    "hacker": "84640273",
    "admin": "43274923"
}


USER_PASSWORD_MAP = {
    "84640273": "KJ87^&%^&3JLH",
    "43274923": "kjf73&@$*&Ykf"
}


def get_user_id(username: str):
    return USER_ID_MAP.get(username)


def authenticate_user(user_id: str, password: str):
    if not is_valid_user_id(user_id):
        return False

    use_password = USER_PASSWORD_MAP[user_id]
    if not use_password:
        return False

    if use_password != password:
        return False
    
    return True


def is_valid_username(username: str):
    return username in USER_ID_MAP


def is_valid_user_id(user_id: str):
    return user_id in USER_PASSWORD_MAP
