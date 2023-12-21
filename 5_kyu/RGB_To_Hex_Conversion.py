# RGB To Hex Conversion

# Topic: ALGORITHMS

'''
# Task:
--------
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

# Sample Tests:
----------------
import codewars_test as test
from solution import rgb


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Tests")
    def _():
        test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
        test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
        test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
        test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
        test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")

# Code:
--------
def rgb(r, g, b):
    # your code here :)
    pass

'''
# Solution:
def rgb(r, g, b):
    # Clamp the values to the range [0, 255]
    r = min(255, max(0, r))
    g = min(255, max(0, g))
    b = min(255, max(0, b))

    # Convert the decimal values to hexadecimal and format them as a 6-character string
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

# Test cases:
print(rgb(0, 0, 0))     # "000000"
print(rgb(1, 2, 3))     # "010203"
print(rgb(255, 255, 255)) # "FFFFFF"
print(rgb(254, 253, 252)) # "FEFDFC"
print(rgb(-20, 275, 125)) # "00FF7D"


# Description:
''' 
To solve this problem, you can create a function called rgb that takes three integer arguments r, g, and b, 
which represent the red, green, and blue components of an RGB color, respectively. The function should return 
the hexadecimal representation of the RGB color.

In this code, we first clamp the values r, g, and b to the range [0, 255] to ensure they are valid RGB values. 
Then, we use the format method to convert these values to hexadecimal and format them as a 6-character string 
with leading zeros if needed.

Now, you can use this rgb function to convert RGB values to hexadecimal representation.
'''
