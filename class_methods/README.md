# Lesson 59: Class Methods

## 🔑 Key Concepts
- **Instance Methods**
  - Use `self`.
  - Work on individual objects.

- **Static Methods**
  - Use `@staticmethod`.
  - No access to `self` or `cls`.
  - Great for utility/helper functions.

- **Class Methods**
  - Use `@classmethod`.
  - First parameter is `cls` (the class itself).
  - Useful for **class-level data and operations**.

---

## Example
```python
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 3.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())        # Class method
print(Student.get_average_gpa())  # Class method
print(student1.get_info())        # Instance method


EXAMPLE OUTPUT:
The total number of students is 3
Average GPA: 3.40
Spongebob 3.2

