# The Millionth Fibonacci Kata
# Topic: MATHEMATICS, ALGORITHMS.

'''
# Task:
-------
The year is 1214. One night, Pope Innocent III awakens to find the the archangel Gabriel floating before him. Gabriel thunders to the pope:

Gather all of the learned men in Pisa, especially Leonardo Fibonacci. In order for the crusades in the holy lands to be successful, these men must calculate the millionth number in Fibonacci's recurrence. Fail to do this, and your armies will never reclaim the holy land. It is His will.

The angel then vanishes in an explosion of white light.

Pope Innocent III sits in his bed in awe. How much is a million? he thinks to himself. He never was very good at math.

He tries writing the number down, but because everyone in Europe is still using Roman numerals at this moment in history, he cannot represent this number. If he only knew about the invention of zero, it might make this sort of thing easier.

He decides to go back to bed. He consoles himself, The Lord would never challenge me thus; this must have been some deceit by the devil. A pretty horrendous nightmare, to be sure.

Pope Innocent III's armies would go on to conquer Constantinople (now Istanbul), but they would never reclaim the holy land as he desired.

In this kata you will have to calculate fib(n) where:

fib(0) := 0
fib(1) := 1
fib(n + 2) := fib(n + 1) + fib(n)
Write an algorithm that can handle n up to 2000000.

Your algorithm must output the exact integer answer, to full precision. Also, it must correctly handle negative numbers as input.

HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason what value fib has to have for negative values.

HINT II: See https://web.archive.org/web/20220614001843/https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.4

# Sample Tests:
----------------
import codewars_test as test

@test.describe("Small positive numbers")
def small_positive_numbers():
    
    for n, result in [(0,0), (1,1), (2,1), (3,2), (4,3), (5,5)]:
        @test.it(f"fib({n}) == {result}")
        def _():        
            test.assert_equals(fib(n), result)

        
@test.describe("Small negative numbers")
def small_negative_numbers():
    
    @test.it("fib(-1) == 1")
    def _():
        test.assert_equals(fib(-1), 1)
    
    @test.it("fib(-6) == -8")
    def _():
        test.assert_equals(fib(-6), -8)
        
    @test.it("fib(-96) == -51680708854858323072")
    def _():
        test.assert_equals(fib(-96), -51680708854858323072)
        
@test.describe("Large Numbers")
def large_numbers():
    
    @test.it("fib(-500)")
    def _():
        test.assert_equals(
            fib(-500),
            -139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
        )
    
    @test.it("fib(1000)")
    def _():
        test.assert_equals(
            fib(1000),
            43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        )                                         


# Code:
--------
def fib(n):
    """Calculates the nth Fibonacci number"""
    pass

'''
# Solution:
def fib(n):
    """Calculates the nth Fibonacci number"""
    if n == 0:
        return 0
    elif n < 0:
        n = -n
        if n % 2 == 0:
            sign = -1
        else:
            sign = 1
    else:
        sign = 1

    def matrix_multiply(A, B):
        return [
            [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]
        ]

    def matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power % 2 == 0:
            return matrix_power(matrix_multiply(matrix, matrix), power // 2)
        else:
            return matrix_multiply(matrix, matrix_power(matrix_multiply(matrix, matrix), (power - 1) // 2))

    result_matrix = matrix_power([[1, 1], [1, 0]], n)
    return sign * result_matrix[0][1]

# Test cases
print(fib(0))  # 0
print(fib(1))  # 1
print(fib(5))  # 5
print(fib(-6))  # -8
print(fib(1000))  # Large positive number
print(fib(-500))  # Large negative number


# Description:
'''
To solve this problem efficiently, especially for very large values of n, we need to use matrix exponentiation. 
This method leverages the fact that Fibonacci numbers can be represented as a result of exponentiating a specific 2x2 matrix. 
The matrix exponentiation can be done in logarithmic time, which makes it suitable for large n.

The key matrix for Fibonacci numbers is:

| 1 1 |
| 1 0 |

When this matrix is raised to the power n, the top left element of the resulting matrix is fib(n).

For negative values of n, we can use the formula:
fib(-n) = (-1)^(n+1) * fib(n)

My implementation should efficiently handle very large values of n, both positive and negative.

'''
