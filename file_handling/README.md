# Lesson 70: File and Directory Checking

## Why This Matters
Before working with files, you should **check if they exist** to avoid crashes and handle errors gracefully.

---

## Checking Files and Directories
Python’s `os.path` module gives us useful tools:

- `os.path.exists(path)` → checks if file/directory exists  
- `os.path.isfile(path)` → checks if path is a file  
- `os.path.isdir(path)` → checks if path is a directory  

---

## Example
```python
import os

file_path = "C:/Users/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"✅ The location '{file_path}' exists!")

    if os.path.isfile(file_path):
        print("📄 That is indeed a file!")

    elif os.path.isdir(file_path):
        print("📂 That is indeed a directory!")

else:
    print(f"❌ The location '{file_path}' does not exist!")
