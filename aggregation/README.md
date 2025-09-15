# Lesson 55: Aggregation

## What is Aggregation?
Aggregation is a type of **object relationship** where:
- One object (the *whole*) contains references to other independent objects (the *parts*).
- The *parts* can exist without the *whole*.

---

## Example
```python
library = Library("The Alone Times")

book1 = Book("The Way of Zen", "Alan Watts")
book2 = Book("The Wisdom of Insecurity", "Alan Watts")
book3 = Book("The Spirit of Zen", "Alan Watts")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)
for book in library.list_books():
    print(book)

EXAMPLE OUTPUT:
The Alone Times
The Way of Zen by Alan Watts
The Wisdom of Insecurity by Alan Watts
The Spirit of Zen by Alan Watts
