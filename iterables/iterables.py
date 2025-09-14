# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop.

# Example 1: Lists are iterable
numbers_list = [1, 2, 3, 4, 5]
print("List (reversed):")
for number in reversed(numbers_list):
    print(number, end=" ")
print("\n")

# Example 2: Tuples are iterable
numbers_tuple = (1, 2, 3, 4, 5)
print("Tuple:")
for number in numbers_tuple:
    print(number, end=" ")
print("\n")

# Example 3: Sets (not reversible, unordered)
fruits = {"apple", "orange", "banana", "coconut"}
print("Set:")
for fruit in fruits:
    print(fruit)
print()

# Example 4: Strings
name = "Spongebob Squarepants"
print("String:")
for character in name:
    print(character, end=" ")
print("\n")

# Example 5: Dictionaries
my_dictionary = {"A": 1, "B": 2, "C": 3, "D": 4}

print("Dictionary (keys):")
for key in my_dictionary:
    print(key)
print()

print("Dictionary (values):")
for value in my_dictionary.values():
    print(value)
print()

print("Dictionary (key-value pairs):")
for key, value in my_dictionary.items():
    print(f"{key} = {value}")
