---

### **temperature_converter.py**

```python
# Python temperature conversion program

unit = input("Is this temperature in Celsius or Fahrenheit (C/F) : ")
temp = float(input("Please enter the temperature? "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp} F")
elif unit == "F":
    temp = round(( temp -32) * 5/9, 1)
    print(f"The temperature in Celsius is: {temp} C")
else:
    print(f"{unit} isn't a valid unit")
