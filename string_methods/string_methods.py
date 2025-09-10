---

### 📄 `lesson_string_methods/string_methods.py`
```python
#   String Methods

# name = input("Enter your name please: ")
# phone_number = input("Enter your phone number please: ")

# result = len(name)                  # returns length of string
# result = name.find("a")             # finds first "a", -1 if not found
# result = name.rfind("e")            # finds first "e" from the end
# name = name.capitalize()            # capitalize first letter
# name = name.upper()                 # uppercase all letters
# name = name.lower()                 # lowercase all letters
# result = name.isdigit()             # True if only digits
# result = name.isalpha()             # True if only letters
# result = phone_number.count("-")    # counts "-" in string
# result = phone_number.replace("-", "*")

# print(result)


#   EXERCISE
#   Validate user input
#   1 - Username is no more than 12 characters
#   2 - Username must not contain spaces
#   3 - Username must not contain digits

username = input("Enter your username please: ")

if len(username) > 12:
    print("Your username is too long")
elif not username.find(" ") == -1:
    print("Your username is invalid. Cannot contain space")
elif not username.isalpha():
    print("Your username is invalid. Cannot contain numbers")
else:
    print(f"Your username is valid.\nWelcome {username}")
