# Lambda function = A small anonymous function for one-time use (throwaway function).
# Syntax: lambda parameters: expression
# - Takes any number of arguments but only one expression
# - Useful in higher order functions: sort(), map(), filter(), reduce()

# Basic examples
double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: x % 2 == 0
age_check = lambda age: age >= 18

# Demonstration
if __name__ == "__main__":
    print(double(5))               # 10
    print(add(69, 3))              # 72
    print(max_value(69, 70))       # 70
    print(min_value(69, 70))       # 69
    print(full_name("Kevin", "Flynn"))  # Kevin Flynn
    print(is_even(8))              # True
    print(age_check(15))           # False
