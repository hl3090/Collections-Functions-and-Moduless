"""
Q. Write a Python function to get the largest number, smallest num and sum of all from a list.

"""

def largest_smallest_sum(nums):
    largest = nums[0]
    smallest = nums[0]
    total_sum = 0

    for num in nums:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total_sum += num

    return largest, smallest, total_sum

numbers = [5,23,4,56,78,4,6,10]

# for i in range(1,6):
#    number = int(input("Enter a number: "))
#    numbers.append(number)

largest, smallest, sum_of_all = largest_smallest_sum(numbers)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {sum_of_all}")