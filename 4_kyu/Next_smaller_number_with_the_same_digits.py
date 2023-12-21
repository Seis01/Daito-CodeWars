# Next smaller number with the same digits

# Topic: STRINGS, MATHEMATICS, ALGORITHMS.

'''
# Task:
--------
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller 
number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

- some tests will include very large numbers.
- test data only employs positive integers.

The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."

# Sample Tests:
---------------
import codewars_test as test
from solution import next_smaller
@test.describe('Fixed Tests')
def fixed_tests():
    @test.it('Simple Cases')
    def example_cases():
        test.assert_equals(next_smaller(907), 790)
        test.assert_equals(next_smaller(531), 513)
        test.assert_equals(next_smaller(135), -1)
        test.assert_equals(next_smaller(2071), 2017)
        test.assert_equals(next_smaller(414), 144)
        test.assert_equals(next_smaller(123456798), 123456789)
        test.assert_equals(next_smaller(123456789), -1)
        test.assert_equals(next_smaller(1234567908), 1234567890)

# Code:
--------
def next_smaller(n):
    pass

'''
# Solution
def next_smaller(n):
    digits = list(str(n))
    length = len(digits)

    # Find the pivot point where the digit to the left is greater than the digit to the right
    pivot = -1
    for i in range(length - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            pivot = i - 1
            break

    # If no pivot is found, there's no smaller number with the same digits
    if pivot == -1:
        return -1

    # Find the rightmost digit greater than the pivot but the smallest among them
    for i in range(length - 1, pivot, -1):
        if digits[i] < digits[pivot]:
            # Swap the pivot with this digit
            digits[i], digits[pivot] = digits[pivot], digits[i]
            break

    # Reverse the digits after the pivot
    digits[pivot + 1:] = reversed(digits[pivot + 1:])

    # Join digits and convert to integer
    result = int(''.join(digits))

    # Check if the result has leading zeros or is the same as the original number
    if result < n and len(str(result)) == length:
        return result
    else:
        return -1

# Test cases
test_cases = [907, 531, 135, 2071, 414, 123456798, 123456789, 1234567908]
results = [next_smaller(tc) for tc in test_cases]
results

# Description:
'''
The function next_smaller successfully solves the task. It finds the next smaller positive integer that contains the same digits as the given number.
The function adheres to the conditions, including not allowing numbers with leading zeros and returning -1 when no smaller number exists with the same digits.

'''

