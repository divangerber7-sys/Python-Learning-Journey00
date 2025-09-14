# Python Class Variables Example

# Class variables = shared among all instances of a class
# Defined outside the constructor
# Allows sharing data among all objects created from that class

class Student:

    class_year = 2025    # Class variable
    num_students = 0     # Class variable to track number of students

    def __init__(self, name, age):
        self.name = name   # Instance variable
        self.age = age     # Instance variable
        Student.num_students += 1  # Modify class variable

# Creating instances of Student
student1 = Student("Spongebob", 22)
student2 = Student("Patrick", 25)
student3 = Student("Squidward", 23)
student4 = Student("Loki", 24)

# Accessing instance variables
print(student2.name)  # Patrick
print(student2.age)   # 25

# Accessing class variables (best practice: via class name)
print(Student.class_year)     # 2025
print(Student.num_students)   # 4

# Exercise: Display all students graduating and the year
print(f"\nThere are {Student.num_students} students graduating in {Student.class_year}:")
for student in [student1, student2, student3, student4]:
    print(student.name)
