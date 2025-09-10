
---

### **lesson_08/lesson_08.py**

```python
# Python weight converter

weight = float(input("Please enter you weight: "))
unit = input("Please enter your unit (K / L) : ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)} {unit})")
else:
    print(f"The unit of {unit} is not valid!!")
