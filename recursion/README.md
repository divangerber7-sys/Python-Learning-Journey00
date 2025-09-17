# Lesson 68: Recursion in Python

## What is Recursion?
A recursive function is a function that calls itself until a base condition is met.  
It helps to simplify problems by breaking them into smaller steps.

### ⚡ Key Notes
- **Iterative** (loop-based) → faster, efficient, but more complex to write.  
- **Recursive** (self-calling) → simpler, easier to visualize, but slower and memory-heavy.  
- Recursion uses the **call stack**, and if it goes too deep, you may hit a `RecursionError`.

---

## Example 1: Walking

### Iterative
```python
def walk_iterative(steps):
    for step in range(1, steps + 1):
        print(f"You have taken step number {step}")

walk_iterative(5)


Recursive:

def walk_recursive(steps):
    if steps == 0:  # base case
        return
    walk_recursive(steps - 1)  # recursive call
    print(f"You have taken step number {steps}")
walk_recursive(5)


Factorial Iterative:

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # 120


Factorial Recursive:

def factorial_recursive(n):
    if n == 1:  # base case
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # 120




