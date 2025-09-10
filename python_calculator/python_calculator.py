
### **python_calculator.py**

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
