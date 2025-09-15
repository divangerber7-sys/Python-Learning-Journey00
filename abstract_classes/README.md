# Lesson 51: Abstract Classes

## What is an Abstract Class?
- An **abstract class** cannot be instantiated directly.
- It serves as a **blueprint** for other classes.
- Declared using the `abc` (Abstract Base Class) module.
- Enforces that all child classes implement required abstract methods.

## Benefits
1. Prevents instantiation of the base class.
2. Enforces consistency across subclasses.

## Example
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
OUTPUT EXAMPLE:
Your vehicle is moving
Your vehicle is stopped

Your Ducati is moving
Your Ducati is stopped

You are sailing the oceans
A port is no place for a boat
