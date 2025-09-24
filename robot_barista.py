menu = ["Black Coffee", "Espresso", "Latte", "Cappucino", "Frappucino"]

print("Hello, welcome to the Coffee Emporium!!!")

name = input("What is your name?\n")

if name == "Divan":
    evil_status = input("Are you evil?\n").strip().lower()
    if evil_status == "yes":
        print("I am sorry but you are not welcome here")
        exit()
    else:
        print("Oh, so you are one of those good Divans. Welcome!!!")
else:
    print(f"Hello {name}. Thank you for coming in today.\n")

print(f"What would you like today? On our menu we have: {', '.join(menu)}")

order = input().title().strip()
quantity = int(input("How many would you like?\n"))

prices = {
    "Frappucino": 13,
    "Black Coffee": 3,
    "Espresso": 5,
    "Cappucino": 10,
    "Latte": 9
}

if order in prices:
    price = prices[order]
    if order == "Latte":
        latte_order = input("Do you want extra whipped cream? \n").strip().lower()
        if latte_order == "yes":
            price = 13
else:
    print("I am sorry, we don't have that here today")
    exit()

total = price * quantity
print(f"That is great. Your price is: ${total}")
print(f"We will have your {quantity} cups of {order} ready shortly. Have a great day!")
