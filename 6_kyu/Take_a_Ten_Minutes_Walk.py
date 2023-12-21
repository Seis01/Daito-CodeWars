# Take a Ten Minutes Walk.

## Topic: ARRAYS, FUNDAMENTALS.

'''
# Task:
-------
You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go 
for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing 
directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so 
create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your 
starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty 
array (that's not a walk, that's standing still!).


# Sample Tests:
---------------
import codewars_test as test

@test.describe('Walk Validator - fixed tests')
def sample_tests():
    @test.it ("should return true for a valid walk")
    def _():
        test.assert_equals(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), True, 'should return True');
    @test.it ("should return false if walk is too long")
    def _():
        test.assert_equals(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), False, 'should return False');
    @test.it ("should return false if walk is too short")
    def _():
        test.assert_equals(is_valid_walk(['w']), False, 'should return False');
    @test.it ("should return false if walk does not bring you back to start")
    def _():        
        test.assert_equals(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), False, 'should return False');

# Code:
--------
def is_valid_walk(walk):
    #determine if walk is valid
    pass


'''
# Solution:
def is_valid_walk(walk):
    # Check if the walk takes exactly ten minutes
    if len(walk) != 10:
        return False

    # Count the number of steps in each direction
    north = walk.count('n')
    south = walk.count('s')
    east = walk.count('e')
    west = walk.count('w')

    # Check if the number of steps north is equal to the number of steps south
    # and the number of steps east is equal to the number of steps west
    return north == south and east == west

print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))  # True
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))  # False
print(is_valid_walk(['w']))  # False
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))  # False


# Description:
'''
To determine if a walk is valid, you can check whether it takes exactly ten minutes and whether it returns to the starting 
point (i.e., the number of steps to the north 'n' should be equal to the number of steps to the south 's', and the number 
of steps to the east 'e' should be equal to the number of steps to the west 'w').
Now can use this function to check if a walk is valid. It returns True if the walk is valid (takes ten minutes and returns 
to the starting point) and False otherwise.
'''
