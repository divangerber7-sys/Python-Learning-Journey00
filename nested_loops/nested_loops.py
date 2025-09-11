#  nested loops = A loop within another loop (outer, inner)
#                 outer loop:
#                   inner loop:

# Example 1: Print numbers under each other
"""
for x in range (1,10):
    print(x)
"""

# Example 2: Print numbers in one line (end="")
"""
for x in range(1, 10):
    print(x, end = "")
"""

# Example 3: Outer loop controls repetition, inner loop prints sequence
"""
for x in range(3):
    for y in range(1, 10):
        print(y, end = "")
"""

# Example 4: Add a newline after inner loop finishes
"""
for x in range(3):
    for y in range(1, 10):
        print(y, end = "")
    print()
"""

# Example 5: Print a rectangle (user input)
rows = int(input("Please enter the number of rows:" ))
cols = int(input("Please enter the number of columns: "))
symbol = input("Please enter the symbol: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end = "")
    print()
