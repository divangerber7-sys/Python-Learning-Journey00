# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

# Example 1: String membership
word = "APPLE"
letter = "A"

if letter in word:
    print(f"There is indeed an {letter} in the secret word!")
else:
    print(f"There is no {letter} in the secret word!")

# Example 2: Set membership
students = {"Spongebob", "Sandy", "Patrick"}
student = "Spongebob"

if student in students:
    print(f"{student} is in this class!")
else:
    print(f"{student} is not in this class!")

# Example 3: Dictionary membership (checks keys by default)
grades = {
    "Sandy": "A",
    "Squidward": "B",
    "Spongebob": "C",
    "Patrick": "D"
}

student = "Sandy"
if student in grades:
    print(f"{student} has a grade of {grades[student]}")
else:
    print(f"{student} is not in this class!")

# Example 4: Simple email validation using membership operators
email = "Thisisfake@gmail.com"

if "@" in email and "." in email:
    print("The email looks valid ✅")
else:
    print("The email is not valid ❌")
