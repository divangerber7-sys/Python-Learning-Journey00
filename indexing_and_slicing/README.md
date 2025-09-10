# Lesson: Indexing and Slicing in Python

Indexing allows you to access elements of a sequence (like strings, lists, or tuples) using **square brackets `[]`**.

---

## 🔑 Syntax
sequence[start:end:step]:

- `start` → starting index (inclusive)  
- `end` → ending index (exclusive)  
- `step` → interval (default is 1)  

---

## 🧪 Examples with Strings
```python
credit_number = "1234-5678-9012-3456"

print(credit_number[0])        # First character -> "1"
print(credit_number[0:4])      # Slice from index 0 to 3 -> "1234"
print(credit_number[0:18:2])   # Every 2nd character up to index 17
print(credit_number[5:])       # From index 5 to end -> "5678-9012-3456"
print(credit_number[-1])       # Last character -> "6"
print(credit_number[::4])      # Every 4th character

MASKING EXAMPLE
credit_number = "1234-5678-9012-3456"
last_digits = credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")
OUTPUT
xxxx-xxxx-xxxx-3456

REVERSE STRING
credit_number = "1234-5678-9012-3456"
print(credit_number[::-1])
OUTPUT
6543-2109-8765-4321


