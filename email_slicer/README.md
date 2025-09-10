# Lesson: Email Slicer Program

This program demonstrates **string indexing and slicing** by splitting an email address into a **username** and a **domain**.

---

## 🧪 Example Code
```python
email = input("Please enter your email: ")

username = email[: email.index("@")]
domain = email[email.index("@") + 1 :]

print(f"Your username is: {username} \nand your domain is: {domain}")

SAMPLE RUN
Please enter your email: divan@example.com
Your username is: divan 
and your domain is: example.com
