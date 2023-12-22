# Path Finder #1: can you reach the exit?

# Topic: ALGORITHMS.

'''
# Task:
--------
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked ..
Walls are marked W.
Start and exit positions are empty in all test cases.

Path Finder Series:
#1: can you reach the exit?
#2: shortest path
#3: the Alpinist
#4: where are you?
#5: there's someone here


# Sample Tesst:
---------------
from solution import path_finder
import codewars_test as test

@test.it('Example 1')
def _():
    maze = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])
    test.assert_equals(path_finder(maze), True, repr(maze))

@test.it('Example 2')
def _():
    maze = "\n".join([


# Code:
--------
def path_finder(maze):
    return True # can go to lower right corner from upper left one

'''
# Solution:
def path_finder(maze):
    # Convert maze string to a 2D list
    maze = maze.split('\n')
    n = len(maze)

    # Helper function to check if a cell is within bounds and open
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n and maze[x][y] == '.'

    # DFS to explore the maze
    def dfs(x, y):
        if not is_valid(x, y) or maze[x][y] == 'V':  # V for visited
            return False
        if x == y == n - 1:  # Reached the end
            return True

        maze[x] = maze[x][:y] + 'V' + maze[x][y + 1:]  # Mark as visited

        # Explore all four directions
        return (dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1))

    return dfs(0, 0)

# Test cases
test1 = "\n".join([".W.", ".W.", "..."])
test2 = "\n".join([".W.", ".W.", "W.."])

path_finder(test1), path_finder(test2)

# Descriptions:
'''
The path_finder function correctly determines whether it is possible to reach the exit in a given maze. 
The function returns True, indicating that it is possible to reach the exit.
The function returns False, indicating that it is not possible to reach the exit.

The function implements a depth-first search (DFS) algorithm to explore the maze and determine if a path exists from 
the start position [0, 0] to the exit position [N-1, N-1]. It correctly handles walls (marked with 'W') and
open spaces (marked with '.'). ​

'''

