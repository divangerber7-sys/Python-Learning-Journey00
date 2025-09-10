# Lesson: String Methods in Python

This lesson introduces **string methods** in Python and how to use them for text manipulation and validation.

---

## 🔑 Key String Methods Covered
- `len(string)` → Returns the length of a string.  
- `string.find("x")` → Finds the first occurrence of `"x"` in the string (or `-1` if not found).  
- `string.rfind("x")` → Finds the first occurrence of `"x"` searching from the end.  
- `string.capitalize()` → Capitalizes only the first letter.  
- `string.upper()` → Converts entire string to uppercase.  
- `string.lower()` → Converts entire string to lowercase.  
- `string.isdigit()` → Returns `True` if string contains only digits.  
- `string.isalpha()` → Returns `True` if string contains only letters.  
- `string.count("-")` → Counts how many times `"-"` appears.  
- `string.replace("-", "*")` → Replaces `"-"` with `"*"`.

---

## 📝 Exercise: Username Validation
Rules:
1. Username must be **12 characters or fewer**  
2. Username must **not contain spaces**  
3. Username must **not contain digits**  

### ✅ Example Code
```python
username = input("Enter your username please: ")

if len(username) > 12:
    print("Your username is too long")
elif not username.find(" ") == -1:
    print("Your username is invalid. Cannot contain space")
elif not username.isalpha():
    print("Your username is invalid. Cannot contain numbers")
else:
    print(f"Your username is valid.\nWelcome {username}")

Example Run:
Enter your username please: Divan
Your username is valid.
Welcome Divan
