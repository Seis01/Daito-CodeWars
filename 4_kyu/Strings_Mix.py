# Strings Mix.

# Topic: FUNDAMENTALS, STRINGS.

'''
# Task:
-------
Given two strings s1 and s2, we want to visualize how different the two strings are. We will only take into account the lowercase letters (a to z). First let us count the frequency of each 
lowercase letters in s1 and s2.

s1 = "A aaaa bb c"

s2 = "& aaa bbb c d"

s1 has 4 'a', 2 'b', 1 'c'

s2 has 3 'a', 3 'b', 1 'c', 1 'd'

So the maximum for 'a' in s1 and s2 is 4 from s1; the maximum for 'b' is 3 from s2. In the following we will not consider letters when the maximum of their occurrences is less than or equal to 1.

We can resume the differences between s1 and s2 in the following string: "1:aaaa/2:bbb" where 1 in 1:aaaa stands for string s1 and aaaa because the maximum for a is 4. In the same manner 2:bbb stands 
for string s2 and bbb because the maximum for b is 3.

The task is to produce a string in which each lowercase letters of s1 or s2 appears as many times as its maximum if this maximum is strictly greater than 1; these letters will be prefixed by the 
number of the string where they appear with their maximum value and :. If the maximum is in s1 as well as in s2 the prefix is =:.

In the result, substrings (a substring is for example 2:nnnnn or 1:hhh; it contains the prefix) will be in decreasing order of their length and when they have the same length sorted in ascending 
lexicographic order (letters and digits - more precisely sorted by codepoint); the different groups will be separated by '/'. See examples and "Example Tests".

Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"

Note for Swift, R, PowerShell
The prefix =: is replaced by E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"



# Sample Tests:
---------------
import codewars_test as test
from solution import mix

@test.describe("Mix")
def _():
    @test.it("Basic Tests")
    def _():
        test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        test.assert_equals(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        test.assert_equals(mix("codewars", "codewars"), "")
        test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


# Code:
--------
def mix(s1, s2):
    # your code
    
'''
# Solution:
from collections import Counter

def mix(s1, s2):
    # Count the frequency of each lowercase letter in both strings
    counter1 = Counter(filter(str.islower, s1))
    counter2 = Counter(filter(str.islower, s2))

    # Create a list to hold the result parts
    result_parts = []

    # Combine the keys from both counters
    all_keys = set(counter1.keys()) | set(counter2.keys())

    for key in all_keys:
        count1 = counter1[key]
        count2 = counter2[key]

        # Only consider letters with a maximum count greater than 1
        if max(count1, count2) > 1:
            if count1 > count2:
                # String 1 has more of this letter
                result_parts.append(f"1:{key * count1}")
            elif count2 > count1:
                # String 2 has more of this letter
                result_parts.append(f"2:{key * count2}")
            else:
                # Both strings have the same count of this letter
                result_parts.append(f"=:{key * count1}")

    # Sort the result parts first by length (descending) and then lexicographically
    result_parts.sort(key=lambda x: (-len(x), x))

    return '/'.join(result_parts)

# Sample tests
test_cases = [
    ("Are they here", "yes, they are here"),
    ("Sadus:cpms>orqn3zecwGvnznSgacs", "MynwdKizfd$lvse+gnbaGydxyXzayp"),
    ("looping is fun but dangerous", "less dangerous than coding"),
    (" In many languages", " there's a pair of functions"),
    ("Lords of the Fallen", "gamekult"),
    ("codewars", "codewars"),
    ("A generation must confront the looming ", "codewarrs")
]

results = [mix(tc[0], tc[1]) for tc in test_cases]
results

# Description:
'''
The function correctly identifies and compares the frequency of each lowercase letter in both strings, considering only 
those with a maximum count greater than 1. It then formats the result as specified, with substrings ordered first by
length (descending) and then lexicographically
'''
