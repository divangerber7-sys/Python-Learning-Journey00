# Static methods = Belong to the class, not to individual objects (instances).
#                  Used for general utility functions that don't depend on
#                  instance or class attributes.
#
# Instance methods = Operate on instances of the class (use `self`).
# Static methods   = Utility functions (use `@staticmethod` decorator).


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method: belongs to each object
    def get_info(self):
        return f"{self.name} = {self.position}"

    # Static method: belongs to the class
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Cashier", "Janitor"]
        return position in valid_positions


if __name__ == "__main__":
    employee1 = Employee("Eugene", "Manager")
    employee2 = Employee("Squidward", "Cashier")
    employee3 = Employee("Spongebob", "Cook")

    # Instance methods (operate on objects)
    print(employee1.get_info())
    print(employee2.get_info())
    print(employee3.get_info())

    # Static method (utility, called on class itself)
    print(Employee.is_valid_position("Manager"))
    print(Employee.is_valid_position("CEO"))  # Not valid

