# File and Directory Checking in Python
import os

# ---------- RELATIVE FILE PATH ----------
file_path = "test.txt"

if os.path.exists(file_path):
    print(f"✅ The location '{file_path}' exists!")
else:
    print(f"❌ The location '{file_path}' does not exist!")

# ---------- FILE IN A SUBDIRECTORY ----------
file_path = "stuff/test.txt"

if os.path.exists(file_path):
    print(f"✅ The location '{file_path}' exists!")
else:
    print(f"❌ The location '{file_path}' does not exist!")

# ---------- ABSOLUTE FILE PATH ----------
# Note: Use forward slashes (/) OR double backslashes (\\) on Windows
file_path = "C:/Users/Desktop/test.txt"

if os.path.exists(file_path):
    print(f"✅ The location '{file_path}' exists!")

    if os.path.isfile(file_path):
        print("📄 That is indeed a file!")
    elif os.path.isdir(file_path):
        print("📂 That is indeed a directory!")
else:
    print(f"❌ The location '{file_path}' does not exist!")
