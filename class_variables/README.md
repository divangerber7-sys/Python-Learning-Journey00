# Python Class Variables Lesson

## Overview
Class variables are shared among all instances of a class. They are defined outside the constructor and allow you to store data that is common to all objects created from that class.

### Key Points
- **Class Variable:** Shared across all instances (defined outside `__init__`).
- **Instance Variable:** Unique to each object (defined inside `__init__`).
- Class variables can be modified using the class name.
- Best practice: Access class variables via the class name for clarity.

### Example Usage
```python
class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
