#   2D lists

# Example of a 2D list
#groceries = [["apple" , "banana", "grape"],
#             ["peas", "celery", "potatoes"],
#             ["chicken", "turkey", "fish"]]

# Accessing a specific item requires two indices
# print(groceries[0][0])  # apple

# Iterating over a 2D list
#for collection in groceries:
#    for food in collection:
#        print(food, end= " ")
#    print()

# EXERCISE - Create a 2D telephone keypad (tuple to maintain order)
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()
