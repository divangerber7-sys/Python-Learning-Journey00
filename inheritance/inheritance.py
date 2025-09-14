# Python Inheritance Example

# Inheritance allows a class to inherit attributes and methods from another class
# Helps with code reusability and extensibility
# Syntax: class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating food")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Child classes inherit from Animal
class Dog(Animal):
    def speak(self):
        print("Woof Woof!!!")

class Cat(Animal):
    def speak(self):
        print("I rule the world!!!")

class Mouse(Animal):
    def speak(self):
        print("What are we gonna do today??")

# Create instances of each child class
dog = Dog("Loki")
cat = Cat("Siff")
mouse = Mouse("Brain")

# Dog actions
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
print(" ")

# Cat actions
print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
print(" ")

# Mouse actions
print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()
