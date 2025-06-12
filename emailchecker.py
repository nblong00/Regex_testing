import re
import time

email_pattern = re.compile(r'''
                           ^[-\w\d.+]+@[-\w\d+]+\.[\w\d-]+\.?
                           [\w\d-]+?\.?[\w\d-]+?$
                           ''', re.X)

user_email = input("Enter an email to check> ")

if email_pattern.match(user_email):
    print("Correct email format used.\nClosing...")
    time.sleep(2)
    exit()
else:
    print("That email doesn't match current email format expectations\nClosing...")
    time.sleep(2)
    exit()
