# Lesson 67: Sorting in Python

Python provides two main ways to sort:
- `.sort()` → List **method**, modifies the list **in place**
- `sorted()` → Built-in **function**, returns a new sorted iterable

---

## 1. Sorting Lists
```python
fruits = ["apple", "banana", "orange", "coconut"]

fruits.sort()  # modifies the list
print(fruits)  # ['apple', 'banana', 'coconut', 'orange']

fruits.sort(reverse=True)
print(fruits)  # ['orange', 'coconut', 'banana', 'apple']

Sorting Tuples:

fruits = ("apple", "banana", "orange", "coconut")

fruits = tuple(sorted(fruits, reverse=True))
print(fruits)  # ('orange', 'coconut', 'banana', 'apple')

Sorting Dictionaries:

fruits = {"apple": 72, "banana": 105, "orange": 73, "coconut": 354}

# by key
dict(sorted(fruits.items()))

# by value
dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))

Sorting Objects:

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"Fruit({self.name}, {self.calories})"

fruits = [Fruit("banana", 105), Fruit("apple", 72), Fruit("coconut", 354)]

sorted(fruits, key=lambda f: f.calories)        # by calories
sorted(fruits, key=lambda f: f.calories, reverse=True)  # descending

