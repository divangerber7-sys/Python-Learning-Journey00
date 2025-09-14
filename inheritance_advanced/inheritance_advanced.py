# Multiple & Multilevel Inheritance Example

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Multilevel Inheritance
class Prey(Animal):
    def flee(self):
        print(f"{self.name} can Flee")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} can Hunt")


# Multiple Inheritance
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


# Instances
rabbit = Rabbit("Jessica")
hawk = Hawk("Bald")
fish = Fish("Wanda")


# Actions
rabbit.eat()
hawk.eat()
fish.eat()
print(" ")

rabbit.sleep()
hawk.sleep()
fish.sleep()
print(" ")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()
