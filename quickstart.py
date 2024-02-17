"""A simple script to demonstrate the usage of CheggPy."""
from cheggpy import CheggPy
chegg = CheggPy(username='22harshit23@gmail.com',
                password='Harry@5387091',
                keywords=['python', 'java', 'c++'],
                ).login()
try:
    while True:
        chegg.fetch_question()
        if chegg.is_question_answerable():
            skip = input(
                "Press enter to continue or press any other key to stop the script.")
            if skip == "":
                chegg.skip_question()
            else:
                raise KeyboardInterrupt
        else:
            chegg.skip_question()
except KeyboardInterrupt:
    print("Script stopped by user.")
    chegg.logout()
