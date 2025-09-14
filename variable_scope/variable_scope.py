# variable scope = where a variable is visible and accessible
# scope resolution follows (LEGB): Local -> Enclosed -> Global -> Built-in

# ------------------------------
# Example 1: Local scope
# ------------------------------
def func1():
    a = 1
    print("func1 local a:", a)

def func2():
    b = 2
    print("func2 local b:", b)

func1()
func2()
# Note: a is not visible in func2, b is not visible in func1

# ------------------------------
# Example 2: Enclosed scope
# ------------------------------
def outer_function():
    x = 1  # enclosed variable

    def inner_function():
        x = 2  # local variable overrides enclosed
        print("Inner local x:", x)

    inner_function()

outer_function()

# If you remove the local `x = 2` in inner_function,
# Python will look in the enclosed scope instead.

def outer_function2():
    x = 1
    def inner_function():
        print("Inner sees enclosed x:", x)  # no local x here
    inner_function()

outer_function2()

# ------------------------------
# Example 3: Global scope
# ------------------------------
x = 3  # global variable

def func3():
    print("func3 sees global x:", x)

def func4():
    print("func4 sees global x:", x)

func3()
func4()

# ------------------------------
# Example 4: Built-in scope
# ------------------------------
from math import e  # built-in constant

def func5():
    print("Built-in math.e:", e)

e = 3  # global variable shadows built-in
func5()  # prints 3, because global overrides built-in

# LEGB order: Local → Enclosed → Global → Built-in
