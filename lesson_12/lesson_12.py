
---

### 📄 `lesson_indexing/indexing.py`
```python
#   Indexing    =   Accessing elements of a sequence using [] (indexing operators)
#                   [start : end : step]

credit_number = "1234-5678-9012-3456"

# print(credit_number[0])         # First character
# print(credit_number[0:4])       # From index 0 to 3
# print(credit_number[0:18:2])    # Every 2nd char up to index 17
# print(credit_number[5:])        # From index 5 to end
# print(credit_number[-1])        # Last character
# print(credit_number[::4])       # Every 4th character

# Masking the number (show last 4 only)
# last_digits = credit_number[-4:]
# print(f"xxxx-xxxx-xxxx-{last_digits}")

# Reversing the string
credit_number = credit_number[::-1]
print(credit_number)
