# Lesson 66: Higher-Order Functions – `reduce()`

## 🔑 Key Concepts
- `reduce(function, collection)` applies a function cumulatively to reduce a sequence to a **single value**.
- Often replaced with a simple loop, but useful in **functional programming**.

---

## Example 1 – Using a Named Function
```python
from functools import reduce

def add(x, y):
    return x + y

prices = [19.99, 1.00, 5.75, 12.99, 10.99]
total = reduce(add, prices)
print(f"R{total:.2f}")  # R50.72

USING LAMBDA FUNCTION EXAMPLE:

from functools import reduce

prices = [19.99, 1.00, 5.75, 12.99, 10.99]
total = reduce(lambda x, y: x + y, prices)
print(f"R{total:.2f}")  # R50.72
