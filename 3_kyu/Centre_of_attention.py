# Centre of attention

# Topic:

'''
# Task:
-------
For this kata, we're given an image in which some object of interest (e.g. a face, or a license plate, or an aircraft) appears as a large block of contiguous pixels all of the same colour. 
(Probably some image-processing has already occurred to achieve this, but we needn't worry about that.) We want to find the centre of the object in the image.

We'll do this by finding which pixels of the given colour have maximum depth. The depth of a pixel P is the minimum number of steps (up, down, left, or right) you have to take from P to 
reach either a pixel of a different colour or the edge of the image.

/pixel depths pic/

In the picture, the red pixel marked "3" has a depth of 3: it takes at least 3 steps from there to reach something other than another red pixel. Note that the steps need not be all in 
the same direction. Only one red pixel has depth 3: the one right in the middle of the red region. Similarly, the blue pixel marked "2" has a depth of 2 (but it is not the only one with 
this depth). The green and purple pixels all have depth 1.

The pixels of a given colour with the largest depth will be found at the centre of the biggest solid region(s) of that colour. Those are the ones we want.

The function you'll write (central_pixels) belongs to the following data structure:

class Image:
  def __init__(self, data, w, h): 
    self.pixels = data
    self.width = w
    self.height = h
    
The image data consists of a one-dimensional array pixels of unsigned integers (or just integers, in languages that don't have unsigned integers as such), which correspond to pixels in 
row-by-row order. (That is, the top row of pixels comes first, from left to right, then the second row, and so on, with the pixel in the bottom right corner last of all.) The values of 
the pixels array elements represent colours via some one-to-one mapping whose details need not concern us.

The central_pixels function should find and return all the positions (pixels array indices) of the pixels having the greatest depth among all pixels of colour colour).

Note 1. The final test in the suite (Big_Test) is a 16-megapixel image (1 megapixel in the Python version), so you will need to consider the time and space requirements of your solution 
        for images up to that size.

Note 2. The order of pixel positions in the returned array is not important; sort them however you like.

Hint. It is possible to get this done in two passes through the pixel data.



# Sample Tests:
---------------
import codewars_test as test
from solution import Central_Pixels_Finder
from preloaded import Image

@test.describe("central_pixels tests")
def _():

    @test.it("Example_Tests")
    def _():
        image = Central_Pixels_Finder( [1,1,4,4,4,4,2,2,2,2,
                                        1,1,1,1,2,2,2,2,2,2,
                                        1,1,1,1,2,2,2,2,2,2,
                                        1,1,1,1,1,3,2,2,2,2,
                                        1,1,1,1,1,3,3,3,2,2,
                                        1,1,1,1,1,1,3,3,3,3], 10, 6 );

        # Only one red pixel has the maximum depth of 3:
        red_ctr = [ 32 ];
        test.assert_equals(image.central_pixels(1), red_ctr)

        # Multiple blue pixels have the maximum depth of 2:
        blue_ctr = [ 16,17,18,26,27,28,38 ];
        test.assert_equals(sorted(image.central_pixels(2)), blue_ctr)

        # All the green pixels have depth 1, so they are all "central":
        green_ctr = [ 35,45,46,47,56,57,58,59 ];
        test.assert_equals(sorted(image.central_pixels(3)), green_ctr)

        # Similarly, all the purple pixels have depth 1:
        purple_ctr = [ 2,3,4,5 ];
        test.assert_equals(sorted(image.central_pixels(4)), purple_ctr)

        # There are no pixels with colour 5:
        non_existent_ctr = [ ];
        test.assert_equals(image.central_pixels(5), non_existent_ctr)

        # Changing one pixel can make a big difference to the result:
        image.pixels[32] = 3;
        test.assert_equals(sorted(image.central_pixels(1)), [ 11,21,41,43 ])


# Code:
-------
class Central_Pixels_Finder(Image):

  def central_pixels(self, colour):
  # your code goes here

'''
# Solution:

from collections import deque

class Central_Pixels_Finder(Image):

    def central_pixels(self, colour):
        # Initialize a matrix to store the depth of each pixel.
        # The maximum possible depth is set to the sum of the image's width and height.
        max_depth = self.width + self.height
        depth_matrix = [[max_depth for _ in range(self.width)] for _ in range(self.height)]

        # Queue for BFS (Breadth-First Search).
        queue = deque()

        # Initialize the queue with edge pixels and pixels adjacent to different colors.
        for y in range(self.height):
            for x in range(self.width):
                if self.pixels[y * self.width + x] == colour:
                    # Check if the pixel is on the edge or adjacent to a different color.
                    is_edge_or_adjacent = x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1
                    if not is_edge_or_adjacent:
                        # Check all four directions (up, down, left, right) for different colors.
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height and self.pixels[ny * self.width + nx] != colour:
                                is_edge_or_adjacent = True
                                break
                    # If the pixel is on the edge or adjacent to a different color, set its depth to 1 and add to the queue.
                    if is_edge_or_adjacent:
                        depth_matrix[y][x] = 1
                        queue.append((x, y))
                    else:
                        # Otherwise, set the depth to the maximum possible depth.
                        depth_matrix[y][x] = max_depth

        # Perform BFS to calculate the depth of each pixel.
        while queue:
            x, y = queue.popleft()

            # Check all four directions (up, down, left, right) for pixels of the same color.
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.pixels[ny * self.width + nx] == colour:
                    new_depth = depth_matrix[y][x] + 1
                    # Update the depth if the new depth is smaller.
                    if depth_matrix[ny][nx] > new_depth:
                        depth_matrix[ny][nx] = new_depth
                        queue.append((nx, ny))

        # Check if there are any pixels of the given color in the image.
        if not any(self.pixels[y * self.width + x] == colour for y in range(self.height) for x in range(self.width)):
            return []

        # Find the maximum depth among pixels of the given color.
        max_depth = max(depth_matrix[y][x] for y in range(self.height) for x in range(self.width) if self.pixels[y * self.width + x] == colour)

        # Find all pixels with the maximum depth.
        central_pixels = [y * self.width + x for y in range(self.height) for x in range(self.width) if depth_matrix[y][x] == max_depth]

        return central_pixels




