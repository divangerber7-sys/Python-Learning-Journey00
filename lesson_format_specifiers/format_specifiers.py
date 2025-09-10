
---

### 📄 `lesson_format_specifiers/format_specifiers.py`
```python
#  Format Specifiers = {value:flags} format a value based on what flags are inserted

price1 = 3000.87456
price2 = -613.3487
price3 = 1299.99

# Round number to decimals after comma
# print(f"Price 1 is: ${price1:.2f}")
# print(f"Price 2 is: ${price2:.2f}")
# print(f"Price 3 is: ${price3:.2f}")

# Allocate total number of spaces
print(f"Price 1 is: ${price1:10}")
print(f"Price 2 is: ${price2:10}")
print(f"Price 3 is: ${price3:10}")

# Zero pad (width = 10)
print(f"Price 1 is: ${price1:010}")
print(f"Price 2 is: ${price2:010}")
print(f"Price 3 is: ${price3:010}")

# Left align
print(f"Price 1 is: ${price1:<10}")
print(f"Price 2 is: ${price2:<10}")
print(f"Price 3 is: ${price3:<10}")

# Right align
print(f"Price 1 is: ${price1:>10}")
print(f"Price 2 is: ${price2:>10}")
print(f"Price 3 is: ${price3:>10}")

# Center align
print(f"Price 1 is: ${price1:^10}")
print(f"Price 2 is: ${price2:^10}")
print(f"Price 3 is: ${price3:^10}")

# Show signs (+/-)
print(f"Price 1 is: ${price1:+}")
print(f"Price 2 is: ${price2:+}")
print(f"Price 3 is: ${price3:+}")

# Force sign at leftmost position
print(f"Price 1 is: ${price1:=}")
print(f"Price 2 is: ${price2:=}")
print(f"Price 3 is: ${price3:=}")

# Space before positive
print(f"Price 1 is: ${price1: }")
print(f"Price 2 is: ${price2: }")
print(f"Price 3 is: ${price3: }")

# Thousands separator
print(f"Price 1 is: ${price1:,}")
print(f"Price 2 is: ${price2:,}")
print(f"Price 3 is: ${price3:,}")

# Combine flags: sign + thousands separator + 2 decimals
print(f"Price 1 is: ${price1:+,.2f}")
print(f"Price 2 is: ${price2:+,.2f}")
print(f"Price 3 is: ${price3:+,.2f}")
