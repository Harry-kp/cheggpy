# __main__.py

import argparse
import sys
from cheggpy import CheggPy
from .util import goodbye_banner
from requests.exceptions import HTTPError


def parse_args():
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="Your Chegg username", required=True)
    parser.add_argument("-p", "--password", help="Your Chegg password", required=True)
    parser.add_argument("-k", "--keywords", help="Keywords to search for in a chegg question to answer", nargs="+", required=True)
    parser.add_argument("-st", "--short_timeout", help="A tuple of two integers representing the range of short timeouts. Default, (5, 10) means the timeout will be between 5 and 10 seconds. This is used for the time between subsequent API requests.", nargs=2, type=int, default=[5, 10])
    parser.add_argument("-lt", "--long_timeout", help="A tuple of two integers representing the range of long timeouts. Default, (5, 10) means the timeout will be between 5 and 10 minutes. This is used to wait when there are no questions to answer.", nargs=2, type=int, default=[5*60, 10*60])

    args = parser.parse_args()
    return args


def main():
    """Run the script to fetch and start ananlyzing the latest question"""
    args = parse_args()
    chegg = CheggPy(username=args.username,
                    password=args.password,
                    keywords=args.keywords,
                    short_timeout=args.short_timeout,
                    long_timeout=args.long_timeout
                    )
    try:
        chegg.login()
        while True:
            chegg.fetch_question()
            if chegg.is_question_answerable():
                print("Hurray!! You got a suitable question to answer -> {}".format(CheggPy.DASHBOARD_URL))
                skip = input(
                    "Press enter to continue or press any other key to stop the script.")
                if skip == "":
                    chegg.skip_question()
                else:
                    raise KeyboardInterrupt
            else:
                chegg.skip_question()
    except HTTPError as e:
        print(e)
    except KeyboardInterrupt:
        print("Script stopped by user..........")
    finally:
        chegg.logout()
        goodbye_banner()
        sys.exit(0)


if __name__ == "__main__":
    main()
