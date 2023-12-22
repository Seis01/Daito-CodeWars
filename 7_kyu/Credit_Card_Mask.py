# Credit Card Mask
# Topic:

'''
# Task:
--------
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"


# Sample Tests:
----------------
from solution import maskify
import codewars_test as test

@test.describe('Sample tests')
def sample_tests():
    @test.it("masking: ''")
    def test1():
        test.assert_equals(maskify(''), '')
    
    @test.it("masking: '123'")
    def test2():
        test.assert_equals(maskify('123'), '123')
    
    @test.it("masking: 'SF$SDfgsd2eA'")
    def test3():
        test.assert_equals(maskify('SF$SDfgsd2eA'), '########d2eA')


# Code:
--------
# return masked string
def maskify(cc):

    pass



'''
# Solution:

# Define the maskify function
def maskify(cc):
    # If the length of the input string is less than or equal to 4, no masking is needed
    if len(cc) <= 4:
        return cc
    else:
        # Create a new string with "#" characters and keep the last 4 characters from the original string
        return '#' * (len(cc) - 4) + cc[-4:]

# Test cases
print(maskify(''))                  # Empty string should remain empty
print(maskify('123'))               # String with 3 characters should remain the same
print(maskify('SF$SDfgsd2eA'))     # Example with special characters and more than 4 characters
print(maskify('Skippy'))            # Example with a non-numeric string
print(maskify('Nananananananananananananananana Batman!'))  # Long string with masking

# Description:
'''
The maskify function checks if the input string length is less than or equal to 4 and returns it as is. 
If the length is greater than 4, it replaces all characters except the last 4 with "#".

'''

