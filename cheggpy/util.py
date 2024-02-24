"""This module contains all the utility functions used in the main module."""
from os import system, path
from time import sleep
from random import randint

from colorama import Fore
from tqdm import trange


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

    print(Fore.RED + """
      |----------------------------------------------------------Klark in the Zodiac----------------------------------------------------------|
      |---------------------------------------------------------------------------------------------------------------------------------------|
    """
          )


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
    print(f"Waiting for {tym} seconds..........")
    for _ in trange(tym):
        sleep(1)


def random_wait(min_time=5, max_time=10) -> None:
    """
    Wait for a random amount of time.
    """
    tym = randint(min_time, max_time)
    print(f"Waiting for {tym} seconds..........")
    for _ in trange(tym):
        sleep(1)


def play_success_notification():
    """
    Whenver an answerable question is found. Play the success notification sound.
    """
    mp3_path = path.join(path.dirname(__file__), 'assets', 'notify.mp3')
    system(f"afplay {mp3_path}")
