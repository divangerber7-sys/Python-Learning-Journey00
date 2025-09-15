# Polymorphism = Greek word meaning "many forms"
# Poly = Many
# Morphe = Form
#
# TWO WAYS TO ACHIEVE POLYMORPHISM
# 1. Inheritance = An object can be treated as if it is its parent type
# 2. Duck Typing = If an object has the required methods/attributes, it can be used regardless of its type

from abc import ABC, abstractmethod

# Abstract Shape class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphic subclass of Circle
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

if __name__ == "__main__":
    # Each object is treated as a Shape due to polymorphism
    shapes = [
        Circle(4),
        Square(5),
        Triangle(6, 7),
        Pizza("Pepperoni", 15)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__}: {shape.area()} cm²")
