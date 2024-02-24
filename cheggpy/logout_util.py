"""Module only used for the login part of the script"""


def logout_user(session):
    """Logins the user with the given username and password"""

    chegg_logout_url = "https://expert.chegg.com/api/auth/logout"
    session.request("POST", chegg_logout_url)
    session.close()
