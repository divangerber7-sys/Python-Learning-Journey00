# Lesson 71: Writing Files in Python

## Why This Matters
Saving data is a core part of most programs. Python makes it easy to write files in multiple formats:
- `.txt` for plain text and logs
- `.json` for structured key/value data
- `.csv` for spreadsheets and tabular data

---

## File Modes
- `"w"` → Write (overwrite or create new file)
- `"a"` → Append (add to existing file)
- `"x"` → Create new (error if file exists)
- `"r"` → Read (default)

---

## Examples

### Plain Text (`.txt`)
```python
with open("output.txt", "w") as file:
    file.write("Hello, world!")


JSON - .json:

import json

employee = {"name": "Kevin", "age": 35, "job": "cook"}

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)


CSV - .csv:

import csv

employees = [
    ["Name", "Age", "Job"],
    ["Siff", 21, "Warrior"]
]

with open("employees.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(employees)
