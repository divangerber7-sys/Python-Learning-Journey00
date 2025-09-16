# @property = Decorator that lets you define methods that act like attributes.
# Benefits:
#   - Control access to attributes (encapsulation)
#   - Add logic when getting, setting, or deleting values
#   - Cleaner syntax than using explicit getters/setters


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter method (read access)
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Setter method (write access with validation)
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be positive")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be positive")

    # Deleter method (delete access)
    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")


if __name__ == "__main__":
    rectangle = Rectangle(13, 30)

    # Access like attributes
    print(rectangle.width)
    print(rectangle.height)

    # Update values (setter called)
    rectangle.width = 5
    rectangle.height = 69
    print(rectangle.width)
    print(rectangle.height)

    # Invalid update
    rectangle.width = -10  # triggers validation

    # Delete attributes
    del rectangle.width
    del rectangle.height
