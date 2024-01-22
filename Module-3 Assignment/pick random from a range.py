"""
Q. How can you pick a random item from a range?
"""
import random

num = range(1,10)

random_num = random.randint(0,len(num))
print(random_num)