"""
Q. Write a Python program to create and display all combinations of letters, selecting each letter from a 
   different key in a dictionary.
"""

d = {
    '1' : ['a','b'],
    '2' : ['c','d']
}

for k in d['1']:
    for v in d['2']:
        print(k+v)