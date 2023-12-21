# Friendly Pairs I

## Topic: NUMBER THEORYALGORITHMS

'''
# Task:
-----
The Abundancy (A) of a number n is defined as:

(sum of divisors of n) / n

For example:
A(8) = (1 + 2 + 4 + 8) / 8 = 15/8
A(25) = (1 + 5 + 25) / 25  = 31/25
Friendly Pairs are pairs of numbers (m, n), such that their abundancies are equal: A(n) = A(m).

Write a function that returns "Friendly!" if the two given numbers are a Friendly Pair. Otherwise return their respective abundacies as strings separated by a space, e.g. "1 15/8"

Notes:
 - All fractions must be written in their most reduced form (e.g. 2/3 instead of 8/12)
 - Every number that is being checked is under 2400
 - Floats should be left on without rounding when you compare the abundancies of the two numbers

Examples:
n = 6, m = 28 ==> "Friendly!"
n = 3, m = 9  ==> "4/3 13/9"

# Sample Tests:
---------------
import codewars_test as test
from solution import friendly_numbers

@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(friendly_numbers(6, 28), 'Friendly!')
        test.assert_equals(friendly_numbers(3, 9), '4/3 13/9')
        test.assert_equals(friendly_numbers(10, 11), '9/5 12/11')
        test.assert_equals(friendly_numbers(138, 644), 'Friendly!')

# Code:
-------
def friendly_numbers(m, n):
    """
    Input
    m - first integer 
    n - second integer
    
    Return
    'Friendly!' if they are friendly pairs
    else
    'Am An' (their abundancies as rational strings)
    """
    pass

'''

# Solution:
