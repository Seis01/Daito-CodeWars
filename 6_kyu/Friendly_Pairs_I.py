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
def gcd(a, b):
    # Function to calculate the greatest common divisor (GCD) of two numbers
    while b:
        a, b = b, a % b
    return a

def reduce_fraction(num, den):
    # Function to reduce a fraction to its lowest terms
    greatest_common_divisor = gcd(num, den)  # Find the GCD of the numerator and denominator
    return f"{num // greatest_common_divisor}/{den // greatest_common_divisor}"

def abundancy(num):
    # Function to calculate the abundancy of a number
    divisors_sum = sum(i for i in range(1, num + 1) if num % i == 0)  # Sum the divisors of the number
    return reduce_fraction(divisors_sum, num)  # Return the abundancy in reduced fractional form

def friendly_numbers(m, n):
    # Function to determine if numbers m and n are friendly pairs
    abundancy_m = abundancy(m)  # Calculate the abundancy for m
    abundancy_n = abundancy(n)  # Calculate the abundancy for n

    if abundancy_m == abundancy_n:
        # If the abundancies are equal, the numbers are friendly
        return "Friendly!"
    else:
        # Otherwise, return the abundancies in reduced fractional form
        return f"{abundancy_m} {abundancy_n}"

# Example tests
print(friendly_numbers(6, 28))  # "Friendly!"
print(friendly_numbers(3, 9))   # "4/3 13/9"
print(friendly_numbers(10, 11)) # "9/5 12/11"
print(friendly_numbers(138, 644)) # "Friendly!"




# Description:
'''
To determine if two numbers m and n are friendly pairs, we need to calculate their abundancies A(m) and A(n) and compare them.
If A(m) is equal to A(n), they are friendly pairs. If not, we need to return their respective abundancies as reduced rational strings.

To calculate the abundancy of a number n, we sum the divisors of n and divide by n. To calculate the divisors, we iterate through numbers
from 1 to n and add those that divide n evenly.

This code first calculates the abundancies of m and n, then compares them. If they are equal, it returns "Friendly!" as required. Otherwise,
it returns their respective abundancies as reduced rational strings.

'''
