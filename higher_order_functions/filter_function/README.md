# Lesson 65: Higher-Order Functions – `filter()`

## 🔑 Key Concepts
- `filter(function, collection)` keeps only the elements that meet a condition.
- Returns a **filter object** (iterator) → usually converted to a `list`.

---

## Example 1 – Using a Named Function
```python
def is_passing(grade):
    return grade >= 60

grades = [90, 32, 83, 44, 75]
passing_grades = list(filter(is_passing, grades))
print(passing_grades)  # [90, 83, 75]

USING A LAMBDA FUNCTION:

grades = [90, 32, 83, 44, 75]
passing_grades = list(filter(lambda g: g >= 60, grades))
print(passing_grades)  # [90, 83, 75]
