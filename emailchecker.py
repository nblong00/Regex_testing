import re
import time


def email_pattern():
    email_pattern = re.compile(r'''
                               ^[-\w.+]+@[-\w+]+\.[-\w]+\.?
                               [-\w]+?\.?[-\w]+?$
                               ''', re.X)
    return email_pattern


def primary_logic_loop(email_pattern):
    user_email = input("Enter an email to check:\n> ")
    while 1 > 0:
        if email_pattern.match(user_email):
            print("Correct email format used.\n")
        else:
            print("That email doesn't match current email format expectations.\n")
        run_again = input("Want to check another email (yes/no):\n> ")
        if run_again in ["n", "no"]:
            print("Program closing...")
            time.sleep(1)
            exit()
        elif run_again in ["yes", "ye", "y"]:
            user_email = input("Enter new email to check:\n> ")
        elif run_again not in ["yes", "ye", "y", "n", "no"]:
            print("Invalid input.\nClosing....")
            time.sleep(1)
            exit()


def main():
    email_pattern = email_pattern()
    primary_logic_loop(email_pattern)


if __name__ == '__main__':
    main()
