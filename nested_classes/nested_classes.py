# Nested class = A class defined within another class
# ---------------------------------------------------
# Benefits:
# - Logically group classes that are closely related
# - Encapsulate details that aren’t relevant outside the parent
# - Keep the namespace clean, reduce naming conflicts


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} ({self.position})"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        # Creates Employee objects scoped to this Company
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


if __name__ == "__main__":
    company1 = Company("End of Line Club")
    company2 = Company("Flynn's Arcade")

    company1.add_employee("Eugene", "Manager")
    company1.add_employee("Spongebob", "Cook")
    company1.add_employee("Squidward", "Cashier")

    print(company1.company_name)
    for employee in company1.list_employees():
        print(employee)

    print("\n" + company2.company_name)
    company2.add_employee("Penny", "Manager")
    company2.add_employee("Sheldon", "Server")
    for employee in company2.list_employees():
        print(employee)


