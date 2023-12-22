# Closest pair of points in linearithmic time
# Topic

'''
# Task:
-------
DESCRIPTION:
Given a number of points on a plane, your task is to find two points with the smallest distance between them in linearithmic O(n log n) time.

Example
  1  2  3  4  5  6  7  8  9
1  
2    . A
3                . D
4                   . F       
5             . C
6              
7                . E
8    . B
9                   . G
For the plane above, the input will be:

(
  (2,2), # A
  (2,8), # B
  (5,5), # C
  (6,3), # D
  (6,7), # E
  (7,4), # F
  (7,9)  # G
)
=> closest pair is: ((6,3),(7,4)) or ((7,4),(6,3))
(both answers are valid. You can return a list of tuples too)
The two points that are closest to each other are D and F.
Expected answer should be an array with both points in any order.

Goal
The goal is to come up with a function that can find two closest points for any arbitrary array of points, in a linearithmic time.

Note: Don't use math.hypot, it's too slow...

# Sample Tests:
----------------
def verify(points, expected):
    
    actual = closest_pair(points)
    if not actual or len(actual) != 2 or not all(pt and isinstance(pt,tuple) and len(pt)==2 for pt in actual):
        test.fail(f"Output should be a tuple or list of tuples: ((a,b), (x,y)), but got {actual}")
    else:
        exp,act = (sorted(stuff) for stuff in (expected, actual))
        test.assert_equals(act,exp)



@test.describe("Fixed tests")
def fixed():
    
    @test.it("Example of the description")
    def it1():
        points = (
            (2, 2), # A
            (2, 8), # B
            (5, 5), # C
            (6, 3), # D
            (6, 7), # E
            (7, 4), # F
            (7, 9)  # G
        )
        expected = ((6, 3), (7, 4))
        verify(points, expected)
    
    
    @test.it("Two points")
    def it1():
        points   = ((2, 2), (6, 3))
        expected = points
        verify(points, expected)
    
    
    @test.it("Duplicated points")
    def it1():
        points =(
                (2, 2), # A
                (2, 8), # B
                (5, 5), # C
                (5, 5), # C
                (6, 3), # D
                (6, 7), # E
                (7, 4), # F
                (7, 9)  # G
        )
        expected =((5, 5), (5, 5))
        verify(points, expected)
        


# Code:
-------
 def closest_pair(points):
    # Your code here!
    pass


'''
# Solution
def closest_pair(points):
    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def closest_split_pair(px, py, delta, best_pair):
        ln_x = len(px)
        mx_x = px[ln_x // 2][0]

        # Sy contains points within delta of the dividing line
        sy = [p for p in py if mx_x - delta <= p[0] <= mx_x + delta]

        best = delta
        ln_y = len(sy)
        for i in range(ln_y - 1):
            for j in range(i + 1, min(i + 7, ln_y)):
                p, q = sy[i], sy[j]
                dst = distance(p, q)
                if dst < best:
                    best_pair = p, q
                    best = dst
        return best_pair

    def closest_pair_rec(px, py):
        if len(px) <= 3:
            return min([(px[i], px[j]) for i in range(len(px)) for j in range(i + 1, len(px))], key=lambda pair: distance(*pair))

        mid = len(px) // 2
        Qx, Rx = px[:mid], px[mid:]
        midpoint = px[mid][0]
        Qy, Ry = [p for p in py if p[0] <= midpoint], [p for p in py if p[0] > midpoint]

        (p1, q1) = closest_pair_rec(Qx, Qy)
        (p2, q2) = closest_pair_rec(Rx, Ry)

        best_pair = min((p1, q1), (p2, q2), key=lambda pair: distance(*pair))
        return closest_split_pair(px, py, distance(*best_pair), best_pair)

    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(px, py)

# Testing the function with the provided test cases
def verify(points, expected):
    actual = closest_pair(points)
    if not actual or len(actual) != 2 or not all(pt and isinstance(pt, tuple) and len(pt) == 2 for pt in actual):
        print(f"Output should be a tuple or list of tuples: ((a,b), (x,y)), but got {actual}")
    else:
        exp, act = (sorted(stuff) for stuff in (expected, actual))
        assert act == exp, f"Expected {exp}, but got {act}"
        print(f"Test passed. Closest pair: {act}")

# Test cases
verify(((2, 2), (2, 8), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)), ((6, 3), (7, 4)))
verify(((2, 2), (6, 3)), ((2, 2), (6, 3)))
verify(((2, 2), (2, 8), (5, 5), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)), ((5, 5), (5, 5)))

# Description:
'''
I use the divide and conquer approach, which is a common method of achieving O(n log n) time complexity.
The algorithm involves the following steps:
1. Sort the Points: First, sort the points based on their x-coordinates. This step takes O(n log n) time.
2. Divide: Divide the set of points into two halves.
3. Conquer: Recursively find the closest pair in each half.
4. Combine: Find the closest pair where one point is in the left half and the other is in the right half. This step requires careful handling to maintain the O(n log n) complexity.
5. Return the Closest Pair: Among the pairs found in steps 3 and 4, return the one with the smallest distance.

The way to determine the nearest pair, at the stage when we combine the results from the split halves: The algorithm must effectively process the strip in the middle (where the 
points are close to the dividing line) to ensure that it does not miss any potentially closest pairs.
My implementation includes an optimized closest_split_pair function that checks only the points in the strip near the dividing line, considering at most 7 points ahead
as per the closest pair problem's geometric properties. This ensures the algorithm maintains O(n log n) complexity.

'''

