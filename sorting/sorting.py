# Sorting in Python
# .sort() → list method (modifies the list in place)
# sorted() → built-in function (returns a new sorted iterable)

# ---------------- LISTS ----------------
fruits = ["apple", "banana", "orange", "coconut"]

fruits.sort()  # alphabetical
print("List sorted ascending:", fruits)

fruits.sort(reverse=True)  # reverse alphabetical
print("List sorted descending:", fruits)


# ---------------- TUPLES ----------------
fruits_tuple = ("apple", "banana", "orange", "coconut")

# tuples don’t have .sort(), so use sorted()
fruits_tuple_sorted = tuple(sorted(fruits_tuple))
print("Tuple sorted ascending:", fruits_tuple_sorted)

fruits_tuple_sorted = tuple(sorted(fruits_tuple, reverse=True))
print("Tuple sorted descending:", fruits_tuple_sorted)


# ---------------- DICTIONARIES ----------------
fruits_dict = {
    "apple": 72,
    "banana": 105,
    "orange": 73,
    "coconut": 354
}

# Sort by key
sorted_by_key = dict(sorted(fruits_dict.items()))
print("Dict sorted by key ascending:", sorted_by_key)

# Sort by key (descending)
sorted_by_key_desc = dict(sorted(fruits_dict.items(), key=lambda item: item[0], reverse=True))
print("Dict sorted by key descending:", sorted_by_key_desc)

# Sort by value
sorted_by_value = dict(sorted(fruits_dict.items(), key=lambda item: item[1]))
print("Dict sorted by value ascending:", sorted_by_value)

# Sort by value (descending)
sorted_by_value_desc = dict(sorted(fruits_dict.items(), key=lambda item: item[1], reverse=True))
print("Dict sorted by value descending:", sorted_by_value_desc)


# ---------------- OBJECTS ----------------
class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"Fruit({self.name}, {self.calories})"

fruits = [
    Fruit("banana", 105),
    Fruit("apple", 72),
    Fruit("orange", 73),
    Fruit("coconut", 354)
]

# Sort by name
print("Objects sorted by name:", sorted(fruits, key=lambda fruit: fruit.name))

# Sort by calories
print("Objects sorted by calories:", sorted(fruits, key=lambda fruit: fruit.calories))

# Sort by calories (descending)
print("Objects sorted by calories descending:", sorted(fruits, key=lambda fruit: fruit.calories, reverse=True))
