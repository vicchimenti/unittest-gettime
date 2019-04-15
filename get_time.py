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
        # print('Invalid Date Format, enter format MM-DD')
        return False
    # print("You entered a valid date")
    return True


# Test Suite of Valid MM-DD Inputs
def check_valid():
    # Test Case 1
    try:
        result = getdate('01-01')
        if result is True:
            print('01-01 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('01-01 Failed : Expected Result True : Actual Result False')
    # Test Case 2
    try:
        result = getdate('12-12')
        if result is True:
            print('12-12 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('12-12 Failed : Expected Result True : Actual Result False')
    # Test Case 3
    try:
        result = getdate('11-13')
        if result is True:
            print('11-13 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('11-13 Failed : Expected Result True : Actual Result False')
    # Test Case 4
    try:
        result = getdate('10-27')
        if result is True:
            print('10-27 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('10-27 Failed : Expected Result True : Actual Result False')
    # Test Case 5
    try:
        result = getdate('02-28')
        if result is True:
            print('02-28 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('02-28 Failed : Expected Result True : Actual Result False')
    # Test Case 6
    try:
        result = getdate('03-29')
        if result is True:
            print('03-29 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('03-29 Failed : Expected Result True : Actual Result False')
    # Test Case 7
    try:
        result = getdate('04-30')
        if result is True:
            print('04-30 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('04-30 Failed : Expected Result True : Actual Result False')
    # Test Case 8
    try:
        result = getdate('05-31')
        if result is True:
            print('05-31 Passed : Expected Result True : Actual Result True')
    except ValueError:
        print('05-31 Failed : Expected Result True : Actual Result False')


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


# date_input = input("Enter any month and day in the format MM-DD: ")
date_today = datetime.datetime.now()
print("Current Date/Time: ")
print(str(date_today))
# print(str(getdate(date_input)))
check_valid()
check_invalid()
