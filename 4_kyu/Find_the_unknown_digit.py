# Find the unknown digit.

# Topic: MATHEMATICS, ALGORITHMS, PUZZLES.

'''
# Task:
-------
Base 10 system, and that they never start a number with a leading zero. He's figured out most of the digits as well as a few operators, 
but he needs your help to figure out the rest.

The professor will give you a simple math expression, of the form

[number][op][number]=[number]

He has converted all of the runes he knows into digits. The only operators he knows are addition (+),subtraction(-), and multiplication (*), 
so those are the only ones that will appear. Each number will be in the range from -1000000 to 1000000, and will consist of only the digits 0-9, 
possibly a leading -, and maybe a few ?s. If there are ?s in an expression, they represent a digit rune that the professor doesn't know (never 
an operator, and never a leading -). All of the ?s in an expression will represent the same digit (0-9), and it won't be one of the other given 
digits in the expression. No number will begin with a 0 unless the number itself is 0, therefore 00 would not be a valid number.

Given an expression, figure out the value of the rune represented by the question mark. If more than one digit works, give the lowest one. 
If no digit works, well, that's bad news for the professor - it means that he's got some of his runes wrong. output -1 in that case.

Complete the method to solve the expression to find the value of the unknown rune. The method takes a string as a paramater repressenting the 
expression and will return an int value representing the unknown rune or -1 if no such rune exists.



# Sample Tests:
----------------
from solution import solve_runes
import codewars_test as test

@test.describe('Find the unknown digit')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(solve_runes("1+1=?"), 2, "Answer for expression '1+1=?' ");
        test.assert_equals(solve_runes("123*45?=5?088"), 6, "Answer for expression '123*45?=5?088' ");
        test.assert_equals(solve_runes("-5?*-1=5?"), 0, "Answer for expression '-5?*-1=5?' ");
        test.assert_equals(solve_runes("19--45=5?"), -1, "Answer for expression '19--45=5?' ");
        test.assert_equals(solve_runes("??*??=302?"), 5, "Answer for expression '??*??=302?' ");
        test.assert_equals(solve_runes("?*11=??"), 2, "Answer for expression '?*11=??' ");
        test.assert_equals(solve_runes("??*1=??"), 2, "Answer for expression '??*1=??' ");

        

# Code:
-------
def solve_runes(runes):
    # Your code here
    pass

'''
# Solution:

import re

def solve_runes(runes):
    for d in sorted(set("0123456789") - set(runes)):
        # Replace '?' with digit and split the expression
        try:
            left, right = runes.replace('?', d).split('=')
        except ValueError:
            # Invalid expression format
            return -1

        # Check for leading zeros in numbers, except for the single digit '0'
        if re.search(r'\b0[0-9]', left) or re.search(r'\b0[0-9]', right):
            continue

        # Evaluate the expression
        try:
            if eval(left) == eval(right):
                return int(d)
        except:
            continue
    return -1

# Retest specifically the "?*11=??" case
test_case = "?*11=??"
solve_runes(test_case)

