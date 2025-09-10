# Lesson 04 - Math in Python

In this lesson, I learned how to perform **arithmetic operations** and use Python’s built-in math functionality.  
I also created small programs to solve **real-world math problems** such as calculating the area, circumference, and hypotenuse.  

---

## Key Concepts Learned
- Arithmetic operations: `+`, `-`, `*`, `/`, `**`, `%`
- **Augmented assignment operators** (e.g., `+=`, `-=`)
- Built-in math functions: `round()`, `abs()`, `pow()`, `max()`, `min()`
- The `math` module → `pi`, `e`, `sqrt()`, `ceil()`, `floor()`
- Applying math to solve geometry problems

---

## Code

```python
# Arithmetic operations
friends = 10

#friends += 1
#friends -= 2
#friends *= 3
#friends /= 2
#friends **= 2

# Modulus (remainder)
#remainder = friends % 2


# Built-in math functions
"""
x = 3.69
y = 5
z = 69

#result = round(x)
#result = abs(y)
#result = pow(5, 3)
#result = max(x, y, z)
#result = min(x, y, z)

print(result)
"""

import math
x = 9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)  # rounds up
# result = math.floor(x) # rounds down
#print(result)


# EXERCISES

# Circumference of a circle
"""
radius = float(input("Please enter the radius of the circle : "))
circumference = 2 * math.pi * radius 
print(f"The circumference of the circle is: {round(circumference, 3)} cm")
"""

# Area of a circle
"""
radius = float(input("Please enter the radius of the circle : "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {round(area, 2)} cm^2")
"""

# Hypotenuse of a right triangle
a = float(input("Please enter the length of side A: "))
b = float(input("Please enter the length of side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"The length of Side C is: {round(c, 2)} cm^2")

d(x)
#result = abs(y)
