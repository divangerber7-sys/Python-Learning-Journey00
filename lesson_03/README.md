# Lesson 03 - User Input and Mini Projects

In this lesson, I practiced using the **`input()` function** in Python to gather information from the user.  
I then applied this to create small projects that combine variables, arithmetic, and string formatting.  

---

## Key Concepts Learned
- `input()` → for user interaction
- Type conversion (`int()`, `float()`) → converting user input into numbers
- String formatting with f-strings
- Basic arithmetic operations (`*`, `+`)
- Building small real-world style programs

---

## Code

```python
# Simple input example
#name = input("What is your name? ")
#age = input("How old are you? ")
#print(f"Hello {name}")
#print(f"Your age is {age}")


# MAD LIBS GAME
"""
adjective1 = input("Please enter adjective: ")
noun1 = input("Please enter noun: ")
adjective2 = input("Please enter adjective: ")
verb1 = input("Please enter verb: ")
adjective3 = input("Please enter adjective: ")

print(f"Today I went to a {adjective1} marketplace")
print(f"In an exhibit, I saw {noun1}")
print(f"{noun1} was {adjective2} and {verb1}ing")
print(f"I was {adjective3}")
"""


# AREA CALCULATOR
"""
length = float(input("Please enter the length of the exhibition: "))
width = float(input("Please enter the width of the exhibition: "))

area = length * width
print(f"The area of the exhibition is {area}cm\u00b2")
"""


# VOLUME CALCULATOR
"""
length = float(input("Please enter the length of the exhibition: "))
width = float(input("Please enter the width of the exhibition: "))
height = float(input("Please enter the height of the exhibition: "))

volume = length * width * height
print(f"The volume of the exhibition is {volume}cm\u00b3")
"""


# SHOPPING CART PROGRAM
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"\nYou have bought {quantity} x {item}/s")
print(f"Your total is: $ {round(total, 2)} ")
print("Thank you for coming. See you soon!!")


