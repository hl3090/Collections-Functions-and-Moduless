"""
Q. How can you get a random number in python?
Ans.
    We can get a random number in python by using function called 'random.randint()' in python.
"""

# # Example of Pick random number 
# import random

# number = random.randint(1,10)
# print(number)


# Import the random module.
import random

# Define a sample list.
sample_list = [1, 2, 3, 4, 5]

# Print the original list.
print(f"The original list is: {sample_list}")

# Randomize the items of the list in place.
random.shuffle(sample_list)

# Print the randomized list.
print(f"The randomized list is: {sample_list}")