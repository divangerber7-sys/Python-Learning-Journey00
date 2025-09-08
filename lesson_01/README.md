# Lesson 01 - Variables and Basic Data Types

In this lesson, I learned about **variables** in Python and how they act as containers for values.  
I explored the four common data types:  

- **Strings** → Text values (e.g., names, email addresses, favorite food)  
- **Integers** → Whole numbers (e.g., age, quantity)  
- **Floats** → Numbers with decimals (e.g., price, GPA, distance)  
- **Booleans** → True/False values  

I also practiced:  
- Using **f-strings** for cleaner formatting  
- A simple **if/else statement** to check conditions  

---

## Code

```python
# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings - Just text
first_name = "Divan"
food = "Noodles"
email = "thisisfake@fake.com"

#print (first_name)

# f-string = formatted string literals, begin a string with f before the opening
# quotation mark. Inside this string, you can write a Python expression between {and}
# characters that can refer to variables or literal value. Instead of + (concatenate)

#print ("Hello " + first_name)
#print (f"Hello {first_name}")

#print (f"You really like {food}!!!")
#print(email)
#print(f"I have your email adress as {email}.")

# Integer - Whole number
age = 25
quantity = 3
num_of_students = 30

#print(f"You are {age} years old. ")
#print(f"You are buying {quantity} of the product")
#print(f"Your class has {num_of_students} students attending.")

# Float - Decimals
price = 10.99
gpa = 3.14
distance = 5.5

#print(f"The price of this is: ${price}")
#print(f"My GPA for the year is: {gpa}")
#print(f"You ran {distance}km to be here!!")

# Boolean - True or False

is_student = False

#print(f"Are you a student here: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student")
