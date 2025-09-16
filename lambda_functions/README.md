# Lesson 63: Lambda Functions

## 🔑 Key Concepts
- **Lambda functions** are anonymous, single-expression functions.  
- Syntax:  
  ```python
  lambda arguments: expression

EXAMPLE OUTPUT:

double = lambda x: x * 2
is_even = lambda x: x % 2 == 0

print(double(5))   # 10
print(is_even(8))  # True

