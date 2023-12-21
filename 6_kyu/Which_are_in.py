# Which are in?
# Topic: ARRAYS, LISTS, STRINGS, REFACTORING

'''
# Task:
--------
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.

# Sample Tests:
----------------
import codewars_test as test
    
@test.describe("in_array")
def tests():
    def testing(array1, array2, expect):
        actual = in_array(array1, array2)
        test.assert_equals(actual, expect)
    @test.it("Basic tests")
    def basics():
        a1 = ["live", "arp", "strong"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp', 'live', 'strong']
        testing(a1, a2, r)          
        a1 = ["arp", "mice", "bull"] 
        a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
        r = ['arp']
        testing(a1, a2, r)           

# Code:
--------
def in_array(array1, array2):
    # your code
    return []

'''
# Solution:
def in_array(array1, array2):
    # Create an empty set to store unique matching strings
    result_set = set()

    # Check if each string in array1 is a substring of any string in array2
    for string1 in array1:
        for string2 in array2:
            if string1 in string2:
                result_set.add(string1)
                break

    # Convert the set to a sorted list
    return sorted(result_set)

# Test cases
a1_1 = ["arp", "live", "strong"]
a2_1 = ["lively", "alive", "harp", "sharp", "armstrong"]
result_1 = in_array(a1_1, a2_1)

a1_2 = ["tarp", "mice", "bull"]
a2_2 = ["lively", "alive", "harp", "sharp", "armstrong"]
result_2 = in_array(a1_2, a2_2)

a1_3 = ["live", "arp", "strong"]
a2_3 = ["lively", "alive", "harp", "sharp", "armstrong"]
result_3 = in_array(a1_3, a2_3)

a1_4 = ["arp", "mice", "bull"]
a2_4 = ["lively", "alive", "harp", "sharp", "armstrong"]
result_4 = in_array(a1_4, a2_4)

result_1, result_2, result_3, result_4

# Description:
'''
The Python function in_array successfully solves the task. It returns a sorted array of strings from the first array (a1) that are 
substrings of any string in the second array (a2).
The function ensures that the result contains unique strings and is sorted in lexicographical order. ​​

'''





