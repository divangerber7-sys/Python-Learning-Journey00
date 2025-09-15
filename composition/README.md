# Lesson 56: Composition

## Aggregation vs. Composition

- **Aggregation** → The "whole" references independent objects.  
  Example: A library *has* books. Even if the library is deleted, the books can still exist.

- **Composition** → The "whole" *owns* its parts.  
  Example: A car *owns* an engine and wheels. If the car is destroyed, so are the engine and wheels.

---

## Example: Car with Engine & Wheels
```python
car1 = Car("McLaren", "SLR", 722, 19)
car2 = Car("Ford", "Everest", 300, 21)

print(car1.display_car())
print(car2.display_car())


example output:
McLaren SLR 722(Hp) 19In
Ford Everest 300(Hp) 21In


