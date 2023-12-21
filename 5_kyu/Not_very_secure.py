# Not very secure

# Topic: REGULAR EXPRESSIONSSTRINGS

'''
# Task:
--------
In this example you have to validate if a user input string is alphanumeric. The given string 
is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore

# Sample Tests:
---------------
@test.describe("Sample Tests")
def sample_tests():
    tests = [
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ]
    for s, b in tests:
        @test.it('alphanumeric("' + s + '")')
        def sample_test():
            test.assert_equals(alphanumeric(s), b)

# Code:
--------
def alphanumeric(password):
    pass
    

'''
# Solution:

import re  # Import the module for working with regular expressions

def alphanumeric(password):
    # Create a regular expression pattern for validation
    # ^ - start of the string, $ - end of the string
    # [a-zA-Z0-9] - any letter (uppercase or lowercase) or digit
    pattern = "^[a-zA-Z0-9]+$"

    # Check if the string matches the specified regular expression
    if re.match(pattern, password):
        return True  # If it matches, the string is alphanumeric
    else:
        return False  # If it doesn't match, the string is not alphanumeric




# Description:
'''  
This solution uses a regular expression that checks if the string contains
only letters (uppercase or lowercase) and digits, and does not contain 
spaces or underscores.

'''
