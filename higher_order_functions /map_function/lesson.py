# Higher-order functions
# map(function, collection) = Applies a given function to all items in a collection

# Example 1: Using a named function
def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temp = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

# Using map() with a named function
fahrenheit_temp = map(c_to_f, celsius_temp)

print("Using a named function:")
for temp in fahrenheit_temp:
    print(temp)

# Converting map object to a list
fahrenheit_temp = list(map(c_to_f, celsius_temp))
print("As list:", fahrenheit_temp)


# Example 2: Using a lambda function
fahrenheit_temp = map(lambda temp: (temp * 9/5) + 32, celsius_temp)

print("\nUsing a lambda function:")
for temp in fahrenheit_temp:
    print(temp)

# Converting to list with lambda
fahrenheit_temp = list(map(lambda temp: (temp * 9/5) + 32, celsius_temp))
print("As list:", fahrenheit_temp)


if __name__ == "__main__":
    # Rerun final example directly
    print("\nQuick rerun with lambda + list:")
    print(list(map(lambda t: (t * 9/5) + 32, celsius_temp)))
