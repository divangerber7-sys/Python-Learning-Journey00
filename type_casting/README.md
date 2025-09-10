Lesson 02 - Explicit Typecasting
In this lesson, I learned about explicit typecasting in Python, which means manually converting a variable from one type to another.

Python has several built-in data types:

String → Text values
Integer → Whole numbers
Float → Decimal numbers
Boolean → True/False
This lesson demonstrates how to convert a variable’s type explicitly using built-in functions like bool().

Code
# (string, integer, float, boolean)
# Explicit vs Implicit

# Explicit Typecasting - Manually converting to another

name = "Bro"
age = 21
gpa = 1.9
student = True

name = bool(name)
print(name)
