"""
Q. Write a Python program to print all unique values in a dictionary.
"""

d1 = {
    "python": "language",
    "django": "framework",
    "java"  : "language",
    "spring": "framework"
}
# add unique values in d2
d2 = set(d1.values())
for v in d2:
    print(v)