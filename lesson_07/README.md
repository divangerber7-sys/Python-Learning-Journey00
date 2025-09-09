# Lesson 07 - Python Weight Converter

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

## Notice - Bug to fix as I progress - Line 27 as additional ) that I need to remove
