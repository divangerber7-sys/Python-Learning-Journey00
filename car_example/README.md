# Python OOP Example: Car Class

This repository demonstrates **Object-Oriented Programming (OOP)** in Python using a `Car` class.  

It includes:

- Defining classes and objects
- Attributes and methods
- Using constructors
- Inheritance (subclasses)
- Example usage with multiple cars

---

## Car Class

A `Car` has the following attributes:

- `make` – Manufacturer (e.g., Ford, Chery)
- `model` – Car model (e.g., Everest, Tiggo Pro7)
- `year` – Year of manufacture
- `for_sale` – Boolean indicating if car is available for sale

### Methods

- `drive()` – Prints driving action
- `stop()` – Prints stopping action
- `describe()` – Prints car description

---

## Inheritance Example

- `ElectricCar` inherits from `Car`
- Adds attribute `battery_capacity`
- Overrides `describe()` method

---

## Example Usage

```python
from car_example import Car, ElectricCar

car1 = Car("Chery", "Tiggo Pro7", 2025, True)
car2 = ElectricCar("Tesla", "Model S", 2025, True, 100)

car1.drive()
car2.describe()
