# Integers: Recreation One

# Topic: FUNDAMENTALS, ALGORITHMS.

'''
# Task:
--------
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246. Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681. The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string. The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors
of which is a square and then the sum of the squared divisors.

Example:
list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note:
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

# Sample Tests:
---------------
import codewars_test as test
from solution import list_squared

@test.describe('Tests...')
def _():
    @test.it('Fixed Tests')
    def _():
        test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
        test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
        test.assert_equals(list_squared(250, 500), [[287, 84100]])

# Code:
--------
def list_squared(m, n):
    # your code
    pass

'''
# Solution:

# Revised function with comments explaining each part of the code
def list_squared(m, n):
    # Function to calculate the sum of squared divisors of a number
    def sum_of_squared_divisors(num):
        # Initialize an empty set to store unique divisors
        divisors = set()
        # Iterate through potential divisors up to the square root of the number
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                # Add both the divisor and its complement to the set
                divisors.add(i)
                divisors.add(num // i)
        # Return the sum of the squares of the divisors
        return sum(d**2 for d in divisors)

    # Initialize an empty list to store the results
    result = []
    # Iterate through numbers from m to n
    for num in range(m, n + 1):
        # Calculate the sum of squared divisors for the number
        sum_squares = sum_of_squared_divisors(num)
        # Check if the sum is a perfect square
        if (sum_squares**0.5).is_integer():
            # Add the number and its sum of squared divisors to the result list
            result.append([num, sum_squares])

    return result

# Testing the function with the provided sample tests
test_cases = [(1, 250), (42, 250), (250, 500)]
results = {f"{m}-{n}": list_squared(m, n) for m, n in test_cases}
results

# Description:
'''
Here's the implementation of the list_squared function, which finds all integers between m and n such that the sum of their squared divisors is itself a square.
The function has been tested with the provided sample tests and produces the correct results.
'''
