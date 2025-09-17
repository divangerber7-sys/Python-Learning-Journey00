# Lesson 72: Reading Files in Python

## Why This Matters
Most applications don’t just save files – they also **read data back in**.  
Python supports easy reading of `.txt`, `.json`, and `.csv`.

---

## Examples

### TXT
```python
with open("input.txt", "r") as file:
    content = file.read()
    print(content)


JSON:

import json

with open("input.json", "r") as file:
    content = json.load(file)
    print(content["job"])


CSV:

import csv

with open("input.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


Access a column:

print(row[2])  # third column (index starts at 0)
