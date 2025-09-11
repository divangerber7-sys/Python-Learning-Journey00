#   Shopping Cart Program

# .lower method takes input and converts to lower case to comply with code

foods = []
prices = []
total = 0

while True:
    food = input("What food would you like to buy? (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"What is the price of the {food} you would like to buy: R "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

# Can print output in horizontal line by print(food, end= " "). End skips new line
for food in foods:
    print(food)

for price in prices:
    # total = total + price - longer code
    total += price

print(f"Your total today is: R{total: 2}")
