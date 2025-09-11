
---

### 2️⃣ `while_loops/while_loops.py`
```python
# While Loops Examples

# Example 1: Ask for name until provided
name = input("What is your name? ")

while name == "":
    print("You didn't enter a name")
    name = input("What is your name? ")
print(f"Hello {name}")


# Example 2: Age validation
age = int(input("What is your age? "))

while age < 0:
    print("You didn't enter a valid age")
    age = int(input("What is your age? "))

print(f"Good, you are {age} years old")


# Example 3: Food preferences with quit option
food = input("What is your favorite food? (q to quit): ")

while not food == "q":
    print(f"You really like {food}")
    food = input("Do you have another favorite food? (q to quit): ")

print("Bye Bye")


# Example 4: Number validation with OR condition
num = int(input("Please choose a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid option.")
    num = int(input("Please choose a number between 1 and 10: "))

print(f"Your number is {num}"
