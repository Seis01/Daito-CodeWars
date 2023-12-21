# Rot13

## Topic: CIPHERS, FUNDAMENTALS.

'''
# Task:
-------
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be 
returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

# Sample Tests:
---------------
from solution import rot13

@test.describe("Fixed tests")
def tests():
        
    @test.it("Should obtain correct Rot13 encoding on fixed strings")
    def test_rot13_fixed_strings():
        test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')

# Code:
-------
def rot13(message):
    pass
    
'''
# Solution
def rot13(message):
    result = []  # Initialize an empty list to store the rotated characters

    for char in message:
        if 'a' <= char <= 'z':
            # Rotate lowercase letters
            result.append(chr(((ord(char) - ord('a') + 13) % 26) + ord('a')))
        elif 'A' <= char <= 'Z':
            # Rotate uppercase letters
            result.append(chr(((ord(char) - ord('A') + 13) % 26) + ord('A')))
        else:
            # Keep non-alphabet characters unchanged
            result.append(char)

    return ''.join(result)  # Convert the list of characters back to a string and return

# Testcase:
print(rot13('test'))  # 'grfg'
print(rot13('Test'))  # 'Grfg'
print(rot13('aA bB zZ 1234 *!?%'))  # 'nN oO mM 1234 *!?%'

# Description:
'''
To implement the ROT13 cipher, let's create a function that iterates over each character in the input string. For each character, check whether 
it is a letter of the Latin/English alphabet (uppercase or lowercase). If so, let's perform the ROT13 transformation, which involves moving the 
letter 13 positions forward in the alphabet, while taking care of the transfer at the end of the alphabet. If the symbol is not a letter, leave 
it unchanged.

'''

