"""
Q. Write a Python program to split a list into different variables.

"""

# List with elements
list_to_split = [1, 2, 3, 4, 5]

# Splitting the list
first_var, second_var, third_var, fourth_var, fifth_var = list_to_split[:1], list_to_split[1:2], list_to_split[2:3], list_to_split[3:4], list_to_split[4:]

print(first_var)
print(second_var)
print(third_var)
print(fourth_var)
print(fifth_var)