# Class methods = Allow operations related to the class itself.
#                 They take (cls) as the first parameter, which represents the class.
#
# Instance methods (self) = Best for operations on individual objects.
# Static methods          = Best for utility functions (no access to self/cls).
# Class methods           = Best for class-level data and operations.


class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # Class methods
    @classmethod
    def get_count(cls):
        return f"The total number of students is {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "No students enrolled"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


if __name__ == "__main__":
    student1 = Student("Spongebob", 3.2)
    student2 = Student("Patrick", 3.0)
    student3 = Student("Sandy", 4.0)

    # Using class methods
    print(Student.get_count())
    print(Student.get_average_gpa())

    # Instance method example
    print(student1.get_info())
