# Lesson 06 - Python Calculator

In this lesson, I built a simple **Python calculator** that performs basic arithmetic operations based on user input.  
This project combines:
- User input
- Conditional logic
- Arithmetic operations
- Error handling for invalid operators

---

## Code

```python
# PYTHON CALCULATOR

operator = input("Please enter your operator (+ - * /) : ")
num1 = float(input("Please enter your first number : "))
num2 = float(input("Please enter your second number : "))

if operator == "+":
    print(round(num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print(f"Invalid operator = {operator}")

exit()
