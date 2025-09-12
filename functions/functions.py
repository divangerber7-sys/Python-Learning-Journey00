#   function = A block of reusable code
#              place () after the function name to invoke it

# Example 1: Simple function without parameters
def happy_birthday():
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("May you have many many more")

# Call the function
happy_birthday()


# Example 2: Function with one parameter
def happy_birthday_name(name):
    print(f"Happy Birthday to {name}")
    print(f"Happy Birthday to {name}")
    print("May you have many many more")

happy_birthday_name("John")


# Example 3: Function with multiple parameters
def happy_birthday_age(name, age):
    print(f"Happy Birthday to {name}")
    print(f"You are now {age} years old. Man, that is old!!")
    print()

happy_birthday_age("Michael", 35)
happy_birthday_age("Loki", 77)
happy_birthday_age("Thor", 101)


# Example 4: Function with multiple arguments (invoice example)
def display_invoice(username, amount, due_date):
    print(f"Aloha {username}")
    print(f"Your invoice amount of R{amount: .2f} is due by {due_date}")
    print()

display_invoice("Coffee Supreme", 2500.25, "2025/09/30")


# Example 5: Functions with return statements (calculator)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(f"69 ÷ 100 = {divide(69, 100)}")


# Example 6: Function to create a full name
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)
