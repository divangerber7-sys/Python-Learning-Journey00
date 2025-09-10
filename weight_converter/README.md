# Lesson 08 - Python Weight Converter

In this lesson, I created a **weight converter** that switches between **kilograms (K)** and **pounds (L)**.  
This project reinforces:
- User input
- Conditional logic
- Arithmetic conversions
- Error handling for invalid units

---

## Code

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

SAMPLE
Please enter you weight: 70
Please enter your unit (K / L) : K
Your weight is 154.35 Lbs

Please enter you weight: 154
Please enter your unit (K / L) : L
Your weight is 69.84 Kgs)

Please enter you weight: 50
Please enter your unit (K / L) : X
The unit of X is not valid!!



