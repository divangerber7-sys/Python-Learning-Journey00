# Python Inheritance Lesson

## Overview
Inheritance allows a class (child) to acquire attributes and methods from another class (parent). This helps reduce code duplication and improves maintainability.

### Key Points
- **Parent Class:** The class whose attributes and methods are inherited.
- **Child Class:** The class that inherits from the parent.
- **Syntax:** `class Child(Parent):`
- Child classes can add new methods or override parent methods.

### Example Usage
```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating food")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof Woof!!!")

EXAMPLE OUTPUT
Loki
True
Loki is eating food
Loki is sleeping
Woof Woof!!!

Siff
True
Siff is eating food
Siff is sleeping
I rule the world!!!

Brain
True
Brain is eating food
Brain is sleeping
What are we gonna do today??
