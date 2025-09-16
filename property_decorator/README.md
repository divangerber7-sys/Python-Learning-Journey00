# Lesson 61: The `@property` Decorator

## 🔑 Key Concepts
- `@property` turns a method into an **attribute-like property**.
- Lets you add custom logic when reading, writing, or deleting attributes.
- Helps enforce **encapsulation** (protect internal data with `_` prefix).

---

## Example

```python
rectangle = Rectangle(13, 30)

print(rectangle.width)   # "13.0cm"
print(rectangle.height)  # "30.0cm"

rectangle.width = 5      # valid update
rectangle.height = -10   # invalid, triggers validation


EXAMPLE OUTPUT:

13.0cm
30.0cm
5.0cm
Height must be positive
