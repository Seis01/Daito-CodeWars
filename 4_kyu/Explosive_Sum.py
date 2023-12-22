# Explosive Sum.

# Topic:

'''
# Task:
-------
How many ways can you make the sum of a number?
From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)

In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. 
Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be 
partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1


Examples:

Basic
exp_sum(1) # 1
exp_sum(2) # 2  -> 1+1 , 2
exp_sum(3) # 3 -> 1+1+1, 1+2, 3
exp_sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
exp_sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3

exp_sum(10) # 42

Explosive
exp_sum(50) # 204226
exp_sum(80) # 15796476
exp_sum(100) # 190569292


See here for more examples: https://www.numericana.com/data/partition.htm



# Sample Tests:
----------------
import codewars_test as test
from solution import exp_sum

@test.describe('testing exp_sum')
def desc1():
    @test.it('Very basic tests')
    def it1():
        test.assert_equals(exp_sum(1), 1)
        test.assert_equals(exp_sum(2), 2)
        test.assert_equals(exp_sum(3), 3)
    @test.it('Funcionality tests')
    def it2():
        test.assert_equals(exp_sum(4), 5)
        test.assert_equals(exp_sum(5), 7)
        test.assert_equals(exp_sum(10), 42)


# Code:
--------
def exp_sum(n):
    #your code here

'''
# Solution:
def exp_sum(n):
    # Table to store the number of partitions for each number up to n
    partition_table = [0] * (n + 1)
    partition_table[0] = 1  # Base case

    # Fill the partition table
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partition_table[j] += partition_table[j - i]

    return partition_table[n]

# Test cases
test_cases = [1, 2, 3, 4, 5, 10]
results = [exp_sum(tc) for tc in test_cases]
results


# Description:
'''
The exp_sum function successfully calculates the number of ways to partition a number into the sum of positive integers. 
The function uses a dynamic programming approach to efficiently compute the number of partitions for each number up to n. 
This method ensures accurate and fast computation even for larger values of n. 

'''
