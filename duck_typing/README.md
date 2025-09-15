# Lesson 54: Duck Typing

## What is Duck Typing?
Duck Typing is a form of **polymorphism** that doesn’t rely on inheritance.  
Instead, it checks whether an object has the **minimum required methods/attributes**.

🦆 “If it looks like a duck and quacks like a duck, it must be a duck.”

---

## Example
```python
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

EXAMPLE OUTPUT:
Woof Woof!!
Alive: True
I rule the world!!!
Alive: True
Honky Honky
Alive: False
