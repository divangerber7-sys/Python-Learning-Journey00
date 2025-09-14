# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      Syntax: [expression for value in iterable if condition]

# Example 1: Traditional loop vs list comprehension
doubles_loop = []
for x in range(1, 11):
    doubles_loop.append(x * 2)

doubles_comprehension = [x * 2 for x in range(1, 11)]

print("Doubles (loop):", doubles_loop)
print("Doubles (comprehension):", doubles_comprehension)

# Example 2: Multiple list comprehensions
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print("Triples:", triples)
print("Squares:", squares)

# Example 3: Strings with list comprehension
fruits = ["apple", "banana", "cherry"]
fruits_upper = [fruit.upper() for fruit in fruits]
fruits_chars = [fruit[0] for fruit in fruits]
print("Uppercase fruits:", fruits_upper)
print("First letters:", fruits_chars)

# Example 4: Conditions inside list comprehension
numbers = [1, -2, 3, -4, 5, -6, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print("Positive numbers:", positive_nums)
print("Negative numbers:", negative_nums)
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)

# Example 5: Practical use case – filter passing grades
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print("Passing grades:", passing_grades)
