"""
Q. Write a Python script to merge two Python dictionaries
"""

software = {
    "python" : "django",
    "php"   : "laravel"
}
designing = {
    "GD"  : "Graphic design",
    "WD"  : "Website design"
}

# New dictionary
d3 ={}

# join two dictionaries
for i in (software,designing):
    d3.update(i)
    
print(d3)    