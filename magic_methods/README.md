# Lesson 60: Magic (Dunder) Methods

## 🔑 Key Concepts
Magic methods (double underscore, `__dunder__`) let you define how your objects behave
with built-in operations like printing, comparisons, addition, and membership tests.

---

## Example Methods Used
- `__init__` → object construction
- `__str__` → string representation (`print(obj)`)
- `__eq__` → equality check (`==`)
- `__lt__`, `__gt__` → comparisons (`<`, `>`)
- `__add__` → addition with `+`
- `__contains__` → membership (`in`)
- `__getitem__` → key-style access (`obj["title"]`)

---

## Example
```python
book1 = Book("The Way of Zen", "Alan Watts", 256)
book2 = Book("The Wisdom of Insecurity", "Alan Watts", 160)

print(book1)             # The Way of Zen by Alan Watts
print(book1 == book2)    # False
print(book1 > book2)     # True
print(book1 + book2)     # 416
print("zen" in book1)    # True
print(book1["title"])    # The Way of Zen


EXAMPLE OUTPUT:
The Way of Zen by Alan Watts
False
True
416
True
The Way of Zen

