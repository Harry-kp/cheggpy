"""Module only used for the login part of the script"""
import json


def login_user(username, password, session):
    """
    Logins the user with the given username and password.

    Args:
        username (str): The username or email of the user.
        password (str): The password of the user.
        session (requests.Session): The session object to use for the request.

    Returns:
        requests.Session: The session object after logging in.
    """
    assert username, "Username not provided"
    assert password, "Password not provided"

    chegg_login_url = "https://expert.chegg.com/api/auth/login"
    payload = json.dumps({
        "email": username,
        "password": password
    })
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"macOS"',
    }

    response = session.post(chegg_login_url, headers=headers, data=payload)
    response.raise_for_status()  # Raise exception for non-2xx status codes
    return session
