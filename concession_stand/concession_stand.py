#   Concession Stand Program
#   dictionary {key:value}

menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 6.00,
        "Fries": 2.50,
        "Pretzel": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25}

cart = []
total = 0

#   Print out the menu
print("-------- MENU -------- ")
for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")
print("----------------------")

#   Take Orders
while True:
    food = input("Can I take your order? (q to quit): ").strip().title()
    if food == "Q":
        break
    elif food in menu:
        cart.append(food)
        print(f"Added {food} to your cart")
    else:
        print("Sorry. That item is not available. Please try again")

# Print the cart
print("\nYour Cart:")
for item in cart:
    print(item)

# Calculate total
for food in cart:
    total += menu.get(food)

print(f"\nYour total comes out to: ${total: .2f}")
print("Thank you for coming in today!\nMahalo")
