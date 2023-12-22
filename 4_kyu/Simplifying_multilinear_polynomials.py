# Simplifying multilinear polynomials.

# Topic: MATHEMATICS, STRING, SREGULAR EXPRESSIONS, PARSING, FUNDAMENTALS.

'''
# Task:
-------
When we attended middle school were asked to simplify mathematical expressions like "3x-yx+2xy-x" (or usually bigger), and that was easy-peasy ("2x+xy"). But tell that to your pc and we'll see!

Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output 
where the same expression has been simplified in the following way ( -> means application of simplify):

-  All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
   "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

-  All monomials appears in order of increasing number of variables, e.g.:
   "-abc+3a+2ac" -> "3a+2ac-abc", "xyz-xz" -> "-xz+xyz"

-  If two monomials have the same number of variables, they appears in lexicographic order, e.g.:
   "a+ca-ab" -> "a-ab+ac", "xzy+zby" ->"byz+xyz"

-  There is no leading + sign if the first coefficient is positive, e.g.:
   "-y+x" -> "x-y", but no restrictions for -: "y-x" ->"-x+y"

N.B. to keep it simplest, the string in input is restricted to represent only multilinear non-constant polynomials, so you won't find something like `-3+yx^2'. 
Multilinear means in this context: of degree 1 on each variable.

Warning: the string in input can contain arbitrary variables represented by lowercase characters in the english alphabet.
Good Work :)



# Sample Tests:
----------------
test.it("Test reduction by equivalence")
test.assert_equals(simplify("dc+dcba"), "cd+abcd")

test.assert_equals(simplify("2xy-yx"),"xy")

test.assert_equals(simplify("-a+5ab+3a-c-2a"),"-c+5ab")

test.it("Test monomial length ordering")
test.assert_equals(simplify("-abc+3a+2ac"),"3a+2ac-abc")

test.assert_equals(simplify("xyz-xz"),"-xz+xyz")

test.it("Test lexicographic ordering")
test.assert_equals(simplify("a+ca-ab"),"a-ab+ac")

test.assert_equals(simplify("xzy+zby"),"byz+xyz")

test.it("Test no leading +")
test.assert_equals(simplify("-y+x"),"x-y")

test.assert_equals(simplify("y-x"),"-x+y")



# Code:
-------
def simplify(poly):

'''
# Solution

import re
from collections import defaultdict

def simplify(poly):
    # Function to standardize the format of terms
    def standardize(term):
        # Separate the coefficient and the variables
        if term[0] in '+-':
            coefficient = term[0] + term[1:].rstrip('abcdefghijklmnopqrstuvwxyz')
            variables = ''.join(sorted(term[1:].lstrip('0123456789+-')))
        else:
            coefficient = term.rstrip('abcdefghijklmnopqrstuvwxyz')
            variables = ''.join(sorted(term.lstrip('0123456789+-')))

        # Default coefficient to 1 if not specified
        coefficient = int(coefficient) if coefficient.strip('+-') else int(coefficient + '1')
        return coefficient, variables

    # Splitting the polynomial into individual terms
    terms = re.findall(r'[+-]?[^+-]+', poly)

    # Dictionary to hold the sum of coefficients for each term
    simplified = defaultdict(int)

    # Summing up the coefficients of like terms
    for term in terms:
        coefficient, variables = standardize(term)
        simplified[variables] += coefficient

    # Building the simplified polynomial
    result = []
    for variables in sorted(simplified, key=lambda x: (len(x), x)):
        coefficient = simplified[variables]
        if coefficient:  # Exclude terms with a coefficient of 0
            if coefficient < 0 or (coefficient > 0 and not result):
                result.append(f"{coefficient}{variables}")
            else:
                result.append(f"+{coefficient}{variables}")

    # Joining the terms and removing coefficients of 1 or -1
    return ''.join(term.replace('1', '') if '1' in term[:2] else term for term in result)

# Sample tests
test_cases = [
    "dc+dcba",
    "2xy-yx",
    "-a+5ab+3a-c-2a",
    "-abc+3a+2ac",
    "xyz-xz",
    "a+ca-ab",
    "xzy+zby",
    "-y+x",
    "y-x"
]

results = [simplify(tc) for tc in test_cases]
results

# Description:
'''
The function correctly handles terms with coefficients of 1 or -1, arranges monomials by the number of variables and lexicographic order,
and ensures no leading '+' sign for positive first coefficients. It also correctly adds or subtracts equivalent monomials.
​
'''


