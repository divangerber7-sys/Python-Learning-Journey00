# Lesson 62: Function Decorators

## 🔑 Key Concepts
- A **decorator** is a function that wraps another function to extend or modify its behavior.
- Uses `*args` and `**kwargs` so it works with any number of arguments.
- Applied using the `@decorator_name` syntax above the target function.
- Multiple decorators can be stacked.

---

## Example

```python
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")

get_ice_cream("rocky road")


EXAMPLE OUTPUT:

*You add sprinkles*
*You add fudge*
Here is your rocky road ice cream
