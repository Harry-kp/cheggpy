"""
This module contains custom exception classes.
"""
# custom_exceptions.py


class CustomError(Exception):
    """Base class for custom exceptions."""


class EmptyQueue(CustomError):
    """Raised when the question queue is empty."""

    def __init__(self, message):
        """
        Initialize an instance of EmptyQueue.

        Args:
                message (str): The error message associated with the exception.

        """
        self.message = message
        super().__init__(self.message)


class NoQuestionToSkip(CustomError):
    """Raised when there is no question to skip."""

    def __init__(self, message):
        """
        Initialize an instance of NoQuestionToSkip.

        Args:
                message (str): The error message associated with the exception.

        """
        self.message = message
        super().__init__(self.message)


class MaxRetryReached(CustomError):
    """Raised when the maximum number of retries is reached."""

    def __init__(self, message):
        """
        Initialize an instance of MaxRetryReached.

        Args:
                message (str): The error message associated with the exception.

        """
        self.message = message
        super().__init__(self.message)
