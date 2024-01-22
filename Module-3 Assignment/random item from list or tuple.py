"""
Q. How can you pick a random item from a list or tuple?

"""

import random
# pick random item from list
l1 = [1,2,3,4,5]
num = random.choice(l1)
print(num)


# pick random item from tuple
t = ('car','bike','train','airplane')
vehicles = random.choice(t)
print(vehicles)
