# super() = Function used in a child class to call methods from a parent class (superclass)
#           Allows you to extend the functionality of inherited methods.
#
# Method overriding = If a child defines the same method as the parent, the child’s method takes precedence.
#                     You can still call the parent method with super().

class Shapes:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shapes):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)  # call parent constructor
        self.radius = radius

    # Method overriding with extension
    def describe(self):
        super().describe()
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius} cm^2")


class Square(Shapes):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a square with an area of {self.width * self.width} cm^2")


class Triangle(Shapes):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {self.width * self.height / 2} cm^2")


if __name__ == "__main__":
    circle = Circle(colour="red", is_filled=True, radius=5)
    square = Square(colour="purple", is_filled=False, width=6)
    triangle = Triangle(colour="yellow", is_filled=True, width=7, height=3)

    circle.describe()
    print()
    square.describe()
    print()
    triangle.describe()
