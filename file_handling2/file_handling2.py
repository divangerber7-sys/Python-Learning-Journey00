# Reading Files in Python (.txt, .json, .csv)
import json
import csv

# ---------- TXT ----------
file_path = "input.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print("TXT Content:")
        print(content)
except FileNotFoundError:
    print("❌ File not found")
except PermissionError:
    print("❌ Permission denied")

# ---------- JSON ----------
file_path = "input.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print("\nJSON Content:")
        print(content)

        # Access a specific key
        print("Job:", content.get("job"))
except FileNotFoundError:
    print("❌ File not found")
except PermissionError:
    print("❌ Permission denied")

# ---------- CSV ----------
file_path = "input.csv"

try:
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        print("\nCSV Content:")
        for row in reader:
            print(row)

    # Example: print only the 3rd column (Job)
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        print("\nCSV 'Job' Column:")
        for row in reader:
            print(row[2])
except FileNotFoundError:
    print("❌ File not found")
except PermissionError:
    print("❌ Permission denied")
