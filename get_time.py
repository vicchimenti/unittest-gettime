#   Victor Chimenti
#   CPSC 5210 Testing and Debugging
#   19SQ Seattle University
#   get_time.py
#   A program to unit test a valid date format
#   Created 4/15/2019


"""

    This program uses the datetime library to validate user input for correct date entry.
    The user is only required to enter Month and Day so the program will not account for leap years.
    In the case of February 29 or greater, the results should always return false.

    The user inputs are currently commented out so this program can run unit test validation.

"""


import datetime


def getdate(date_in):
    try:
        datetime.datetime.strptime(date_in, '%m-%d')
    except ValueError:
        # print('Invalid Date Format, enter format MM-DD') // for user input option only
        return False
    # print("You entered a valid date") // for user input option only
    return True


# Test Suite of Valid MM-DD Inputs
def check_valid():
    # Test Case 1
    test_input = '01-01'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 2
    test_input = '12-12'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 3
    test_input = '11-13'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 4
    test_input = '10-27'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 5
    test_input = '02-28'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 6
    test_input = '03-29'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 7
    test_input = '04-30'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')
    # Test Case 8
    test_input = '05-31'
    try:
        result = getdate(test_input)
        if result is True:
            print(test_input + ' Passed : Expected Result True : Actual Result True')
    except ValueError:
        print(test_input + ' Failed : Expected Result True : Actual Result False')


# Test Suite of InValid MM-DD Inputs
def check_invalid():
    # Test Case 9
    test_input = '00-00'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 10
    test_input = '13-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 11
    test_input = '27-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 12
    test_input = '28-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 13
    test_input = '29-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 14
    test_input = '30-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 15
    test_input = '31-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 16
    test_input = '07-32'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 17
    test_input = '-1-01'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 18
    test_input = '02-29'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 19
    test_input = '02-30'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')
    # Test Case 20
    test_input = '06-31'
    try:
        result = getdate(test_input)
        if result is False:
            print(test_input + ' Passed : Expected Result False : Actual Result False')
    except ValueError:
        print(test_input + ' Failed : Expected Result False : Actual Result True')


# Get Current Timestamp and Display
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))

# Run Unit Tests
check_valid()
check_invalid()

# Option for User Input
# date_input = input("Enter any month and day in the format MM-DD: ")
# print(str(getdate(date_input)))

# Get Current Timestamp and Display
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))
