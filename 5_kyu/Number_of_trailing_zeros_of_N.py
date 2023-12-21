# Number of trailing zeros of N!

# Topic: ALGORITHMS, LOGIC, MATHEMATICS.

'''
# Task:
-------
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

# Sample Tests:
----------------
import codewars_test as test
from solution import zeros

@test.describe("Sample Tests")
def sample_tests():
    
    @test.it("Should pass sample tests")
    def sample_tests():
        test.assert_equals(zeros(0), 0, "Testing with n = 0")
        test.assert_equals(zeros(6), 1, "Testing with n = 6")
        test.assert_equals(zeros(30), 7, "Testing with n = 30")
        test.assert_equals(zeros(100), 24, "Testing with n = 100")
        test.assert_equals(zeros(1000), 249, "Testing with n = 1000")
        test.assert_equals(zeros(100000), 24999, "Testing with n = 100000")
        test.assert_equals(zeros(1000000000), 249999998, "Testing with n = 1000000000")

# Code:
-------
def zeros(n):
    return 0

'''
# Solution:

def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

# Testing the function with the provided sample tests
test_cases = [0, 6, 30, 100, 1000, 100000, 1000000000]
results = {n: zeros(n) for n in test_cases}
results


# Description:
'''
The function zeros(n) calculates the number of trailing zeros in the factorial of a given number n. It works by counting the number of 
times n can be divided by 5, since each such division represents a factor of 10 in the factorial (which comes from a pair of factors 2 
and 5, with 2s being more abundant).

'''
