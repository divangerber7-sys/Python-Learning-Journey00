#   Keyword arguments = An argument preceded by an identifier
#                       Helps with readability.
#                       Order of arguments doesn't matter when using keywords.
#   Order of precedence:
#       1. Positional
#       2. Default
#       3. Keyword
#       4. Arbitrary (*args, **kwargs)

# Example 1: Positional arguments
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Aloha", "Dr.", "Spongebob", "Squarepants")

# Example 2: Keyword arguments (order doesn’t matter)
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Aloha", title="Dr.", first="Spongebob", last="Squarepants")

# Example 3: Keyword args already in Python functions
for x in range(1, 11):
    print(x, end=" ")      # end is a keyword argument

print("\n")
print("1", "2", "3", "4", "5", sep="-")   # sep is a keyword argument


# Exercise: Get phone number
def get_phone(country_code, area_code, first, last):
    return f"{country_code}-{area_code}-{first}-{last}"

# Using keyword arguments makes it very clear which part is which
phone_num = get_phone(country_code="+27", area_code="123", first="869", last="9480")
print(phone_num)
