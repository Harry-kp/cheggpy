"""The module that handles a question and its properties of Chegg"""
from bs4 import BeautifulSoup


class Question:
    """Class to represent a question in Chegg"""

    def __init__(self, response=None):
        response = response or {}
        question = response.get('data', {}).get(
            'nextQuestionAnsweringAssignment', {}).get('question', {})
        self.id = question.get('id')
        self.uuid = question.get('uuid')
        self.body = self.__sanitize_html(question.get('body', "") or "")
        self.transcription = self.__sanitize_html(
            question.get('imageTranscriptionText', "") or "")

    def __str__(self):
        return f"Body: {self.body}\nTranscription: {self.transcription}"

    def __sanitize_html(self, html_data):
        return BeautifulSoup(html_data, 'html.parser').get_text()
