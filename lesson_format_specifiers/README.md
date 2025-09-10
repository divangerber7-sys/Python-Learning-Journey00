# Lesson: Format Specifiers in Python

Format specifiers allow you to control how values are displayed when using **f-strings** or the `format()` function.  
They follow the syntax:

VALUE:FLAGS

---

## 🔑 Common Flags

- `.2f` → round to 2 decimal places (fixed point)  
- `:10` → allocate 10 spaces  
- `:03` → zero-pad with width of 3  
- `<` → left-align  
- `>` → right-align  
- `^` → center align  
- `+` → always show sign (`+` or `-`)  
- `=` → place sign at the leftmost position  
- (space) → insert a space for positive numbers  
- `,` → use comma as thousands separator  

---

## 🧪 Example Code
```python
price1 = 3000.87456
price2 = -613.3487
price3 = 1299.99

# Round numbers
print(f"Price 1 is: ${price1:.2f}")

# Allocate spaces
print(f"Price 1 is: ${price1:10}")

# Zero-padding
print(f"Price 1 is: ${price1:010}")

# Alignment
print(f"Left : ${price1:<10}")
print(f"Right: ${price1:>10}")
print(f"Center: ${price1:^10}")

# Signs
print(f"With sign: ${price1:+}")
print(f"Force sign left: ${price1:=}")
print(f"Space before positive: ${price1: }")

# Thousands separator
print(f"Comma: ${price1:,}")

# Combining flags
print(f"Formatted: ${price1:+,.2f}")

SAMPLE OUTPUT
Price 1 is: $3000.87
Price 1 is: $    3000.87456
Price 1 is: $0003000.87456
Left : $3000.87456
Right: $    3000.87456
Center: $ 3000.87456
With sign: $+3000.87456
Force sign left: $+3000.87456
Space before positive: $ 3000.87456
Comma: $3,000.87456
Formatted: $+3,000.87
