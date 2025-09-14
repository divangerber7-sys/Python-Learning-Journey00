
---

## 2️⃣ `car_example.py`
```python
# car_example.py
# Python OOP Example with Car and ElectricCar

class Car:
    def __init__(self, make, model, year, for_sale=True):
        self.make = make
        self.model = model
        self.year = year
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive a really nice {self.make} {self.model}")

    def stop(self):
        print(f"The {self.make} {self.model} stops safely.")

    def describe(self):
        status = "available" if self.for_sale else "not for sale"
        print(f"The {self.year} {self.make} {self.model} is {status}.")


# Inheritance Example
class ElectricCar(Car):
    def __init__(self, make, model, year, for_sale=True, battery_capacity=75):
        super().__init__(make, model, year, for_sale)
        self.battery_capacity = battery_capacity  # in kWh

    def describe(self):
        status = "available" if self.for_sale else "not for sale"
        print(f"The {self.year} {self.make} {self.model} is {status} and has a {self.battery_capacity} kWh battery.")


# Example Usage
if __name__ == "__main__":
    car1 = Car("Chery", "Tiggo Pro7", 2025)
    car2 = Car("Ford", "Everest Platinum", 2025, False)
    car3 = ElectricCar("Tesla", "Model S", 2025, True, 100)

    car1.drive()
    car2.stop()
    car3.describe()
