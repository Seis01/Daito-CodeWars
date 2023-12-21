# Nesting Structure Comparison.

# Topic: ARRAYS, ALGORITHMS.

'''
# Task:
-------
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding
length of nested arrays as the first array.

For example:

# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )


# Sample Tests:
----------------
from solution import same_structure_as
import codewars_test as test

test.assert_equals(same_structure_as([1,[1,1]],[2,[2,2]]), True, "[1,[1,1]] same as [2,[2,2]]")
test.assert_equals(same_structure_as([1,[1,1]],[[2,2],2]), False, "[1,[1,1]] not same as [[2,2],2]")

# Code:
--------
def same_structure_as(original,other):
    pass
'''
# Solution
def same_structure_as(original, other):
    # Check if both are lists
    if isinstance(original, list) and isinstance(other, list):
        # Check if the lengths of the lists are equal
        if len(original) == len(other):
            # Recursively check each element in the lists
            for orig_elem, other_elem in zip(original, other):
                if not same_structure_as(orig_elem, other_elem):
                    return False
            return True
        else:
            return False
    else:
        # If both elements are not lists, they are considered having the same structure
        return not isinstance(original, list) and not isinstance(other, list)

# Test cases
test_cases = [
    ([1, [1, 1]], [2, [2, 2]]), 
    ([1, [1, 1]], [[2, 2], 2]), 
    ([[[], []]], [[[], []]]),
    ([[[], []]], [[1, 1]])
]

results = [same_structure_as(tc[0], tc[1]) for tc in test_cases]
results

# Description:
'''
The same_structure_as function accurately determines whether two arrays have the same nesting structure and the same corresponding length of nested arrays. 
The function works correctly for arrays with various levels of nesting and checks both the structure and the length of nested arrays.
'''

    
