# Lesson 52: `super()` and Method Overriding

## What is `super()`?
- The `super()` function is used in a child class to **call methods from its parent class**.
- This allows us to reuse or extend parent functionality without rewriting code.

## Method Overriding
- If a child defines the same method as its parent, the **child’s version takes precedence**.
- With `super()`, you can combine both the parent and child methods.

## Example
```python
class Shapes:
    def describe(self):
        print("This is a shape")

class Circle(Shapes):
    def describe(self):
        super().describe()  # Call parent version
        print("This is a circle")


EXAMPLE OUTPUT:
It is red and filled
It is a circle with an area of 78.5 cm^2

It is purple and not filled
It is a square with an area of 36 cm^2

It is yellow and filled
It is a triangle with an area of 10.5 cm^2
