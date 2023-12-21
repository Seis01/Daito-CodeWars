# Roman Numerals Helper.

# Topic: ALGORITHMS.

'''
# Task:
-------
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1
Help
Symbol	Value
I     	 1
IV	     4
V     	 5
X     	 10
L     	 50
C	       100
D	       500
M	       1000

# Sample Tests:
---------------
import codewars_test as test
from solution import RomanNumerals

@test.describe('fixed tests')
def fixed_tests():

    def do_test(input, expected):
        func = RomanNumerals.to_roman if type(input) is int else RomanNumerals.from_roman
        actual = func(input)
        test.assert_equals(actual, expected, f'testing {func.__name__}, for input {input}\n')

    @test.it('to roman')
    def fixed_tests_to():
        do_test(1000, 'M')
        do_test(4, 'IV')
        do_test(1, 'I')
        do_test(1990, 'MCMXC')
        do_test(2008, 'MMVIII')

    @test.it('from roman')
    def fixed_tests_from():
        do_test('XXI', 21)
        do_test('I', 1)
        do_test('IV', 4)
        do_test('MMVIII', 2008)
        do_test('MDCLXVI', 1666)

# Code:
-------
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        return ''

    @staticmethod
    def from_roman(roman_num : str) -> int:
        return 0

  

'''
# Solution:
class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        # Dictionary mapping integer values to Roman numeral symbols
        roman_numerals = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        result = ''  # Initialize an empty string to store the Roman numeral

        # Iterate through the dictionary in descending order of values
        for numeral_value, numeral_symbol in sorted(roman_numerals.items(), reverse=True):
            while val >= numeral_value:
                # Append the Roman numeral symbol to the result
                result += numeral_symbol
                # Subtract the corresponding value from the integer
                val -= numeral_value

        return result  # Return the Roman numeral string

    @staticmethod
    def from_roman(roman_num: str) -> int:
        # Dictionary mapping Roman numeral symbols to integer values
        roman_numerals = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
            'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
            'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
        }

        result = 0  # Initialize the result as zero
        i = 0  # Initialize an index variable to traverse the input string

        # Iterate through the input Roman numeral string
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i + 2] in roman_numerals:
                # If a two-character Roman numeral symbol is found, add its value to the result
                result += roman_numerals[roman_num[i:i + 2]]
                i += 2  # Move the index by 2 characters
            else:
                # If a one-character Roman numeral symbol is found, add its value to the result
                result += roman_numerals[roman_num[i]]
                i += 1  # Move the index by 1 character

        return result  # Return the integer value

# description:
'''
Modern Roman numerals are written by expressing each digit separately, starting with the leftmost digit and skipping any digit 
with a value of zero. In Roman numerals, 1990 is rendered as MCMXC (1000=M, 900=CM, 90=XC), and 2008 is written as MMVIII (2000=MM, 8=VIII).
The task is to create functions that can perform these conversions accurately.

Input Range:
The input integer for the to_roman function should satisfy: 1 <= n < 4000.
The input Roman numeral string for the from_roman function should follow the modern Roman numeral rules.
Note:
The Roman numerals should follow the provided symbol-value mapping.
The to_roman function should not use shorthand with 3 characters; the output should always be 6 characters long.

'''






