# Lesson 69: Exception Handling in Python

## What is an Exception?
An **exception** is an error that disrupts the normal flow of a program.  
Examples:  
- `ZeroDivisionError` → when dividing by zero  
- `ValueError` → invalid type (e.g., converting "abc" to int)  
- `TypeError` → operation on the wrong type  

---

## Basic Structure
```python
try:
    # Code that might cause an error
except SomeException:
    # Code that runs if error occurs
finally:
    # Code that always runs (cleanup, closing files, etc.)


Example: Division:

try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("❌ You can't divide by zero")
except ValueError:
    print("❌ You didn't enter a valid number")
except Exception as e:
    print(f"❌ Something went wrong: {e}")
finally:
    print("✅ Goodbye - this will always run")
