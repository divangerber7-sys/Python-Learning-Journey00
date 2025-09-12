#   *args       = allows you to pass multiple non-keyword arguments (positional) - packed into a tuple
#   **kwargs    = allows you to pass multiple keyword arguments - packed into a dictionary
#                 Often called the "unpacking operator"
#   Order of precedence in function definitions:
#       1. positional
#       2. default
#       3. keyword
#       4. arbitrary (*args, **kwargs)

# Example 1: *args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # prints 55

# Example 2: display_name with *args
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# Example 3: **kwargs
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Homeland Str.",
              apt=100,
              city="San Diego",
              state="CA",
              zip=12345,
              country="USA")

# Exercise: Using both *args and **kwargs together
def shipping_label(*args, **kwargs):
    # Print positional info (e.g., name)
    for arg in args:
        print(arg, end=" ")
    print()

    # Address formatting logic
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

# Example usage
shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street="123 Homeland Str.",
               pobox="PO Box 1001",
               city="San Diego",
               state="CA",
               zip=12345,
               country="USA")
