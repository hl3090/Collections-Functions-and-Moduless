def check_range(num, dct):
    """Check if a number is in a given range using a dictionary"""
    return num in dct.values()

my_dict = {'best': 3, 'is': 2, 'gfg': 1}
print(check_range(1, my_dict))
print(check_range(5, my_dict))  