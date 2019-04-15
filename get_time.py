#   Victor Chimenti
#   CPSC 5210 Testing and Debugging
#   19SQ Seattle University
#   get_time.py
#   A program to unit test a valid date format


"""
    This program uses the datetime library to validate user input for correct date entry.
    The user is only required to enter Month and Day so the program will not account for leap years.
    In the case of February 29 or greater, the results should always return false.
"""


import datetime


def getdate(date_in):
    try:
        datetime.datetime.strptime(date_in, '%m-%d')
    except ValueError:
        print('Invalid Date Format, enter format MM-DD')
        return False
    print("You entered a valid date")
    return True


date_input = input("Enter any month and day in the format MM-DD: ")
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))
print(str(getdate(date_input)))
