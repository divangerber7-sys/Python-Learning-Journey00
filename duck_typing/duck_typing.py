# "Duck Typing" = Another way to achieve polymorphism besides inheritance
# If an object has the necessary attributes/methods, it can be treated as that type
# "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof Woof!!")

class Cat(Animal):
    def speak(self):
        print("I rule the world!!!")

class Car(Animal):
    alive = False

    # Because Car has a speak() method, it behaves like an Animal in this context
    def speak(self):
        print("Honky Honky")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Car()]

    for animal in animals:
        animal.speak()
        print("Alive:", animal.alive)
