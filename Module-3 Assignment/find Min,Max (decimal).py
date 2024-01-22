"""
Q.Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.
"""

# List of decimal numbers
l1 = [10.23,56.34,5.7,78.98,45.34]

# Initialize variables for minimum and maximum values
min_value = float('inf')
max_value = float('-inf')

for num in l1:
    min_value = min(min_value, num)   # Update the minimum and maximum values
    max_value = max(max_value, num)

print("Minimum Values: ",min_value)
print("Maximum values: ",max_value)