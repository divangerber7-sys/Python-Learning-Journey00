# Lesson 09 - Logical Operators

In this lesson, I learned how to use **logical operators** in Python.  
Logical operators are used to combine or modify conditions inside `if` statements.

---

## Key Operators
- `and` → True if **both** conditions are true  
- `or` → True if **at least one** condition is true  
- `not` → Inverts the condition (True becomes False, False becomes True)

---

## Code Examples

```python
# Logical operators = used on conditional statements

# Example 1: using `and`
"""
temp = 25

if temp > 0 and temp < 30:
    print("This is a good temperature!!!")
else:
    print("This is a bad temperature!!!")
"""

# Example 2: using `or`
"""
temp = 40

if temp <= 0 or temp >= 30:
    print("This is a bad temperature!!!")
else:
    print("This is a good temperature!!!")
"""

# Example 3: using `not`
sunny = True

if not sunny:
    print("This is a sunny day!!!")
else:
    print("This is a cloudy day!!!")
