"""
Q. Write a Python program to combine values in python list of dictionaries.
"""

import collections

input_list = [
    {'item': 'item1', 'amount': 400}, 
    {'item': 'item2', 'amount': 300}, 
    {'item': 'item1', 'amount': 750}
]

counter = collections.Counter()

for item in input_list:
    counter[item['item']] += item['amount']
print(counter)