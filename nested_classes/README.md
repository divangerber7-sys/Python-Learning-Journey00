# Lesson 57: Nested Classes

## What is a Nested Class?
A nested class is defined **inside another class**.

### Benefits
- Groups related classes together logically.
- Encapsulates implementation details.
- Keeps the namespace clean and avoids conflicts.

---

## Example: `Company` with nested `Employee`
```python
company1 = Company("End of Line Club")
company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")

print(company1.company_name)
for employee in company1.list_employees():
    print(employee)

EXAMPLE OUTPUT:
End of Line Club
Eugene (Manager)
Spongebob (Cook)

