# MODULE = a file containing code you want to include in your programs
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate files

# ------------------------------
# Example 1: Explore built-in modules
# ------------------------------

# List of available modules (⚠️ will print A LOT!)
# print(help("modules"))

# List functions/variables inside the math module
# print(help("math"))

# Import the whole module
import math
print("Math PI:", math.pi)

# Alias a module (rename for convenience)
import math as m
print("Math PI (alias):", m.pi)

# Import only specific parts (⚠️ may cause naming conflicts)
from math import e
print("Math constant e:", e)

# Example of conflict:
a, b, c, d, e = 1, 2, 3, 4, 5
print("Here e is no longer the math constant, but reassigned:", e)

# Safer to always use math.e instead of from-import
print("Math constant e again (safe):", math.e)


# ------------------------------
# Example 2: Create your own module
# ------------------------------
# Step 1: Create a new file named `example.py` with this content:
"""
pi = 3.14159

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2
"""

# Step 2: Import your own module (make sure example.py is in the same folder)
# import example

# print("Square of 3:", example.square(3))
# print("Cube of 2:", example.cube(2))
# print("Circumference of r=5:", example.circumference(5))
# print("Area of r=5:", example.area(5))
