# Higher-order functions
# reduce(function, collection) = Reduces elements in a collection to a single value
# ⚠️ Note: In many cases, a for-loop is clearer. 
# Reduce is useful for a functional programming style.

from functools import reduce

# Example 1: Using a named function
def add(x, y):
    return x + y

prices = [19.99, 1.00, 5.75, 12.99, 10.99]

total = reduce(add, prices)
print(f"Total (with named function): R{total:.2f}")

# Example 2: Using a lambda function
total = reduce(lambda x, y: x + y, prices)
print(f"Total (with lambda): R{total:.2f}")


if __name__ == "__main__":
    # Quick check: product of numbers
    nums = [2, 3, 4]
    product = reduce(lambda x, y: x * y, nums)
    print(f"Product of {nums} = {product}")
