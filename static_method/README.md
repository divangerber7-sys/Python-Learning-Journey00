# Lesson 58: Static Methods

## 🔑 Key Concepts
- **Instance Methods**
  - Defined with `self`.
  - Operate on **individual objects**.
  - Example: `get_info()`.

- **Static Methods**
  - Decorated with `@staticmethod`.
  - Do **not** need access to `self` or `cls`.
  - Used for **utility functions**.
  - Called on the **class itself**, not on instances.

---

## Example
```python
employee1 = Employee("Eugene", "Manager")
print(employee1.get_info())         # Instance method
print(Employee.is_valid_position("Manager"))  # Static method

EXAMPLE OUTPUT:
Eugene = Manager
True
False
