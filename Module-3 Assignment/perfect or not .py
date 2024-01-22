"""
Q. Write a Python function to check whether a number is perfect or not.
"""    
    
def check_perfect(n):
    
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
            
    return sum, n == sum 

n = int(input("Enter a number: "))
check_perfect(n)
factors_sum, is_perfect = check_perfect(n)

if is_perfect:
    print("Perfect number")
else:
    print("Not perfect number")    
           