# Lesson 16 – While Loops

## 📖 Overview
This lesson introduces the **`while` loop**, which allows code to run repeatedly **as long as a condition remains true**.  
It’s useful for input validation, repetitive tasks, or looping until a specific exit condition is met.

---

## 🧪 Example Code
```python
# Basic example
name = input("What is your name? ")

while name == "":
    print("You didn't enter a name")
    name = input("What is your name? ")
print(f"Hello {name}")

# Age validation
age = int(input("What is your age? "))

while age < 0:
    print("You didn't enter a valid age")
    age = int(input("What is your age? "))

print(f"Good, you are {age} years old")

# Food loop with quit option
food = input("What is your favorite food? (q to quit): ")

while not food == "q":
    print(f"You really like {food}")
    food = input("Do you have another favorite food? (q to quit): ")

print("Bye Bye")

# Number validation with OR condition
num = int(input("Please choose a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid option.")
    num = int(input("Please choose a number between 1 and 10: "))



