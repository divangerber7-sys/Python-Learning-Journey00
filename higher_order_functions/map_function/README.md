# Lesson 64: Higher-Order Functions – `map()`

## 🔑 Key Concepts
- `map(function, collection)` applies a function to **every item** in a collection.
- Returns a **map object** (an iterator) → often converted to a `list`.

---

## Example 1 – Using a Named Function
```python
def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temp = [0.0, 10.0, 20.0]
fahrenheit_temp = list(map(c_to_f, celsius_temp))
print(fahrenheit_temp)  # [32.0, 50.0, 68.0]


EXAMPLE OUTPUT:
celsius_temp = [0.0, 10.0, 20.0]
fahrenheit_temp = list(map(lambda t: (t * 9/5) + 32, celsius_temp))
print(fahrenheit_temp)  # [32.0, 50.0, 68.0]


