#   Default arguments = A default value for certain parameters
#                       Default is used when that argument is omitted.
#                       Makes functions more flexible, reduces # of arguments.
#   Order of precedence:
#       1. Positional
#       2. Default
#       3. Keyword
#       4. Arbitrary (*args, **kwargs)

# Example 1: No defaults
def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))   # → 525.0


# Example 2: Add default discount and tax
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(505))            # Only uses tax default
print(net_price(505, 0.10))      # Uses discount + default tax
print(net_price(500, 0.10, 0))   # Overrides both defaults


# Exercise: Count-up timer using a default start
import time

def count(end, start=0):
    """Counts from start to end with a 1-second delay."""
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("We are done!")

# Example: Start from 15 instead of default 0
count(20, 15)
