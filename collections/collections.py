#   collection = single "variable" used to store multiple values
#   List    = [] ordered and changeable. Duplicates OK
#   Set     = {} unordered and mutable. No Duplicates
#   Tuple   = () ordered and unchangeable. Duplicates OK. FASTER

# LIST EXAMPLES
#fruits = ["apple", "banana", "orange", "strawberry", "kiwi"]

# Examples of list methods:
# fruits.append("grapefruits")
# fruits.remove("orange")
# fruits.insert(3, "tomato")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("banana"))
# print(fruits.count("banana"))

# SET EXAMPLES
#fruits_set = {"apple", "banana", "orange", "strawberry", "kiwi"}
#fruits_set.add("peppers")
#fruits_set.remove("banana")
#fruits_set.pop()
#fruits_set.clear()

# TUPLE EXAMPLES
fruits = ("apple", "banana", "orange", "strawberry", "kiwi")

# Iterate over tuple
for fruit in fruits:
    print(fruit)
