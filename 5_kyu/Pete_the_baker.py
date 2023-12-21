# Pete, the baker.

## Topic: ALGORITHMS.

'''
# Task:
--------
Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and returns the maximum number of cakes Pete can bake (integer). For simplicity there 
are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.

Examples:
# must return 2
cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# must return 0
cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

# Sample Tests:
---------------
import codewars_test as test
from solution import cakes

@test.it('Testing Pete, the Baker')
def _():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    test.assert_equals(cakes(recipe, available), 2, 'example #1')

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    test.assert_equals(cakes(recipe, available), 0, 'example #2')

# Code:
-------
def cakes(recipe, available):
    return 5

'''
# Solution:
def cakes(recipe, available):
    # Initialize a list to store the maximum number of cakes for each ingredient
    max_cakes = []

    # Iterate through each ingredient in the recipe
    for ingredient, quantity in recipe.items():
        # Check if the ingredient exists in the available ingredients
        if ingredient in available:
            # Calculate the maximum number of cakes for this ingredient
            max_cakes.append(available[ingredient] // quantity)
        else:
            # If the ingredient is not available, return 0 cakes
            return 0

    # Return the minimum of the maximums as the result
    return min(max_cakes)

# Tsetcase:
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))  # 2
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}))  # 0

# Description:
'''
To solve this problem, we need to calculate how many cakes can be made using the available ingredients and the recipe. The idea is 
to iterate through each ingredient in the recipe, check if it exists in the available ingredients, and calculate the maximum number 
of cakes that can be made for each ingredient. The minimum of these maximums will be the maximum number of cakes that can be made.
Now, we can use this function to calculate the maximum number of cakes Pete can bake given the recipe and available ingredients. 
It returns the integer representing the maximum number of cakes.

'''
