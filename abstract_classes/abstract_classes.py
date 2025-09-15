# Abstract Classes in Python
# Abstract class: A class that cannot be instantiated on its own; it must be subclassed.
# They can contain abstract methods, which are declared but not implemented.
#
# Benefits of abstract classes:
# 1. Prevents instantiation of the class itself
# 2. Enforces that children implement abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Subclasses must implement all abstract methods

class Car(Vehicle):
    def go(self):
        print("Your vehicle is moving")

    def stop(self):
        print("Your vehicle is stopped")


class Motorcycle(Vehicle):
    def go(self):
        print("Your Ducati is moving")

    def stop(self):
        print("Your Ducati is stopped")


class Boat(Vehicle):
    def go(self):
        print("You are sailing the oceans")

    def stop(self):
        print("A port is no place for a boat")


if __name__ == "__main__":
    # car = Vehicle()  # ❌ This will raise an error (cannot instantiate abstract class)

    car = Car()
    car.go()
    car.stop()
    print()

    motorcycle = Motorcycle()
    motorcycle.go()
    motorcycle.stop()
    print()

    boat = Boat()
    boat.go()
    boat.stop()
