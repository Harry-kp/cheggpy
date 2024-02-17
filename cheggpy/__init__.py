"""This module is the main module of the package and is used to interact with the Chegg API"""
from os import environ
from time import sleep
from requests import Session, RequestException
from .login_util import login_user
from .logout_util import logout_user
from .question_util import fetch_latest_question, skip_latest_question, analyze_question
from .question import Question


class CheggPy:
    """Class to interact with Chegg API"""

    def __init__(self, username=None, password=None, keywords=None):
        self.username = username or environ.get('CHEGG_USER')
        self.password = password or environ.get('CHEGG_PW')
        self.keywords = keywords or []
        self.session = Session()
        self.latest_question = Question()

    def login(self):
        """Login the user with the provided username and password"""
        try:
            self.session = login_user(
                self.username, self.password, self.session)
            print('Logged in successfully')
            sleep(3)
        except AssertionError as err:
            print(str(err))
            raise
        except RequestException as err:
            print('Login failed:', err)
            raise
        return self

    def logout(self):
        """Logout the user"""
        try:
            logout_user(self.session)
            print('Logged out successfully')
            sleep(3)
        except NotImplementedError as err:
            print(str(err))

    def fetch_question(self):
        """Fetch the latest question"""
        try:
            self.latest_question = Question(
                fetch_latest_question(self.session))
            print('Fetched the latest question successfully with id:',
                  self.latest_question.id)
            sleep(3)
        except NotImplementedError as err:
            print(str(err))
        return self

    def skip_question(self):
        """Skip the latest question"""
        try:
            skip_latest_question(self.session, self.latest_question)
            print('Skipped the latest question successfully with id:',
                  self.latest_question.id)
            sleep(3)
        except NotImplementedError as err:
            print(str(err))
        return self

    def is_question_answerable(self):
        """Check if the latest question is answerable"""
        if analyze_question(self.latest_question, self.keywords):
            return True
        return False
