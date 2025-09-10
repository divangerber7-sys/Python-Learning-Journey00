# Lesson 05 - If Statements

In this lesson, I learned how to use **conditional statements** in Python.  
Conditionals allow a program to make decisions and execute different code depending on whether a condition is **True** or **False**.  

---

## Key Concepts Learned
- `if` = run code if a condition is `True`
- `elif` = test another condition if the first one was `False`
- `else` = run code if none of the conditions are `True`
- Boolean conditions can be used directly (`True`/`False`)

---

## Code Examples

```python
# Check age
"""
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are old enough")
elif age < 0:
    print("You haven't been born yet!!!")
else:
    print("You are NOT old enough")
"""

# Check if name is empty
"""
name = input("Please enter your name:")

if name == "":
    print("You didn't enter your name")
else:
    print(f"Your name is {name}")
"""

# Simple boolean check
online = False

if online:
    print("The user is online!!")
else:
    print("The user is offline!!")
