# Aggregation vs. Composition
# ---------------------------
# Aggregation = A relationship where one object contains references 
#               to other INDEPENDENT objects. ("has-a" relationship)
#
# Composition = The composed object directly owns its components, 
#               which cannot exist independently. ("owns-a" relationship)


class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        # Composition: Car directly creates/owns its parts
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for _ in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(Hp) {self.wheels[0].size}In"


if __name__ == "__main__":
    car1 = Car("McLaren", "SLR", 722, 19)
    car2 = Car("Ford", "Everest", 300, 21)

    print(car1.display_car())
    print(car2.display_car())
