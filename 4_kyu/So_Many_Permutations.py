# So Many Permutations!

# Topic: PERMUTATIONS, STRINGS, ALGORITHMS

'''
# Task: 
--------
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

Note: The order of the permutations doesn't matter.
Good luck!

# Sample Tests:
----------------
import codewars_test as test
from solution import permutations

@test.describe("Basic Tests")
def basic_tests():
    
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(sorted(permutations('a')), ['a']);
        test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
        test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


# Code:
-------
def permutations(s):
    # Code Away!

'''
# Solution:

from itertools import permutations as itertools_permutations

def permutations(s):
    # Use itertools.permutations to generate all permutations
    # Then convert each permutation tuple to a string
    # Use set to remove duplicates
    return list(set(''.join(p) for p in itertools_permutations(s)))

# Testing the function with the provided sample tests
test_cases = ['a', 'ab', 'aabb']
results = {s: sorted(permutations(s)) for s in test_cases}
results


# Description:
'''
Here's the implementation of the permutations function, along with the results of the sample tests.
The function permutations(s) generates all unique permutations of the string s and returns them as a list. It uses the itertools.permutations
function to create all permutations and a set to eliminate duplicates. Each permutation is a tuple, which is then joined into a string.

'''
