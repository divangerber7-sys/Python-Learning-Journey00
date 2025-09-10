
---

### 📄 `lesson_email_slicer/email_slicer.py`
```python
#  Email Slicer Program Exercise

email = input("Please enter your email: ")

# index = email.index("@")
# username = email[: index]
# domain = email[index + 1 :]

# To use less code:
username = email[: email.index("@")]
domain = email[email.index("@") + 1 :]

print(f"Your username is: {username} \nand your domain is: {domain}")
