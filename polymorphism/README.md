# Lesson 53: Polymorphism

## What is Polymorphism?
Polymorphism means **"many forms"**.  
It allows different object types to be treated under a **common interface**.

### Ways to Achieve Polymorphism
1. **Inheritance** – A child class can be treated as its parent.
2. **Duck Typing** – If an object has the necessary methods, it can be used (regardless of its type).

---

## Example
```python
shapes = [
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza("Pepperoni", 15)
]

for shape in shapes:
    print(f"{shape.area()} cm²")

EXAMPLE OUTPUT:
Circle: 50.24 cm²
Square: 25 cm²
Triangle: 21.0 cm²
Pizza: 706.5 cm²

