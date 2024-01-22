"""
Q. Write a Python program to read a random line from a file.
"""

import random

with open('file1.txt', 'r') as f:
    lines = f.readlines()   # Get the lines of the file as a list.

# Pick random line from the list
random_line = random.choice(lines)
print(random_line)