# Writing Files in Python (.txt, .json, .csv)
import json
import csv

# ---------- PLAIN TEXT ----------
txt_data = "Ramen"
file_path = "output.txt"  # relative file path

with open(file_path, "w") as file:  # "w" = overwrite / create new
    file.write(txt_data)
    print(f"✅ txt file '{file_path}' was created")

# Append mode ("a")
with open(file_path, "a") as file:
    file.write("\nMore ramen 🍜")
    print(f"✅ text appended to '{file_path}'")

# Writing a list of employees (each on new line)
employees = ["Kevin", "Flynn", "Loki", "Siff"]
with open("employees.txt", "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print("✅ employees.txt created with names")

# ---------- JSON ----------
employee = {
    "name": "Kevin",
    "age": 35,
    "job": "cook"
}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)
    print("✅ employee.json created")

# ---------- CSV ----------
employees = [
    ["Name", "Age", "Job"],
    ["Siff", 21, "Warrior"],
    ["Flynn", 36, "Creator"],
    ["Patrick", 44, "Unemployed"]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)
    print("✅ employees.csv created")

