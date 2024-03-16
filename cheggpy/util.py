"""This module contains all the utility functions used in the main module."""
from os import system, path
from time import sleep
from random import randint

from colorama import Fore
from tqdm import trange
from .custom_exceptions import MaxRetryReached


def welcome_banner():
    """
    Display a welcome banner.
    """
    clear_screen()
    print(Fore.RED + """

    ▄████▄   ██░ ██ ▓█████   ▄████   ▄████     ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ███▄ ▄███▓ ▄▄▄      ▄▄▄█████▓ ██▓ ▒█████   ███▄    █
    ▒██▀ ▀█  ▓██░ ██▒▓█   ▀  ██▒ ▀█▒ ██▒ ▀█▒   ▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██▒▀█▀ ██▒▒████▄    ▓  ██▒ ▓▒▓██▒▒██▒  ██▒ ██ ▀█   █
    ▒▓█    ▄ ▒██▀▀██░▒███   ▒██░▄▄▄░▒██░▄▄▄░   ▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██    ▓██░▒██  ▀█▄  ▒ ▓██░ ▒░▒██▒▒██░  ██▒▓██  ▀█ ██▒
    ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ░▓█  ██▓░▓█  ██▓   ░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██    ▒██ ░██▄▄▄▄██ ░ ▓██▓ ░ ░██░▒██   ██░▓██▒  ▐▌██▒
    ▒ ▓███▀ ░░▓█▒░██▓░▒████▒░▒▓███▀▒░▒▓███▀▒    ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒   ░██▒ ▓█   ▓██▒  ▒██▒ ░ ░██░░ ████▓▒░▒██░   ▓██░
    ░ ░▒ ▒  ░ ▒ ░▒░ ░ ░ ░  ░  ░   ░   ░   ░      ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░  ░      ░  ▒   ▒▒ ░    ░     ▒ ░░ ░ ░ ▒     ░   ░ ░
      ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░   ░   ░      ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░      ░     ░   ▒     ░       ▒ ░░ ░ ░ ▒     ░   ░ ░
    ░         ░  ░░ ░   ░   ░ ░   ░ ░ ░   ░      ░  ░   ░                  ░ ░         ░         ░  ░          ░      ░ ░           ░
    ░ ░       ░  ░  ░   ░  ░      ░       ░          ░  ░   ░                  ░ ░         ░         ░  ░          ░      ░ ░           ░
    ░
                                              Made with ❤️️  by """ + Fore.GREEN + "\033]8;;https://github.com/Harry-kp\aHarry-kp\033]8;;\a\n")


def goodbye_banner():
    """
    Display a goodbye banner.
    """
    print(Fore.RED + """
      |                                                         <----------[Klark in the Zodiac]---------->                                                         |
    """
          )
    print("Found any bugs. Raise it here -> https://github.com/Harry-kp/cheggpy/issues")


def clear_screen():
    """
    Clear the screen.
    """
    system('clear')


def random_long_wait(min_time=5, max_time=10):
    '''
      Sleep the execution of scripts for x minutes where x is random value b/w [min_time,max_time]
    '''
    tym = randint(min_time, max_time) * 60
    for _ in trange(tym, desc='Sleeping 😴'):
        sleep(1)


def random_wait(min_time=5, max_time=10) -> None:
    """
    Wait for a random amount of time.
    """
    tym = randint(min_time, max_time)
    for _ in trange(tym, desc='Sleeping 😴'):
        sleep(1)


def play_success_notification():
    """
    Whenver an answerable question is found. Play the success notification sound.
    """
    mp3_path = path.join(path.dirname(__file__), 'assets', 'notify.mp3')
    system(f"afplay {mp3_path}")


def retry(max_retries=-1, exceptions=None):
    """
    Decorator that retries a function call a specified number of times if it raises specific exceptions.

    Args:
        max_retries (int, optional): The maximum number of retries. Set to -1 for unlimited retries. Defaults to -1.
        exceptions (Exception or tuple of Exception, optional): The exception(s) to catch and retry. Defaults to None.

    Returns:
        The decorated function.

    Raises:
        MaxRetryReached: If the maximum number of retries is reached and the function still raises an exception.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries or max_retries == -1:
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    retries += 1
                    print(str(err), f"Retrying {retries}..........")
                    if retries == max_retries:
                        raise MaxRetryReached('Max retries reached. Failed to fetch the question.') from err
                    random_long_wait()
            # This return statement is added to provide consistency
            return None  # or raise another exception here if needed
        return wrapper
    return decorator
